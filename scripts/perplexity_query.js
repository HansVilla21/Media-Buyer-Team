const https = require('https');

const API_KEY = process.argv[2];
const query = process.argv[3];
const recency = process.argv[4] || 'month';

const payload = JSON.stringify({
  model: 'sonar-pro',
  messages: [{ role: 'user', content: query }],
  search_recency_filter: recency
});

const options = {
  hostname: 'api.perplexity.ai',
  path: '/chat/completions',
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + API_KEY
  }
};

const req = https.request(options, (res) => {
  let data = '';
  res.on('data', chunk => data += chunk);
  res.on('end', () => {
    try {
      const result = JSON.parse(data);
      if (result.choices && result.choices[0]) {
        console.log('=== RESPUESTA ===');
        console.log(result.choices[0].message.content);
        if (result.citations && result.citations.length > 0) {
          console.log('\n=== FUENTES ===');
          result.citations.forEach((c, i) => console.log((i+1) + '. ' + c));
        }
      } else {
        console.log('ERROR en respuesta:', data);
      }
    } catch(e) {
      console.log('Error parseando:', e.message, data.substring(0,500));
    }
  });
});
req.on('error', (e) => console.error('Error request:', e.message));
req.write(payload);
req.end();
