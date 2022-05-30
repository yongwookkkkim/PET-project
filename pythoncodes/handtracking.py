import cv2
import mediapipe as mp
import time

cap=cv2.VideoCapture(0)

mpHands=mp.solutions.hands
hands=mpHands.Hands()
#static_image_mode=False, .., min detection confidence=0.5, min tracking confidence=0.5 
mpDraw=mp.solutions.drawing_utils

while True:
    success, img=cap.read()
    imgRGB=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results=hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms)

    cv2.imshow("Image", img)
    cv2.waitKey(1)