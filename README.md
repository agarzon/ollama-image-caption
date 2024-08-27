# Ollama Image Description Script

This project provides a Python script that reads images from a specified folder, uses the `llava` model from the Ollama API to generate descriptions for each image, and saves these descriptions in a corresponding `.txt` file. This script is ideal for developers and researchers working with image datasets who need to generate textual descriptions automatically.

## Features

- **Automatic Image Description:** The script uses the `llava` model to describe images.
- **Batch Processing:** Processes all images in a specified folder.
- **Output to Text Files:** Saves descriptions in `.txt` files with the same names as the corresponding images.

## How It Works

1. The script converts images to base64 encoding.
2. It sends the base64 image data to the Ollama API, specifying the `llava` model.
3. The API returns a description of the image, which the script saves in a `.txt` file.

## Installation

### Prerequisites

- **Python 3.7+**
- **Pip** (Python package installer)
- **Ollama API** running locally (default at `http://localhost:11434`)

### Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/ollama-image-description.git
   cd ollama-image-description
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

### Requirements

Create a `requirements.txt` file in the project directory containing:

```plaintext
requests
Pillow
```

## Usage

1. **Activate the virtual environment:**

   ```bash
   source myenv/bin/activate
   ```

2. **Run the script:**

   ```bash
   python script_name.py
   ```

   Replace `script_name.py` with the name of your script.

3. **Output:**
   - The script processes each image in the specified folder and generates a `.txt` file with the description.

## Example

If you have an image named `example.jpg`, the script will generate a description and save it in `example.txt` in the same folder.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contribution

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements, bug fixes, or other improvements.

## Contact

For questions or feedback, please contact [yourname@example.com](mailto:yourname@example.com).

---

**Disclaimer:** This project is for educational and research purposes. Make sure to comply with the terms and conditions of the Ollama API and any other third-party services used.
