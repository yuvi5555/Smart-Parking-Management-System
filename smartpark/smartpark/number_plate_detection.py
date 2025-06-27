import cv2
import pytesseract

# Set the Tesseract path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def detect_plate(image_path):
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        return "Image not found"

    # Resize for better OCR (optional)
    image = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Sharpen the image using thresholding
    _, thresh = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # OCR with PSM 7 (single line of text) and OEM 3 (best)
    custom_config = r'--oem 3 --psm 7 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    text = pytesseract.image_to_string(thresh, config=custom_config)

    # Clean result
    plate = ''.join(filter(str.isalnum, text))
    return plate if plate else "Plate not detected"
