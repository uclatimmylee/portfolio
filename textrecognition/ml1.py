import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

#read the image
img = cv2.imread("receipt2.jpg")

#color change to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#changes color value to either 0 or 255 depending on comparison with threshold value
#OTSU automatically selects a threshold value
#Binary sets values to either 0 or 255, inv switches to 255 or 0
#ret returns what threshold was used, thresh1 is the new image
ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

#defines a rectangle, using kernel size(18,18)
#bigger kernel groups larger blocks of text together
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (50000,50000))

#dilation expands the text blocks
dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)

#takes in source image, countour retrieval method, and approximation method
#returns list of all contours
contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

img2 = img.copy()

file = open("text.txt", "w+")
file.write("")
file.close()

for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    
    rect = cv2.rectangle(img2, (x, y), (x + w, y + h), (0, 255, 0), 5)
    cropped = img2[y:y + h, x:x + w]
    file = open("text.txt", "a")
    
    text = pytesseract.image_to_string(cropped)
    
    file.write(text)
    file.write("\n")
    
    file.close()
