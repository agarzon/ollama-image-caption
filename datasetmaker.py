import os
import base64
import requests
import sys
from PIL import Image

# Ensure the script is running in a virtual environment
def ensure_venv():
    if sys.prefix == sys.base_prefix:
        print("Please activate the virtual environment first!")
        sys.exit(1)

# Convert image to base64 encoding
def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

# Fetch image description from Ollama API
def get_image_description(image_base64, model_name, api_url):
    payload = {
        "model": model_name,
        "prompt": "I want you to describe this image. Be consise and only describe what you are sure of. Do not make assumptions. You description will be used to train a model. Only describe what you see in the image. No more than 20 words.",
        "stream": False,
        "images": [image_base64]
    }
    try:
        response = requests.post(api_url, json=payload)
        response.raise_for_status()
        return response.json().get("response", "").strip()
    except requests.exceptions.RequestException as e:
        print(f"Failed to get description for the image: {e}")
        return None

# Process images in the specified folder
def process_images(image_folder, model_name, api_url):
    for filename in os.listdir(image_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(image_folder, filename)
            image_base64 = image_to_base64(image_path)
            description = get_image_description(image_base64, model_name, api_url)
            if description:
                save_description(image_folder, filename, description)
            print(f"Processed {filename}")

# Save description to a text file with the same name as the image
def save_description(image_folder, filename, description):
    text_filename = os.path.splitext(filename)[0] + ".txt"
    text_path = os.path.join(image_folder, text_filename)
    with open(text_path, "w") as text_file:
        text_file.write(description)

# Main entry point
def main():
    ensure_venv()

    # Set your Ollama API URL and the model name
    api_url = "http://localhost:11434/api/generate"
    model_name = "llava"

    # Define the folder containing your images
    image_folder = "/home/agarzon/GIT/experiments/ollama-dataset/images"

    process_images(image_folder, model_name, api_url)
    print("All images processed.")

if __name__ == "__main__":
    main()
