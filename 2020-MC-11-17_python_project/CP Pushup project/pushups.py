import cv2
import mediapipe as mp
import numpy as np
from pushupModule import poseDetector

def Run(name):
    cap = cv2.VideoCapture(name)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1200)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    detector = poseDetector() # object
    count = 0
    
    direction = 0
    form = 0
    feedback = "Fix Form"

    while cap.isOpened():
        ret, img = cap.read()
        #Determine dimensions of video - Help with creation of box
        img = cv2.resize(img,(int(1200),int(720)))
        img = detector.findPose(img, False)  # obj class
        lmList = detector.findPosition(img, False)
        
        if len(lmList) != 0: #land mark list
            elbow = detector.findAngle(img, 11, 13, 15)
            #elbow = detector.findAngle(img, 12, 14, 16)
            shoulder = detector.findAngle(img, 13, 11, 23)
            hip = detector.findAngle(img, 11, 23,25)
            
            #Percentage of success of pushup
            per = np.interp(elbow, (90, 170), (0, 100))
        
            #Bar to show Pushup progress
            bar = np.interp(elbow, (90, 170), (710, 10))
            
            #Check to ensure right form before starting the program
            if elbow > 160 :
                form = 1
        
            #Check for full range of motion for the pushup
            if form == 1:# direction.
                if per == 0:
                    if elbow <= 90 :
                        feedback = "Up"
                        if direction == 0:
                            count += 0.5 # yahn tak dir=0 us k bad khud ma ny dir=1 ty k push up pora kr sakon
                            direction = 1
                    else:
                        feedback = "Fix Form"
                        
                if per == 100:
                    if elbow > 160:
                        feedback = "Down"
                        if direction == 1:
                            count += 0.5
                            direction = 0
                    else:
                        feedback = "Fix Form"
                            # form = 0
                    
            #Draw Bar
            cv2.rectangle(img, (1175, 10), (1195, 710), (115, 240, 240), 3)  #  OUTERBAR SHOWN ON SCREEN 
            if form == 1:
                cv2.rectangle(img, (1175, int(bar)), (1195, 710), (115, 240, 240), cv2.FILLED)#INNER BAR SHOWN
                cv2.putText(img, f'Percentage {int(per)}%', (880, 350), cv2.FONT_HERSHEY_PLAIN, 2,
                            (115, 240, 240), 2)


            #Pushup counter
            cv2.rectangle(img, (400, 0), (800, 90), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, "Counter: "+str(int(count)), (460, 80), cv2.FONT_HERSHEY_PLAIN, 3,
                        (255, 0, 0), 3)
            #Feedback 
            cv2.putText(img, "Status: "+feedback, (500, 35 ), cv2.FONT_HERSHEY_PLAIN, 2,
                        (255, 0, 0), 2)
            cv2.putText(img, "Press Q to Quit", (0, 710 ), cv2.FONT_HERSHEY_PLAIN, 2,
                        (0, 255, 255), 2)

        cv2.imshow('Pushup counter',img)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
        if cv2.waitKey(10) & 0xFF == ord('Q'):
            break
            
    cap.release()
    cv2.destroyAllWindows()