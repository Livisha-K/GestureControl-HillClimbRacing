import cv2 as cv
from mediapipe import solutions
import pyautogui
import time

CAP = cv.VideoCapture(0)
hand = solutions.hands
hands = solutions.hands.Hands()
draw = solutions.drawing_utils

def find_command(results):
    for landmarks in results.multi_hand_landmarks:
        x9,y9,z9 = landmarks.landmark[9].x, landmarks.landmark[9].y, landmarks.landmark[9].z
        x12,y12,z12 = landmarks.landmark[12].x, landmarks.landmark[12].y, landmarks.landmark[12].z
        if abs(x9 - x12)+abs(y9 - y12)+abs(z9 - z12) < 0.10 :
            command = 2
        else:
            command = 1
        
        return command

def trace_hand(frame):
    results  = hands.process(frame)
    if results.multi_hand_landmarks:
        for landmarks in results.multi_hand_landmarks:
            draw.draw_landmarks(frame, landmarks, hand.HAND_CONNECTIONS)
        return (True,frame,find_command(results))
    else:
        return (False,0,0)
    
while True:
    success , frame = CAP.read()
    
    if success :
        # trace the hand
        frame = cv.flip(frame,1)
        rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        result,frame,command = trace_hand(rgb_frame)

        if result :
            mk_frame = frame
        else:
            mk_frame = rgb_frame

        print("command: " + str(command))
        if command == 1:
            pyautogui.keyUp('left')
            pyautogui.keyDown('right')
            
        elif command == 2:
            pyautogui.keyDown('left')
            pyautogui.keyUp('right')

        else:
            pyautogui.keyUp('right')
            pyautogui.keyUp('left')
        mk_frame = cv.cvtColor(mk_frame, cv.COLOR_RGB2BGR)
        cv.imshow("Ouput",mk_frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break