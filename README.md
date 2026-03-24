# Cheapest AI Image API — $0.20/image, No Monthly Fees

> The simplest REST API for AI image generation. One endpoint. Pay as you go. No subscription required.

[![API Status](https://img.shields.io/badge/API-Live-brightgreen)](https://api.pau1.cloud)
[![Price](https://img.shields.io/badge/Price-from%20%240.20%2Fimage-blue)](https://api.pau1.cloud)
[![No Subscription](https://img.shields.io/badge/Subscription-None-orange)](https://api.pau1.cloud)

**👉 [Try it FREE at api.pau1.cloud](https://api.pau1.cloud)**

## Why This API?

Every AI image API I tried had the same problems:

| API | Problem |
|-----|---------|
| OpenAI DALL-E | Billing setup required, $0.04–$0.08/image |
| Stability AI | Complex tier system, confusing credits |
| Midjourney | **No API at all** |
| Google Imagen | Full GCP setup required |

I built this API for developers who just want: **call endpoint → get image → pay fair price**.

## Quick Start (3 Lines)

```bash
curl -X POST https://api.pau1.cloud/generate-image \
  -H "x-api-key: YOUR_KEY" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "a neon cyberpunk city at night", "aspect_ratio": "16:9", "model": "photorealistic"}'
```

### Response

```json
{
  "success": true,
  "image_url": "https://cdn.api.pau1.cloud/images/abc123.jpg",
  "credits_remaining": 9,
  "generation_time_ms": 3200
}
```

## Code Examples

### Python

```python
import requests

API_KEY = "your_api_key_here"

response = requests.post(
    "https://api.pau1.cloud/generate-image",
    headers={"x-api-key": API_KEY},
    json={
        "prompt": "minimalist tech workspace, 4K, professional",
        "aspect_ratio": "16:9",
        "model": "photorealistic"
    }
)

data = response.json()
print(f"Image URL: {data['image_url']}")
print(f"Credits remaining: {data['credits_remaining']}")
```

### JavaScript / Node.js

```javascript
const generateImage = async (prompt) => {
  const response = await fetch('https://api.pau1.cloud/generate-image', {
    method: 'POST',
    headers: {
      'x-api-key': process.env.AI_IMAGE_API_KEY,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      prompt,
      aspect_ratio: '16:9',
      model: 'photorealistic'
    })
  });

  const data = await response.json();
  return data.image_url;
};

// Usage
const imageUrl = await generateImage('futuristic smart city at sunset');
console.log(imageUrl);
```

### TypeScript

```typescript
interface GenerateImageResponse {
  success: boolean;
  image_url: string;
  credits_remaining: number;
  generation_time_ms: number;
}

const generateImage = async (prompt: string): Promise<string> => {
  const response = await fetch('https://api.pau1.cloud/generate-image', {
    method: 'POST',
    headers: {
      'x-api-key': process.env.AI_IMAGE_API_KEY!,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      prompt,
      aspect_ratio: '16:9',
      model: 'photorealistic',
    }),
  });

  const data: GenerateImageResponse = await response.json();
  return data.image_url;
};
```

### PHP

```php
<?php
function generateImage(string $prompt, string $apiKey): string {
    $response = file_get_contents('https://api.pau1.cloud/generate-image', false, stream_context_create([
        'http' => [
            'method' => 'POST',
            'header' => "x-api-key: {$apiKey}\r\nContent-Type: application/json\r\n",
            'content' => json_encode([
                'prompt' => $prompt,
                'aspect_ratio' => '16:9',
                'model' => 'photorealistic'
            ])
        ]
    ]));
    
    return json_decode($response, true)['image_url'];
}

$imageUrl = generateImage('a cozy coffee shop in Paris', 'YOUR_API_KEY');
echo $imageUrl;
```

## Pricing

| Package | Price | Images | Cost Per Image | Features |
|---------|-------|--------|----------------|---------|
| **Starter** | $4.99 | 10 | $0.50/image | All models, never expire |
| **Standard** | $14.99 | 50 | $0.30/image | All models, never expire |
| **Pro** | $39.99 | 200 | $0.20/image | All models, priority queue |

**✅ Credits never expire**  
**✅ No subscription, no hidden fees**  
**✅ No GCP account required**  
**✅ First image free — no signup needed**

👉 **[Buy Credits at api.pau1.cloud](https://api.pau1.cloud)**

## Available Models

| Model | Description | Best For |
|-------|-------------|---------|
| `photorealistic` | Ultra-realistic photos | Products, people, landscapes |
| `digital-art` | Digital illustration style | Game assets, concept art |
| `anime` | Anime/manga style | Characters, scenes |
| `3d-render` | 3D rendered objects | Products, architectural |
| `watercolor` | Painterly style | Artistic projects |
| `minimalist` | Clean, simple designs | Icons, logos, UI |

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `prompt` | string | ✅ | Image description (max 1000 chars) |
| `aspect_ratio` | string | ✅ | `16:9`, `1:1`, `9:16`, `4:3`, `3:4` |
| `model` | string | ❌ | Defaults to `photorealistic` |
| `negative_prompt` | string | ❌ | What to avoid in the image |
| `seed` | integer | ❌ | For reproducible results |

## What You Can Build

- 🛒 **E-commerce product image generators**
- 📱 **Social media content automation**
- 🎮 **Game asset generators for indie devs**
- 🖼️ **AI art apps and MVPs**
- 📸 **Automated thumbnail generators**
- 🏢 **Internal design tools**
- 📰 **Blog post image generators**
- 🎨 **Creative tools for makers**

## Rate Limits

- 10 requests/minute (Starter)
- 30 requests/minute (Standard)
- 100 requests/minute (Pro)

## Error Codes

| Code | Meaning |
|------|---------|
| `401` | Invalid or missing API key |
| `402` | Insufficient credits |
| `422` | Invalid parameters |
| `429` | Rate limit exceeded |
| `500` | Generation failed — retry |

## Getting Your API Key

1. Go to [api.pau1.cloud](https://api.pau1.cloud)
2. Click "Get API Key"
3. Choose a credit package
4. Start generating immediately — no waiting period

## FAQ

**Q: Do credits expire?**  
A: No. Credits never expire. Use them whenever you want.

**Q: Is there a free tier?**  
A: Yes — first image is free, no signup required. Test the API before buying.

**Q: Can I use the images commercially?**  
A: Yes, all generated images can be used commercially.

**Q: What image formats are returned?**  
A: JPEG by default. PNG available on request.

**Q: How fast is generation?**  
A: Typically 2–5 seconds per image depending on model and complexity.

## Changelog

- **v1.0** — Initial release with 6 models
- **v1.1** — Added seed parameter for reproducible results  
- **v1.2** — PNG format support added

## Support

- 🌐 **Website:** [api.pau1.cloud](https://api.pau1.cloud)
- 📧 **Email:** p.l@mail.de
- 🐛 **Issues:** Open a GitHub issue

---

*Built by an indie developer who was tired of complex AI APIs. Made simple on purpose.*

**[→ Start generating images now](https://api.pau1.cloud)**
