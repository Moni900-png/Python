import cv2
import time
import pygetwindow as gw
from PIL import ImageGrab
import easyocr


# Function to find and return the Chrome window if visible
def find_chrome_window():
    chrome_windows = [win for win in gw.getWindowsWithTitle('Google Chrome') if win.visible]
    return chrome_windows[0] if chrome_windows else None


# Function to wait for webpage to load (adjust as needed)
def wait_for_webpage_load():
    time.sleep(5)  # Adjust timing based on webpage load speed


# Function to take screenshot of Chrome window displaying a specific website
def take_website_screenshot(url):
    # Open Chrome browser and navigate to the URL (replace with your URL)
    # This is an example and won't open Chrome automatically; you need to open it manually
    chrome_window = find_chrome_window()

    if chrome_window:
        chrome_window.activate()
        wait_for_webpage_load()  # Wait for the webpage to load

        # Get Chrome window bounds
        left, top, right, bottom = chrome_window.left, chrome_window.top, chrome_window.right, chrome_window.bottom

        # Calculate the actual size of the Chrome window (excluding borders)
        chrome_window_width = right - left
        chrome_window_height = bottom - top

        # Take screenshot using Pillow's ImageGrab
        screenshot = ImageGrab.grab(bbox=(left, top, left + chrome_window_width, top + chrome_window_height))

        # Save the screenshot
        screenshot_path = "screenshot.png"
        screenshot.save(screenshot_path)

        print("Screenshot saved successfully.")
        return screenshot_path
    else:
        print("No visible Chrome window found.")
        return None


# Function to check if a given text is present in the OCR output
def is_text_present(ocr_output, expected_text):
    for result in ocr_output:
        text = result[1]
        if expected_text.lower() in text.lower():
            return True
    return False


# Example usage
if __name__ == "__main__":
    url_to_capture = "https://www.swiggy.com/"  # Replace with the URL you want to capture

    # Take screenshot of the website
    screenshot_path = take_website_screenshot(url_to_capture)

    if screenshot_path:
        # Load the screenshot image
        screenshot = cv2.imread(screenshot_path)

        # Perform OCR on the screenshot
        reader = easyocr.Reader(['en'])
        ocr_results = reader.readtext(screenshot)

        # Expected text to compare against
        expected_text = "What's on your mind?"

        # Check if the expected text is present in the OCR results
        text_found = is_text_present(ocr_results, expected_text)

        # Output the result
        if text_found:
            print(f"Expected text '{expected_text}' found in the screenshot.")
        else:
            print(f"Expected text '{expected_text}' not found in the screenshot.")

