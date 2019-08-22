# Opencv_Resize_Padding

## To Know How To Use Opencv , Os , Numpy , Matplotlib Resize and Pqdding


### Opnecv Read Image & Write Image

       cv2.imread(path)   # path = where your image paht // Example:'/User/home/image.jpg' 
       
       cv2.imwritee('new_name_of_picture(path+name)', Image) 

### Opnecv Resize

       cv2.resize(img, (width, hight), interpolation=cv2.INTER_CUBIC)
       

### Opnecv Padding

      cv2.copyMakeBorder( img , top , bottom , left , right , cv2.BORDER_CONSTANT , value=BLACK )
       

### Matplotlib Show Image

       plt.imshow(Image)
       

### Os

      os.path.isdir(path)
      #Make floder in path
      os.mkdir(path)
      #Show the list of path
      os.listdir(path)
      #Get name for file EX:image.jpg => image
      os.path.splitext(i)[0]
       
