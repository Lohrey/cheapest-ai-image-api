# 🖼️ Cheapest AI Image API — $0.20/image, No Monthly Fees

The simplest REST API for AI image generation. No GCP setup. No monthly subscriptions. Just pay for what you use.

[![API Status](https://img.shields.io/badge/API-Live-brightgreen)](https://api.pau1.cloud)
[![Price](https://img.shields.io/badge/Price-from%20%240.20%2Fimage-blue)](https://api.pau1.cloud)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

## 🚀 Quick Start (3 Lines)

```bash
curl -X POST https://api.pau1.cloud/generate-image \
  -H "x-api-key: YOUR_KEY" \
  -d '{"prompt": "a neon cyberpunk city at night", "aspect_ratio": "16:9"}'
```

**[Try free demo (no signup) → api.pau1.cloud](https://api.pau1.cloud)**

## 💰 Pricing

| Package | Price | Cost Per Image |
|---------|-------|----------------|
| Starter | $4.99 | $0.50/image |
| Standard | $14.99 | $0.30/image |
| Pro | $39.99 | **$0.20/image** |

Credits **never expire**. No subscriptions. No hidden fees.

## 📦 Installation (Python)

```python
pip install requests
```

```python
import requests

def generate_image(prompt, aspect_ratio="1:1", api_key="YOUR_KEY"):
    response = requests.post(
        "https://api.pau1.cloud/generate-image",
        headers={"x-api-key": api_key},
        json={
            "prompt": prompt,
            "aspect_ratio": aspect_ratio,
            "model": "photorealistic"
        }
    )
    return response.json()["image_url"]

# Example usage
url = generate_image("a serene mountain landscape at sunrise", "16:9")
print(f"Generated: {url}")
```

## 📦 Installation (Node.js)

```javascript
const fetch = require('node-fetch');

async function generateImage(prompt, aspectRatio = '1:1') {
  const response = await fetch('https://api.pau1.cloud/generate-image', {
    method: 'POST',
    headers: {
      'x-api-key': 'YOUR_KEY',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ prompt, aspect_ratio: aspectRatio })
  });
  const data = await response.json();
  return data.image_url;
}

// Example
generateImage('minimalist tech workspace', '16:9').then(url => {
  console.log('Generated:', url);
});
```

## 🎨 Supported Models

- `photorealistic` — Photorealistic images
- `digital-art` — Digital artwork and illustrations
- `anime` — Anime and manga style
- `illustration` — Illustrated artwork

## 📐 Aspect Ratios

| Ratio | Use Case |
|-------|----------|
| `1:1` | Instagram posts, profile pictures |
| `16:9` | Landscape, desktop wallpapers, YouTube thumbnails |
| `9:16` | Mobile wallpapers, TikTok/Instagram Stories |
| `4:3` | Standard web images |
| `3:4` | Portrait photos |

## 🔑 Authentication

All requests require an `x-api-key` header with your API key.

Get your API key at [api.pau1.cloud](https://api.pau1.cloud) after purchasing credits.

## 📊 Comparison vs Competitors

| Provider | Price/Image | Monthly Fee | Setup Complexity |
|----------|-------------|-------------|-----------------|
| **api.pau1.cloud** | **$0.20–$0.50** | **None** | **Minimal (1 endpoint)** |
| OpenAI DALL-E 3 | $0.040–$0.120 | None | Medium |
| Stability AI | $0.01–$0.09 | From $20/mo | Complex |
| Google Imagen (via GCP) | $0.02 | None | High (GCP required) |
| Midjourney | N/A | $10+/mo | No API available |

*Our pricing is higher per-image but requires zero setup and no monthly commitment — ideal for prototypes, side projects, and low-volume production use.*

## 🛠️ API Reference

### POST /generate-image

**Request:**
```json
{
  "prompt": "string (required) — Image description",
  "aspect_ratio": "1:1 | 16:9 | 9:16 | 4:3 | 3:4 (default: 1:1)",
  "model": "photorealistic | digital-art | anime | illustration (default: photorealistic)",
  "output_format": "jpeg | png (default: jpeg)"
}
```

**Response:**
```json
{
  "success": true,
  "image_url": "https://cdn.example.com/image.jpg",
  "credits_remaining": 9,
  "generation_time_ms": 7823
}
```

### GET /balance

Check remaining credits:
```bash
curl https://api.pau1.cloud/balance \
  -H "x-api-key: YOUR_KEY"
```

## 🎯 Use Cases

- **E-commerce** — Generate product lifestyle photos programmatically
- **Content tools** — Automate blog/social media thumbnail creation
- **MVPs & prototypes** — Add AI image generation to your app in minutes
- **Internal tools** — Create branded visuals without a designer
- **Games** — Generate character art, backgrounds, assets

## 🚀 Live Demo

Try it at **[api.pau1.cloud](https://api.pau1.cloud)** — first image free, no signup required.

## 📞 Support

- Issues: [GitHub Issues](https://github.com/Lohrey/cheapest-ai-image-api/issues)
- Email: support@pau1.cloud

---

*Made by indie developers, for indie developers. We hate overpriced AI APIs too.*
