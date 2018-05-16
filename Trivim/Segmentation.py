from PIL import Image
import os
import numpy as np
import shutil


def crop_image(image,mask,database,filename,main_directory):
    pic_name=filename[:filename.find("_")]
    #pic_name=filename
    #print "pic_name ",pic_name
    print "main_directory", main_directory
    print "current directory", os.getcwd()
    home=os.getcwd()
    path= os.path.normpath(os.getcwd() + os.sep + os.pardir)
    #index = len(path)-1
    os.chdir(path)
    print "new current directory", os.getcwd()
    ds=os.listdir(path)
    for i in ds:
        if i.endswith(".kml"):
            oldname=i
    print "oldname", oldname
    newname=pic_name+".kml"
    print "newname", newname
    os.rename(oldname,newname)
    print "sucessfully renamed"
    os.chdir(home)
    cropBox = (mask[0],mask[1],mask[2],mask[3])
    print image
    image1=Image.open(image)
    image1.load()
    image_data1=np.asarray(image1)
    print "Image array is", image_data1
    print "Crop Box is ", cropBox
    image_data_new = image_data1[int(cropBox[0]):int(cropBox[1]), int(cropBox[2]):int(cropBox[3]),:]
    new_image = Image.fromarray(image_data_new)
    if os.path.isdir(main_directory+"\\"+pic_name) == True:
        print main_directory+"\\"+pic_name
        dst=main_directory+"\\"+pic_name
        print filename
        new_image.save(dst+"\\"+filename+".jpg")
        shutil.copy(database,dst+"\\"+filename+".txt")
        print "save"
    else:
        os.mkdir(main_directory+"\\"+pic_name)
        dst=main_directory+"\\"+pic_name
        print filename
        new_image.save(dst+"\\"+filename+".jpg")
        shutil.copy(database,dst+"\\"+filename+".txt")
        print "new building save"
    
    
##crop_image("C://Trivim2.0//DSC01008.JPG",[1000,10000,1000,10000],"build1_1","C://Trivim2.0//segmentation test")
