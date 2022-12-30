    import cv2
    import numpy as np

    capture = cv2.VideoCapture(1)
    codec = cv2.VideoWriter_fourcc(*'XVID')
    output = cv2.VideoWriter('CAPTURE.avi', codec, 30, (640, 480))

    while True:
        ret, frame_temp = capture.read()
        cv2.imshow('FRAME', frame_temp)
        key=cv2.waitKey(1)
        if key%256 == 27:
            break
        elif key%256 == 32:
            output.write(frame_temp)

    capture.release()
    output.release()
    cv2.destroyAllWindows()