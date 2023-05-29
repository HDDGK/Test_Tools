import cv2 as cv
def take_a_photo():
    capture = cv.VideoCapture(0)
    print(capture)
    f, frame = capture.read()
    cv.imwrite('image.jpg', frame)
    capture.release()

def take_a_video():
    capture = cv.VideoCapture(0)
    if not capture.isOpened():
        print("打不开摄像头")
        exit()
    while True:
        ret,frame=capture.read()
        if not ret:
            break
        cv.imshow('frame',frame)
        if cv.waitKey(1)==ord('q'):
            break
    capture.release()
    cv.destroyAllWindows()
def show_a_video():
    cap=cv.VideoCapture('out.mp4')
    print("?")
    while cap.isOpened():
        ret ,frame=cap.read()
        if not ret:
            break
        cv.imshow('frame', frame)
        if cv.waitKey(1) == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()
    print("??")
def save_a_video():
    cap=cv.VideoCapture(0)
    fourcc=cv.VideoWriter_fourcc(*'mp4v')
    out=cv.VideoWriter('out.mp4',fourcc,20.0,(1080,720))
    while cap.isOpened():
        ret,frame=cap.read()
        if not ret:
            break
        frame=cv.flip(frame,1)
        out.write(frame)
        cv.imshow('frame',frame)
        if cv.waitKey(1)==ord('q'):
            break
    cap.release()
    out.release()
    cv.destroyAllWindows()
if __name__ == '__main__':
    # take_a_photo()
    # take_a_video()

    save_a_video()
    # show_a_video()