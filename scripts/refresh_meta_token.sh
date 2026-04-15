#!/usr/bin/env bash
# ============================================================
# refresh_meta_token.sh
# Renueva el META_ACCESS_TOKEN (long-lived, ~60 días) en .env
# Uso: bash scripts/refresh_meta_token.sh
# ============================================================

ENV_FILE="$(dirname "$0")/../.env"

# Leer credenciales del .env
APP_ID=$(grep '^META_APP_ID=' "$ENV_FILE" | cut -d'=' -f2)
APP_SECRET=$(grep '^META_APP_SECRET=' "$ENV_FILE" | cut -d'=' -f2)
CURRENT_TOKEN=$(grep '^META_ACCESS_TOKEN=' "$ENV_FILE" | cut -d'=' -f2)

if [[ -z "$APP_ID" || -z "$APP_SECRET" || -z "$CURRENT_TOKEN" ]]; then
  echo "ERROR: Faltan META_APP_ID, META_APP_SECRET o META_ACCESS_TOKEN en .env"
  exit 1
fi

echo "Renovando token de Meta Ads..."

RESPONSE=$(curl -s "https://graph.facebook.com/v19.0/oauth/access_token?grant_type=fb_exchange_token&client_id=${APP_ID}&client_secret=${APP_SECRET}&fb_exchange_token=${CURRENT_TOKEN}")

# Extraer nuevo token
NEW_TOKEN=$(echo "$RESPONSE" | grep -o '"access_token":"[^"]*"' | cut -d'"' -f4)
EXPIRES_IN=$(echo "$RESPONSE" | grep -o '"expires_in":[0-9]*' | cut -d':' -f2)

if [[ -z "$NEW_TOKEN" ]]; then
  echo "ERROR: No se pudo obtener nuevo token. Respuesta de Meta:"
  echo "$RESPONSE"
  exit 1
fi

DAYS=$((EXPIRES_IN / 86400))
TODAY=$(date +%Y-%m-%d)
NEXT_RENEWAL=$(date -d "+50 days" +%Y-%m-%d 2>/dev/null || date -v+50d +%Y-%m-%d)

# Actualizar token en .env
sed -i "s|^META_ACCESS_TOKEN=.*|META_ACCESS_TOKEN=${NEW_TOKEN}|" "$ENV_FILE"

# Actualizar comentario con fechas
sed -i "s|# Última renovación:.*|# Última renovación: ${TODAY} | Próxima renovación: ~${NEXT_RENEWAL}|" "$ENV_FILE"

echo "✓ Token renovado exitosamente"
echo "  Expira en: ${DAYS} días (~${TODAY} + ${DAYS}d)"
echo "  Próxima renovación recomendada: ${NEXT_RENEWAL}"
