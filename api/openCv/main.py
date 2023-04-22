import pickle
import cvzone
import cv2
import numpy as np

def CVLogic(sec):
    
    # Video feed
    # r'/home/ikshan/Ikshan/projects/Car_Parking/api/carPark.mp4'
    cap = cv2.VideoCapture("api/openCv/carPark.mp4")
    
    with open(r'/home/ikshan/Ikshan/projects/Car_Parking/api/openCv/CarParkPos', 'rb') as f:
        posList = pickle.load(f)
    
    width, height = 107, 48
    
    
    def checkParkingSpace(imgPro):
        spaceCounter = 0
    
        for pos in posList:
            x, y = pos
    
            imgCrop = imgPro[y:y + height, x:x + width]
            # cv2.imshow(str(x * y), imgCrop)
            count = cv2.countNonZero(imgCrop)
    
    
            if count < 900:
                color = (0, 255, 0)
                thickness = 5
                spaceCounter += 1
            else:
                color = (0, 0, 255)
                thickness = 2
    
            cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), color, thickness)
            cvzone.putTextRect(img, str(count), (x, y + height - 3), scale=1,
                            thickness=2, offset=0, colorR=color)
    
        cvzone.putTextRect(img, f'Free: {spaceCounter}/{len(posList)}', (100, 50), scale=3,
                            thickness=5, offset=20, colorR=(0,200,0))
        
        return spaceCounter
        #to return count of a parking space -> return spaceCounter

    while True:
        
        #keep the loop infintite
        
        if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        
        amount_of_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT) #679
        print(amount_of_frames)
        frame_number = (amount_of_frames/30)*sec
        #there are 679 frames in a 30 second video
        #therefore there are approx 22 frames in a second

        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number-1)

        success, img = cap.read()
        print("success = ",success)
        print(img)
        if img is None:
            print("Image is none")
            return "error: (-215:Assertion failed) !_src.empty() in function 'cvtColor"
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
        imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                            cv2.THRESH_BINARY_INV, 25, 16)
        imgMedian = cv2.medianBlur(imgThreshold, 5)
        kernel = np.ones((3, 3), np.uint8)
        imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)
    
        ans = checkParkingSpace(imgDilate)
        # cv2.imshow("Image", img)
        # cv2.imshow("ImageBlur", imgBlur)
        # cv2.imshow("ImageThres", imgMedian)
        # cv2.waitKey(10)
        return ans;
