import cv2
import pickle
 
# width, height = 107, 48
 

 
def mouseClick(events, x, y, flags, params):
    posList = params.get('poslist')
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x, y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1, y1 = pos
            if x1 < x < x1 + params.get('w') and y1 < y < y1 + params.get('h'):
                posList.pop(i)
 
    with open(params.get('parking'), 'wb') as f:
        pickle.dump(posList, f)
 
def mouseClick(events, x, y, flags, params):
    global counter
    if events == cv2.EVENT_LBUTTONDOWN:
        
        circles[counter]= x,y
        counter =counter +1
        print('circles')
img = cv2.imread('static\uploads\WhatsApp_Image_2023-01-07_at_14.16.10.jpg')    
cv2.imshow("Original Image",img)   
cv2.setMouseCallback("Original Image", 'mousePoints')
cv2.waitKey(0)

def open_parking_image_window(pngimage='carParkImg.png',params={'parking':'hazratganj_1','w':107,'h':48}):
    try:
        with open(params.get('parking'), 'rb') as f:
            posList = pickle.load(f)
    except:
        posList = []
    
    while True:
        img = cv2.imread(pngimage)
        for pos in posList:
            cv2.rectangle(img, pos, (pos[0] + params.get('w'), pos[1] + params.get('h')), (255, 0, 255), 2)

   
        cv2.imshow("Image", img)
        params['poslist'] = posList
        cv2.setMouseCallback("Image", mouseClick, params)
        if cv2.waitKey(1) == 27:
            break
    cv2.destroyAllWindows()

if __name__ == "__main__":
    parking_img = 'carParkImg.png'
    parking='hazratganj_1'
    w = 107
    h = 48    
    open_parking_image_window(parking_img, params=dict(parking=parking,w=w, h=h ))
