import cv2
cap = cv2.VideoCapture("video.mp4")
people_cascade = cv2.CascadeClassifier("Final_train.xml")
while True:
    ret, cuadros = cap.read()
    detected_people = people_cascade.detectMultiScale( cuadros, 1.1,1)
    for (x,y,z,h) in detected_people:
        cv2.rectangle(cuadros,(x,y),(x+z,y+h),(255,0,0),2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(cuadros, 'Tracking...', (x+6,y-6),font,0.5,(0,255,0),1)
        cv2.imshow('People Tracking', cuadros)
    if cv2.waitKey(33) == 13:
        break
cap.release()
cv2.destroyAllWindows()
