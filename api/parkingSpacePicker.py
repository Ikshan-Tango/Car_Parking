import pickle
import cv2

def Main():

    try:
        with open('CarParkPos','rb') as f:
            posList = pickle.load(f)
    except:
        posList = []

    width , height = 107, 48

    def mouseClick(event,x,y,flags,params):

        #to add a square 
        if event == cv2.EVENT_LBUTTONDOWN:
            posList.append((x,y))

        #to remove a square
        if event == cv2.EVENT_RBUTTONDOWN:
            for i,pos in enumerate(posList):
                x1,y1 = pos
                if x1<x<x1+width and y1<y<y1+width:
                    posList.pop(i)
                    break
        
        with open('CarParkPos', 'wb') as f:
            pickle.dump(posList, f)

    while True:

        img = cv2.imread('carParkImg.png')

        # cv2.rectangle(img,(50,192),(157,240),(255,0,255),2) #this creates the box of purple color

        for pos in posList:
            cv2.rectangle(img,pos,(pos[0]+width,pos[1]+height),(255,0,255),2)

        # cv2.imshow("image",img)
        cv2.setMouseCallback("image", mouseClick)

        cv2.waitKey(1)