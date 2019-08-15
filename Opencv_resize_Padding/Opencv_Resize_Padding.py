import cv2
import os
import matplotlib.pyplot as plt

path = '/Users/mio'                                    ## 圖片存放資料夾
re_path = path + '/Resize_image'                 ## 處理過圖片存放資料夾
re_height = 600                                         ## 填充後高度
re_width = 800                                          ## 填充後寬度
BLACK = [0,0,0]                                        ## 填充顏色設定RGB


if not os.path.isdir(re_path) :
    os.mkdir(re_path)

piclist = []  
file = os.listdir(path)
for pic_names in file :
    if pic_names.endswith(".jpg") or pic_names.endswith(".png") or pic_names.endswith(".JPG") :
        piclist.append( pic_names )

def img_resize(re_height , re_width , piclist , path) :
    for i in piclist :
        img = cv2.imread(path + '/' + i)
        if img.shape[0] > re_height and img.shape[1] > re_width : 
            img_resize = cv2.resize(img, (re_width, re_height), interpolation=cv2.INTER_CUBIC)
            try :
                cv2.imwrite( re_path + '/new_' + i + ' .jpg' ,  img_resize)
                print('complete')
            except :
                print(path + '/' + i)
        else :
            y = re_height - img.shape[0]
            x = re_width - img.shape[1]
            top , bottom = y//2 , y - (y//2)
            left , right = x//2 , x - (x//2)
            img_padding = cv2.copyMakeBorder( img , top , bottom , left , right , cv2.BORDER_CONSTANT , value=BLACK )
            try :
                cv2.imwrite(re_path + '/new_' + i + ' .jpg' , img_padding )
                print('complete')
            except :
                print(path + '/' + i)
            
if __name__ == "__main__" :
    img_resize(re_height , re_width , piclist , path)
