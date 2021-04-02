import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#video = cv2.VideoCapture(0) live video

video = cv2.VideoCapture('pewpew.mp4')

while True:
	_, img = video.read()
	grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	face_detect = face_cascade.detectMultiScale(grayscale)
	for (x, y, w, h) in face_detect:
		cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
	cv2.imshow('img', img)
	k = cv2.waitKey(30) & 0xff
	if k==27:
		break
video.release()