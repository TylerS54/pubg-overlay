import time
import logging
import argparse
from typing import Tuple

import os
import pyautogui
from PIL import Image
import pytesseract


def get_screen_region(width: int, height: int) -> Tuple[int, int, int, int]:
    screen_width, screen_height = pyautogui.size()
    left = max(screen_width - width, 0)
    top = 0
    return left, top, width, height


def capture_region(region: Tuple[int, int, int, int]) -> Image.Image:
    """Capture a region of the screen."""
    screenshot = pyautogui.screenshot(region=region)
    return screenshot


def extract_text(image: Image.Image) -> str:
    """Extract text from image using pytesseract."""
    return pytesseract.image_to_string(image)


def monitor(width: int, height: int, interval: float, log_file: str, tesseract_cmd: str) -> None:
    if tesseract_cmd:
        pytesseract.pytesseract.tesseract_cmd = tesseract_cmd
    logging.basicConfig(filename=log_file, level=logging.INFO,
                        format="%(asctime)s %(message)s")
    region = get_screen_region(width, height)
    previous_text = ""
    logging.info("Monitoring started. Region: %s", region)
    print(f"Monitoring region: {region}. Press Ctrl+C to stop.")
    try:
        while True:
            image = capture_region(region)
            text = extract_text(image).strip()
            if text != previous_text:
                logging.info("Text changed: %s", text)
                print(f"Text changed: {text}")
                previous_text = text
            time.sleep(interval)
    except KeyboardInterrupt:
        print("Monitoring stopped.")
        logging.info("Monitoring stopped by user.")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Monitor top-right corner of screen and log text changes.")
    parser.add_argument("--width", type=int, default=300, help="Width of region to capture (pixels)")
    parser.add_argument("--height", type=int, default=200, help="Height of region to capture (pixels)")
    parser.add_argument("--interval", type=float, default=1.0, help="Seconds between captures")
    parser.add_argument("--log", type=str, default="text_log.txt", help="File to log detected text")
    parser.add_argument("--tesseract", type=str, default=os.getenv('TESSERACT_CMD', ''),
                        help="Path to tesseract executable (optional)")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    monitor(args.width, args.height, args.interval, args.log, args.tesseract)
