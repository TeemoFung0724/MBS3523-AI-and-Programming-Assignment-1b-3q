import cv2

print(cv2.__version__)

x, y = 300, 200
dx, dy = 3, 2

capture = cv2.VideoCapture(0)
capture.set(3,640)
capture.set(4,480)

while True:
    success, frame = capture.read()

    cv2.putText(frame, 'MBS3523 Assignment 1b-Q3 Name: Fung Man Yuk', (20, 40), cv2. FONT_HERSHEY_SCRIPT_SIMPLEX, 0.75, (255,247,0), 2)
    cv2.rectangle(frame, (x, y), (x + 80, y + 80), (255, 255, 255), 2)

    x += dx
    y += dy

    if x >= 560 or x <= 0:
       dx *= -1
    if y >= 400 or y <= 0:
       dy *= -1

    cv2.imshow('MBS3523', frame)
    if cv2.waitKey(20) & 0xff == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()