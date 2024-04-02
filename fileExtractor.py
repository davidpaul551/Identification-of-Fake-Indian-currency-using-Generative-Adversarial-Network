import cv2
import numpy as np
import matplotlib.pyplot as plt
import os 

# get all files from directory
def getFilesList(root):
    listOfFiles = []
    listOfFolder = os.listdir(root)
    for folder in listOfFolder:
        if not folder.endswith('jpg'):
            listOfFiles.extend(os.listdir(root + '/'+folder))
    return listOfFiles

root = 'F:/Fake_Currency_OLD/Image_Processing/projects/0_MiniProject_Test/0010.jpg'


print(next(os.walk(root))[2])