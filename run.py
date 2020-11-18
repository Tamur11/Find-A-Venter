import cv2
import pytesseract
import pyautogui
import time
import re
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

time.sleep(3)

image = pyautogui.screenshot("logs.png", region=(441, 128, 985, 933))  # screenshot

img = cv2.imread("logs.png")  # read with cv2

text = pytesseract.image_to_string(img)  # read with tesseract

# TEXT FORMATTING
# text = re.sub(r'[\W_]+', ' ', text)
print(text)
# log = [entry for entry in log if "sensor" in entry]

# lines = [line for line in lines if 'sensor' in line]


# print(lines)
# pyautogui.alert(name + " Vented!")