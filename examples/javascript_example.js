// AI Image API - JavaScript/Node.js Examples
// Get your API key at: https://api.pau1.cloud

const API_KEY = process.env.AI_IMAGE_API_KEY || "your_api_key_here";
const BASE_URL = "https://api.pau1.cloud";

// Basic image generation
async function generateImage(prompt, options = {}) {
  const {
    aspectRatio = "16:9",
    model = "photorealistic",
    negativePrompt = null,
    seed = null,
  } = options;

  const response = await fetch(`${BASE_URL}/generate-image`, {
    method: "POST",
    headers: {
      "x-api-key": API_KEY,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      prompt,
      aspect_ratio: aspectRatio,
      model,
      ...(negativePrompt && { negative_prompt: negativePrompt }),
      ...(seed !== null && { seed }),
    }),
  });

  if (!response.ok) {
    throw new Error(`API error: ${response.status}`);
  }

  return response.json();
}

// Example usage
async function main() {
  console.log("Generating image...");

  // Basic example
  const result = await generateImage("a futuristic smart city at sunset");
  console.log("Image URL:", result.image_url);
  console.log("Credits remaining:", result.credits_remaining);

  // All available models
  const models = [
    "photorealistic",
    "digital-art",
    "anime",
    "3d-render",
    "watercolor",
    "minimalist",
  ];

  for (const model of models) {
    const r = await generateImage("a mountain landscape", { model });
    console.log(`${model}:`, r.image_url);
  }
}

main().catch(console.error);
