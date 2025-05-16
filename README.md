# PUBG Overlay Monitor

This project provides a small desktop application that monitors the top-right corner of the screen, reads any text that appears there, and logs changes.

## Requirements

- Python 3.8+
- `pyautogui`
- `pytesseract`
- `pillow`
- Tesseract OCR engine (e.g., `sudo apt-get install tesseract-ocr`)

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the monitor from a terminal:

```bash
python monitor_top_right.py
```

### Options

- `--width`: width of the region to capture (default: 300)
- `--height`: height of the region to capture (default: 200)
- `--interval`: seconds between captures (default: 1.0)
- `--log`: file to log detected text (default: `text_log.txt`)
- `--tesseract`: path to the Tesseract executable (defaults to `TESSERACT_CMD` env var if set)

Press `Ctrl+C` in the terminal to stop the monitoring.
