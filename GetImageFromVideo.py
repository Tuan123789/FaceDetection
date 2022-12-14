import cv2
import time

def main():
    cap = cv2.VideoCapture('../video/BanThien.mp4')
    # Resolution 640*480
    time.sleep(1)
    if cap is None or not cap.isOpened():
        print('Khong the mo file video')
        return
    cv2.namedWindow('Image', cv2.WINDOW_AUTOSIZE)
    n = 1
    dem = 1
    while True:
        [success, img] = cap.read()
        ch = cv2.waitKey(30)
        if success:
            #img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
            imgROI = img[90:(90+480),:] # Tao ra anh 480x480

            imgROI = cv2.resize(imgROI,(250,250))
            cv2.imshow('Image', imgROI)
        else:
            break
        if n%4 == 0:
            filename = '../image_bt/BanThien/BanThien_%04d.bmp'%(dem)
            cv2.imwrite(filename,imgROI)
            dem = dem + 1
        n = n + 1
    return

if __name__ == "__main__":
    main()
