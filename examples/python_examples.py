#!/usr/bin/env python3
"""
AI Image API - Python Examples
Cheapest AI image generation API: $0.20/image
Get your API key at: https://api.pau1.cloud
"""

import requests
import os
import json
from pathlib import Path

API_KEY = os.environ.get('AI_IMAGE_API_KEY', 'your_api_key_here')
BASE_URL = 'https://api.pau1.cloud'


def generate_image(prompt: str, aspect_ratio: str = '16:9', model: str = 'photorealistic') -> dict:
    """Generate an AI image from a text prompt."""
    response = requests.post(
        f'{BASE_URL}/generate-image',
        headers={
            'x-api-key': API_KEY,
            'Content-Type': 'application/json'
        },
        json={
            'prompt': prompt,
            'aspect_ratio': aspect_ratio,
            'model': model
        }
    )
    response.raise_for_status()
    return response.json()


def download_image(url: str, filename: str) -> None:
    """Download an image from URL to a local file."""
    response = requests.get(url)
    response.raise_for_status()
    with open(filename, 'wb') as f:
        f.write(response.content)
    print(f'Saved to {filename}')


def get_credits() -> dict:
    """Check remaining API credits."""
    response = requests.get(
        f'{BASE_URL}/credits',
        headers={'x-api-key': API_KEY}
    )
    return response.json()


# Example 1: Basic usage
if __name__ == '__main__':
    # Simple generation
    print('Generating image...')
    result = generate_image('a neon cyberpunk city at night, 4K, ultrarealistic')
    print(f'Image URL: {result["image_url"]}')
    print(f'Credits remaining: {result["credits_remaining"]}')

    # Download the image
    download_image(result['image_url'], 'cyberpunk_city.jpg')

    # Generate with different models
    models = ['photorealistic', 'digital-art', 'anime', 'minimalist']
    for model in models:
        result = generate_image(
            prompt='a mountain landscape at golden hour',
            aspect_ratio='16:9',
            model=model
        )
        print(f'{model}: {result["image_url"]}')

