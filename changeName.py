import os 
import shutil
#import subprocess

path = "C:/Users/"
usb_path = "E:/"
folder_ls = os.listdir(path)

###gets list of files renames to first 6 digits after "NET0000-CELL-" and adds extension accordingly
for i in folder_ls:
    
    if len(i) > 10:
        short_ci = (i.split("-")[2][:6])
        
        extension = i.split(".")[-1]
        if extension == "cfg":
            new_extension = "da0"
            new_file = f"{short_ci}.{new_extension}"
            
            os.rename(path+i, f"{path}{new_file}")
            path_shutil = path + new_file
            #command to move new shorter file name from folder to usb disk E:
            shutil.move(path_shutil, usb_path)
        elif extension == "txt":
            new_file = f"{short_ci}.{extension}"
            
            os.rename(path+i, f"{path}{new_file}")
            path_shutil = path + new_file
            #command to move new shorter file name from folder to usb disk E:
            shutil.move(path_shutil, usb_path)
            

        

        
   
