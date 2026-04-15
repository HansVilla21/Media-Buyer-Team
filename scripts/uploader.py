"""
Módulo compartido de publicación en Instagram via Upload Post API.
Usado por: noticias_ia_carousel.py, tips_carousel.py

API docs : https://docs.upload-post.com/
Endpoint : POST https://api.upload-post.com/api/upload_photos
Auth     : Authorization: Apikey YOUR_KEY

────────────────────────────────────────────────────────────────────
USO DIRECTO (para publicar slides ya generados):

  python scripts/uploader.py --dir outputs/tips/2026-03-12/claude-vs-chatgpt
  python scripts/uploader.py --dir outputs/noticias/2026-03-12 --fecha "2026-03-13T09:00:00-06:00"

────────────────────────────────────────────────────────────────────
"""

import os
import json
import uuid
import glob
import argparse
import urllib.request
import urllib.error
from datetime import datetime

BASE                  = "C:/Users/hvill/Documents/Cloude Code/Media Buyer Team"
UPLOAD_POST_ENDPOINT  = "https://api.upload-post.com/api/upload_photos"

HASHTAGS = (
    "#IA #InteligenciaArtificial #ChatGPT #Claude #Gemini "
    "#ProductividadIA #Automatizacion #TipsIA #AprendeIA "
    "#LATAM #EmprendimientoDigital #MomentumAI"
)


# ─── Helpers ──────────────────────────────────────────────────────────────────

def load_env():
    env = {}
    path = f"{BASE}/.env"
    if not os.path.exists(path):
        return env
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip()
    return env


def _build_multipart(fields, files):
    """
    Construye un body multipart/form-data sin librerías externas.

    Args:
        fields : dict  {name: value}  — campos de texto
        files  : list  [{name, path}] — archivos a adjuntar

    Returns:
        (body_bytes, content_type_header_value)
    """
    boundary = uuid.uuid4().hex
    parts    = []

    for name, value in fields.items():
        if value is None:
            continue
        parts.append(
            f"--{boundary}\r\n"
            f'Content-Disposition: form-data; name="{name}"\r\n\r\n'
            f"{value}\r\n".encode("utf-8")
        )

    for finfo in files:
        filename = os.path.basename(finfo["path"])
        with open(finfo["path"], "rb") as fh:
            file_data = fh.read()
        header = (
            f"--{boundary}\r\n"
            f'Content-Disposition: form-data; name="{finfo["name"]}"; filename="{filename}"\r\n'
            f"Content-Type: image/png\r\n\r\n"
        ).encode("utf-8")
        parts.append(header + file_data + b"\r\n")

    parts.append(f"--{boundary}--\r\n".encode("utf-8"))

    body         = b"".join(parts)
    content_type = f"multipart/form-data; boundary={boundary}"
    return body, content_type


def slides_en_directorio(out_dir):
    """Devuelve los PNGs de un directorio de carrusel ordenados por nombre."""
    archivos = sorted(glob.glob(f"{out_dir}/slide-*.png"))
    return archivos


# ─── Función principal ────────────────────────────────────────────────────────

def publicar_carousel(
    slides_paths,
    caption,
    scheduled_date=None,
    api_key=None,
    ig_user=None,
    dry_run=False,
):
    """
    Publica (o programa) un carrusel en Instagram via Upload Post API.

    Args:
        slides_paths  : Lista de rutas absolutas a los PNG en orden de publicación
        caption       : Texto del post completo (copy + hashtags)
        scheduled_date: ISO-8601 con timezone, ej: "2026-03-13T09:00:00-06:00"
                        None = publicar de inmediato
        api_key       : API key de Upload Post. Si None, lee UPLOAD_POST_API_KEY del .env
        ig_user       : Usuario de Instagram conectado en Upload Post. Si None, lee IG_ACCOUNT del .env
        dry_run       : Si True, muestra toda la info pero NO envía la request

    Returns:
        dict: {"status": int, "response": dict | str}
    """
    env  = load_env()
    key  = api_key or env.get("UPLOAD_POST_API_KEY", "")
    user = ig_user or env.get("IG_ACCOUNT", "hansvilla.ai")

    # ── Validaciones ──
    if not key:
        print("❌  UPLOAD_POST_API_KEY no encontrada en .env")
        print("    Agregá: UPLOAD_POST_API_KEY=tu-api-key")
        return {"status": 0, "response": "missing_api_key"}

    if not slides_paths:
        print("❌  No hay slides para publicar.")
        return {"status": 0, "response": "no_slides"}

    if len(slides_paths) > 10:
        print(f"⚠️   Instagram acepta máximo 10 slides por carrusel. Se usan los primeros 10.")
        slides_paths = slides_paths[:10]

    missing = [p for p in slides_paths if not os.path.exists(p)]
    if missing:
        for m in missing:
            print(f"❌  Archivo no encontrado: {m}")
        return {"status": 0, "response": "missing_files"}

    # ── Preview en consola ──
    print("\n" + "─" * 56)
    print("  📤  PUBLICACIÓN EN INSTAGRAM")
    print("─" * 56)
    print(f"  Usuario  : @{user}")
    print(f"  Slides   : {len(slides_paths)} imágenes")
    for i, p in enumerate(slides_paths, 1):
        print(f"             {i}. {os.path.basename(p)}")
    print(f"  Caption  : {caption[:90]}{'...' if len(caption) > 90 else ''}")
    if scheduled_date:
        print(f"  Programa : {scheduled_date}")
    else:
        print(f"  Timing   : ahora")
    print("─" * 56)

    if dry_run:
        print("\n⚠️   MODO DRY RUN — no se envió ninguna request.\n")
        return {"status": 0, "response": "dry_run"}

    # ── Construir y enviar request ──
    fields = {
        "user":             user,
        "platform[]":       "instagram",
        "title":            caption,
        "instagram_title":  caption,
    }
    if scheduled_date:
        fields["scheduled_date"] = scheduled_date

    files = [{"name": "photos[]", "path": p} for p in slides_paths]

    body, content_type = _build_multipart(fields, files)

    req = urllib.request.Request(
        UPLOAD_POST_ENDPOINT,
        data=body,
        headers={
            "Authorization": f"Apikey {key}",
            "Content-Type":  content_type,
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=90) as r:
            status   = r.status
            raw      = r.read().decode("utf-8")
            try:
                response = json.loads(raw)
            except Exception:
                response = raw

        if status in (200, 202):
            if scheduled_date:
                print(f"\n✅  Carrusel programado para {scheduled_date}")
            else:
                print(f"\n✅  Carrusel publicado en @{user}")
        else:
            print(f"\n⚠️   Respuesta inesperada: HTTP {status}")

        return {"status": status, "response": response}

    except urllib.error.HTTPError as e:
        body_err = e.read().decode("utf-8")
        print(f"\n❌  Error HTTP {e.code}: {body_err}")
        return {"status": e.code, "response": body_err}

    except Exception as e:
        print(f"\n❌  Error inesperado: {e}")
        return {"status": 0, "response": str(e)}


# ─── Caption generators ───────────────────────────────────────────────────────

def caption_tips(titulo_carrusel):
    """Caption estándar para carruseles de tips."""
    return (
        f"{titulo_carrusel}\n\n"
        f"Guardá este post para cuando lo necesites 🔖\n\n"
        f"{HASHTAGS}"
    )


def caption_noticias(fecha=None):
    """Caption estándar para carruseles de noticias."""
    fecha_str = fecha or datetime.now().strftime("%d/%m/%Y")
    return (
        f"Lo que pasó en IA esta semana ({fecha_str}) 🤖\n\n"
        f"Las noticias más importantes para que nada te pase por alto.\n\n"
        f"Guardá este post 🔖\n\n"
        f"{HASHTAGS}"
    )


# ─── CLI standalone (para publicar carpetas ya generadas) ─────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Publica slides PNG de un directorio en Instagram via Upload Post"
    )
    parser.add_argument("--dir",     "-d", required=True,
                        help="Carpeta con los slide-*.png (ej: outputs/tips/2026-03-12/claude)")
    parser.add_argument("--caption", "-c", default="",
                        help="Caption personalizado. Si se omite, se auto-genera.")
    parser.add_argument("--fecha",   "-f", default=None,
                        help="Fecha de publicación ISO-8601 (ej: 2026-03-13T09:00:00-06:00). "
                             "Si se omite, publica ahora.")
    parser.add_argument("--dry-run", action="store_true",
                        help="Muestra la info pero no envía la request.")
    args = parser.parse_args()

    out_dir = args.dir if os.path.isabs(args.dir) else f"{BASE}/{args.dir}"
    slides  = slides_en_directorio(out_dir)

    if not slides:
        print(f"❌  No se encontraron slide-*.png en: {out_dir}")
        return

    cap = args.caption or caption_noticias()

    publicar_carousel(
        slides_paths   = slides,
        caption        = cap,
        scheduled_date = args.fecha,
        dry_run        = args.dry_run,
    )


if __name__ == "__main__":
    main()
