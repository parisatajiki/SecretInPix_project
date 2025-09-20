# SecretInPix

**SecretInPix** is a Python-based project that demonstrates how to hide and retrieve text messages directly inside images.
Each character of the text is stored in the red (R) channel of the pixels. Once the text ends, remaining pixels are filled with blue (0, 0, 255) as a marker.
The program can then decode the text by reading the red channel values until it encounters the blue pixels, making it a simple yet effective example of pixel-based steganography.

---

## Features

- **Encode text into images**: Hide text directly in the red channel of pixels.
- **Decode text from images**: Retrieve the hidden text easily.
- **Step-based scanning**: Efficiently skips pixels for faster encoding/decoding.
- **Educational and simple**: Great for learning image-based steganography with Python.

---

## Installation

1. Make sure you have Python installed (3.x recommended).
2. Install the required library:
```bash
pip install pil
```
## Usage

### Encode Text
```bash
python encode.py
```
### Decode Text
```bash
python decode.py
```

