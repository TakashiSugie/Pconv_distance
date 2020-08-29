#画像のpsnr mse 部分的なpsnrを計測するライブラリ
#p_psnrの使い方は二枚の画像を入れ、計測したい部分が白、無視する部分を黒のマスクを入れること
import cv2
import numpy as np
import math
import glob
import os

def min_max(x, axis=None):
    min = x.min(axis=axis, keepdims=True)
    max = x.max(axis=axis, keepdims=True)
    result = (x-min)/(max-min)
    return result

def my_mkdir(path):
    if not os.path.isdir(path):
        os.makedirs(path)

def my_list(dir_name,sort=1,color=1,size=0):
    name_list = glob.glob(dir_name + '/*.png')
    img_list=[]
    print("hyahhhhhhaaaaaaaaa")
    if sort:
        name_list.sort()
    for name in name_list:
        print(name)
        img=cv2.imread(name,color)
        if size:
            img=cv2.resize(img,(size[0],size[1]))
        img_list.append(img)
    return img_list

def mse(img1,img2):
    mse=np.sum(np.square(img1-img2)/img1.shape[0]*img1.shape[2]*img.shape[3])
    return mse

def psnr(img1,img2):
    mse=np.sum(np.square(img1-img2)/img1.shape[0]*img1.shape[2]*img.shape[3])
    if not mse:
        print("same image")
        return 0
    else:
        psnr=10*math.log10(255*255/mse)
    return psnr

def p_psnr(img1,img2,mask):
    mask=mask/255
    deno=np.sum(mask)
    if mask.ndim==2:
        mask3=np.stack([mask,mask,mask],2)
    #print(mask3.shape)
    p_img1=img1*mask3
    p_img2=img2*mask3
    p_mse=np.sum(np.square(p_img1-p_img2)/(deno*3))
    if not p_mse:
        print("same image")
        return 0
    else:
        psnr=10*math.log10(255*255/p_mse)
    return psnr


if __name__ == '__main__':
    img1=cv2.imread("./data/pred/predict.png")
    img2=cv2.imread("./data/ori/psnr.png")
    mask=cv2.imread("./data/mask/mask2.png",0)
    psnr=p_psnr(img1,img2,mask)
    print(psnr)
