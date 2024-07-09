import os
import shutil
global filename_
import cv2
import edge_detection
from matplotlib import pyplot as plt
import numpy as np

img_name="14.jpg"
def find_edge():
    global filename_
    edge_detection.edge_detection(img_name)

def clr_back():

    global filename_
    img = cv2.imread("croped.jpg")
    mask = np.zeros(img.shape[:2], np.uint8)

    bgdModel = np.zeros((1, 65), np.float64)
    fgdModel = np.zeros((1, 65), np.float64)

    rect = (50, 50, 450, 290)
    cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
    img = img * mask2[:, :, np.newaxis]
    cv2.imwrite("removed.jpg", img)
    plt.imshow(img), plt.colorbar(), plt.show()

def histogram():
        global filename_
        im = Image.open(filename_).convert('L')
        #Display image
        #im.show()
        print("The image content are as follow:\n")
        ss=im.histogram()
        print (ss);
        #Applying a filter to the image
##        im_sharp = im.filter( ImageFilter.SHARPEN )
##        #Saving the filtered image to a new file
##        im_sharp.save( '"croped.jpg"', 'JPEG' )
##        #im.show()
##        im.save('sharp.jpg','png')
def data0():
    p=0
    import cv2
    import os
    import glob
   
  

    
    img_dir = "croped_data/"  # Enter Directory of all images
    data_path = os.path.join(img_dir, '*g')
    files = glob.glob(data_path)
    data = []
    for f1 in files:
 #36422830_55c844bc2d       
        img = cv2.imread(f1)
        data.append(img)
    final=[]
    img_names=[]
    
    for i in range(len(data)):
        original = cv2.imread(files[i])
        print(i)
        #print(files[i])
        image_to_compare = cv2.imread(img_name)
        if original.shape == image_to_compare.shape:
           # print("The images have same size and channels")
            difference = cv2.subtract(original, image_to_compare)
            b, g, r = cv2.split(difference)

            if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
                #print("The images are completely Equal")
                p+=1
                
            
            else:
                #print("The images are NOT equal")
                p+=1
                

        
        sift = cv2.xfeatures2d.SIFT_create()
        kp_1, desc_1 = sift.detectAndCompute(original, None)
        kp_2, desc_2 = sift.detectAndCompute(image_to_compare, None)

        index_params = dict(algorithm=0, trees=5)
        search_params = dict()
        flann = cv2.FlannBasedMatcher(index_params, search_params)

        matches = flann.knnMatch(desc_1, desc_2, k=2)

        good_points = []
        for m, n in matches:
            if m.distance < 0.6 * n.distance:
                good_points.append(m)

        # Define how similar they are
        number_keypoints = 0
        if len(kp_1) <= len(kp_2):
            number_keypoints = len(kp_1)
        else:
            number_keypoints = len(kp_2)

        #print("Keypoints 1ST Image: " + str(len(kp_1)))
        #print("Keypoints 2ND Image: " + str(len(kp_2)))
        n1=int(len(kp_1))
        n2=int(len(kp_2))

        percentage=len(good_points) #* 100/ number_keypoints
        final.append(percentage)
        img_names.append(str(files[i]))
        result = cv2.drawMatches(original, kp_1, image_to_compare, kp_2, good_points, None)
        #print(good_points)

        #cv2.imwrite("result/feature_matching."+str(i)+".jpg", result)
        cv2.imshow("result", cv2.resize(result, None, fx=1, fy=1))
        cv2.waitKey(1000)

    #import numpy as np
    val=max(final)
    
    ind=0
    
    print (final,val)
    
    
    ind = final.index(val)

    ss=img_names[ind][12:]
    print(ss)
    return ss
    #search_string_in_file(img_names[ind])

##data0()
##find_edge()
##clr_back()
from PIL import Image

import pytesseract
def text_extraction():
    text = pytesseract.image_to_string(Image.open(img_name))
    print(text)
        

def ocr_core():
    """
    This function will handle the core OCR processing of images.
    """
    text = pytesseract.image_to_string(Image.open(img_name))  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text

#print(ocr_core('images/ocr_example_1.png'))
def clr_back():

    global filename_
    img = cv2.imread("croped.jpg")
    mask = np.zeros(img.shape[:2], np.uint8)

    bgdModel = np.zeros((1, 65), np.float64)
    fgdModel = np.zeros((1, 65), np.float64)

    rect = (50, 50, 230, 230)
    cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
    img = img * mask2[:, :, np.newaxis]
    cv2.imwrite("removed.jpg", img)
    plt.imshow(img), plt.colorbar(), plt.show()

#clr_back()


