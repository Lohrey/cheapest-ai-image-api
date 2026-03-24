"""
AI Image API — Python Client
https://api.pau1.cloud

Get your API key at api.pau1.cloud (first image free, no signup)
"""
import requests
import os

API_KEY = os.getenv("AI_IMAGE_API_KEY", "your_api_key_here")
BASE_URL = "https://api.pau1.cloud"


def generate_image(prompt: str, aspect_ratio: str = "1:1", model: str = "photorealistic") -> str:
    """
    Generate an AI image from a text prompt.
    
    Args:
        prompt: Text description of the image to generate
        aspect_ratio: "1:1", "16:9", "9:16", "4:3", or "3:4"
        model: "photorealistic", "digital-art", "anime", or "illustration"
    
    Returns:
        URL of the generated image
    """
    response = requests.post(
        f"{BASE_URL}/generate-image",
        headers={"x-api-key": API_KEY},
        json={"prompt": prompt, "aspect_ratio": aspect_ratio, "model": model}
    )
    response.raise_for_status()
    data = response.json()
    print(f"Credits remaining: {data.get('credits_remaining', 'N/A')}")
    return data["image_url"]


def get_balance() -> int:
    """Get remaining credit balance."""
    response = requests.get(
        f"{BASE_URL}/balance",
        headers={"x-api-key": API_KEY}
    )
    return response.json()["credits_remaining"]


# Examples
if __name__ == "__main__":
    # Generate a landscape
    url = generate_image("a serene Japanese garden at sunset with cherry blossoms", "16:9")
    print(f"Generated: {url}")
    
    # Generate a product shot
    url = generate_image("minimalist white headphones on a clean surface", "1:1", "photorealistic")
    print(f"Product shot: {url}")
    
    # Check balance
    balance = get_balance()
    print(f"Credits left: {balance}")
