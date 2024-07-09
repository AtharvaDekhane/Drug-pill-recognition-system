import time
import cv2
path="/"
croped_images="croped_data/"
final_data="final_Data/"

def capture1(name):
        
        key = cv2. waitKey(1)
        webcam = cv2.VideoCapture(0)
        while True:
            try:
                check, frame = webcam.read()
        #print(check) #prints true as long as the webcam is running
        #print(frame) #prints matrix values of each framecd 
                cv2.imshow("Captured", frame)
                time.sleep(2)
        
                cv2.imwrite(filename=name+".jpg", img=frame)
                time.sleep(2)
                print("saved")
                webcam.release()
            
                cv2.waitKey()

                cv2.destroyAllWindows()
                im = Image.open(name+".jpg")
                im_new = crop_center(im, 300, 300)
                im_new.save(croped_images+name+".jpg", quality=95)
                time.sleep(2)
                clr_back(croped_images+name+".jpg")
                
            
                
                break
        
            except(KeyboardInterrupt):
                print("Turning off camera.")
                webcam.release()
                print("Camera off.")
                print("Program ended.")
                cv2.destroyAllWindows()
                break
from PIL import Image


def crop_center(pil_img, crop_width, crop_height):
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))

import numpy as np
from matplotlib import pyplot as plt
def clr_back(name):
    print(name)
    global filename_
    img = cv2.imread(name)
    mask = np.zeros(img.shape[:2], np.uint8)

    bgdModel = np.zeros((1, 65), np.float64)
    fgdModel = np.zeros((1, 65), np.float64)

    rect = (50, 50, 230, 230)
    cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
    img = img * mask2[:, :, np.newaxis]
    cv2.imwrite(name, img)
    
    #plt.imshow(img), plt.colorbar(), plt.show()


