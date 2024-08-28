# Ollama image caption tool

This project provides a Python script that reads images from a specified folder, uses the `llava` model from the Ollama API to generate descriptions for each image, and saves these descriptions in a corresponding `.txt` file. This script is ideal for developers and researchers working with image datasets who need to generate textual descriptions automatically.

## Features

- **Automatic Image Description:** The script uses the `llava` model to describe images.
- **Batch Processing:** Processes all images ('.png', '.jpg', '.jpeg') in the folder.
- **Output to Text Files:** Saves descriptions in `.txt` files with the same names as the corresponding images.

## How It Works

1. The script converts images to base64 encoding.
2. It sends the base64 image data to the Ollama API, specifying the `llava` model.
3. The API returns a description of the image, which the script saves in a `.txt` file.

## Installation

### Prerequisites

- **Python 3.9+**
- **Pip** (Python package installer)
- **Ollama API** running locally (default at `http://localhost:11434`)

### Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/agarzon/ollama-image-caption.git
   cd ollama-image-caption
   ```

2. **Create and activate a virtual environment:**

   - On Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Put all the images you want to process in the `images` folder.

2. **Activate the virtual environment:**

   ```bash
   source myenv/bin/activate
   ```

3. **Run the script:**

   ```bash
   python script_name.py
   ```

   Replace `script_name.py` with the name of your script.

4. **Output:**
   - The script processes each image in the specified folder and generates a `.txt` file with the description.

## Example

If you have an image named `example.jpg`, the script will generate a description and save it in `example.txt` in the same folder.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

**Disclaimer:** This project is for educational and research purposes. Make sure to comply with the terms and conditions of the Ollama API and any other third-party services used.
