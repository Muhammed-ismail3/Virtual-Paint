import cv2
import numpy as np

frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

# List to store all drawn points: [x, y, colorId]
myPoints = [] 

# Define Drawing Colors in BGR format to match detected colors
myDrawingColors = [
    [255, 0, 0],  # Blue
    [0, 255, 0],  # Green
    [0, 0, 255]   # Red
]

def getContours(mask):
    """
    Finds contours in a mask, filters by area, and returns the
    top-center point (x, y) of the bounding box.
    Returns None if no valid object is found.
    """
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    
    for cnt in contours:
        area = cv2.contourArea(cnt)
        # Step 5: Filter contours using area threshold (adjust 400 as needed)
        if area > 400:
            
            # cv2.drawContours(frame, cnt, -1, (255, 0, 0), 3)
            
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            x, y, w, h = cv2.boundingRect(approx)
            
            # Return the "Logical Drawing Point"
            return (x + w // 2, y) 
            
    return None

def drawOnCanvas(myPoints, myDrawingColors):
 
    # Loops through stored points and draws them.
   
    for point in myPoints:
        # point = [x, y, colorId]
        cv2.circle(frame, (point[0], point[1]), 10, myDrawingColors[point[2]], cv2.FILLED)


while True:
    success, frame = cap.read()
    if not success:
        break
        
    frame = cv2.flip(frame, 1) # Mirror the frame so it feels more natural :)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    
    # 1. Blue Mask
    lower_blue = np.array([100, 100, 20])
    upper_blue = np.array([140, 255, 255])
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

    # 2. Green Mask
    lower_green = np.array([30, 110, 50])
    upper_green = np.array([50, 255, 255])
    mask_green = cv2.inRange(hsv, lower_green, upper_green)

    # 3. Red Mask (Merging your two red ranges)
    lower_red1 = np.array([0, 100, 100])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 100, 100])
    upper_red2 = np.array([180, 255, 255])
    mask_red1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask_red2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask_red = mask_red1 | mask_red2

    # Put masks in a list to loop through them easily
    # Order matches myDrawingColors: [Blue, Green, Red]
    masks = [mask_blue, mask_green, mask_red]

    # Process each color
    newPoints = []
    for i, mask in enumerate(masks):
        
        # Determine the drawing point for this specific color mask
        point = getContours(mask)
        
        if point:
            # Append new point (x, y, colorID)
            # We add it to `newPoints` first, then main list
            newPoints.append([point[0], point[1], i])

    # Add detected points from this frame to the persistent list
    if len(newPoints) != 0:
        for newP in newPoints:
            myPoints.append(newP)

    # Draw all points on the Virtual Canvas
    drawOnCanvas(myPoints, myDrawingColors)

    # Display result
    cv2.imshow("Virtual Painter", frame)

    k = cv2.waitKey(1) & 0xFF
    if k == 27: # Press 'ESC' to exit
        break

cap.release()
cv2.destroyAllWindows()