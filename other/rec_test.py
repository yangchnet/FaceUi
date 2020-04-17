import face_recognition
import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_alt2.xml')

cap = cv2.VideoCapture(0)
# i = 0
while (True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)   # 转化为灰度图
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

    for (x, y, w, h) in faces:
        print(x, y , w, h)
        roi_gray = gray[y: y+h, x:x+w]  # (ycord_start, ycord_end)
        roi_color = frame[y: y+h, x:x+w]
        img_item = 'unknown.png'
        cv2.imwrite(img_item, roi_gray)
        # print('write ', img_item)

        #compare
        known_image = face_recognition.load_image_file("lichang.jpg")
        unknown_image = face_recognition.load_image_file("unknown.png")

        biden_encoding = face_recognition.face_encodings(known_image)[0]
        unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

        results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
        print("results: ", results)

        # draw a rectangle
        color = (255, 0, 0) # BGR blue grenn red 0-255
        stroke = 2
        end_cord_x = x + w
        end_cord_y = y + h
        cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)
        # i += 1

    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()