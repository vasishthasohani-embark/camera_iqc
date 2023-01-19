#!/usr/bin/env python3

import cv2
import os
import subprocess
from pprint import pprint
import inquirer


class camera_iqc:


    def __init__(self):
        print('Starting Camera IQC testing now')
        print('Detecting video devices...')

        self.device_count()
        index = int(self.device_select()[-1])
        device = cv2.VideoCapture(index)
        a = camera_attributes
        a.serial_and_model(self,index)
        a.parameters(self,index,device)
        a.live_stream(self,device) 
               
    def device_count(self):
        #count the number of devices
        
        sub = subprocess.Popen('v4l2-ctl --list-devices',stdout=subprocess.PIPE, shell = True,universal_newlines=True,stderr=subprocess.STDOUT)
        blockdevs = [line.strip() for line in sub.stdout if 'video' in line]      
        return blockdevs
        
    
    def device_select(self):
        sub = subprocess.Popen('v4l2-ctl --list-devices',stdout=subprocess.PIPE, shell = True,universal_newlines=True,stderr=subprocess.STDOUT).communicate()[0]
        print(sub)
        list_devices = [inquirer.List(
                    "Video Devices selected",
                    message = "Select a device",
                    choices = self.device_count())]
        answers = inquirer.prompt(list_devices)
        selection = answers['Video Devices selected']
        return selection


class camera_attributes():
    

    def serial_and_model(self, index):

        attributes = ['ID_SERIAL' , 'ID_MODEL', 'ID_VENDOR' , 'ID_BUS','ID_USB_INTERFACES']
        display_attributes = ['Serial Number' , 'Camera Type','Vendor ID' , 'Bus ID' , 'Bus Interface ID']
        value = []
        for list in range(len(attributes)):
            p1 = subprocess.Popen('udevadm info --name=/dev/video{} | grep {}= | cut -d "=" -f 2'.format(index,attributes[list]),stdout=subprocess.PIPE, shell=True)
            (output1,err1) = p1.communicate()
            p1.status = p1.wait()
            response1 = output1.decode('utf-8')
            print('{} = {}'.format(display_attributes[list],response1),end = '')
    
    
    


    def parameters(self, index, device): #object from selecting the device
        
        
        #device = cv2.VideoCapture(index)
        w = device.get(cv2.CAP_PROP_FRAME_WIDTH)
        h = device.get(cv2.CAP_PROP_FRAME_HEIGHT)
        print("Image Resolution = " , w , "X" , h)

        fps= device.get(cv2.CAP_PROP_FPS)
        print("Frames per second = " , fps)

        #capture other camera qualities
        brightness = device.get(cv2.CAP_PROP_BRIGHTNESS)
        print("Brightness = ", brightness)

        contrast = device.get(cv2.CAP_PROP_CONTRAST)
        print("Contrast = ", contrast)

        saturation = device.get(cv2.CAP_PROP_SATURATION)
        print("Saturation = ", saturation)

        hue = device.get(cv2.CAP_PROP_HUE)
        print("Hue = ", hue)

        gain = device.get(cv2.CAP_PROP_GAIN)
        print("Gain = ", gain)

        exposure = device.get(cv2.CAP_PROP_EXPOSURE)
        print("Exposure = ", exposure)
    
    def live_stream(self,device):
        print(" Press q to end the live stream")
        while True:
            ret,frame = device.read()
           
            cv2.imshow('Live Stream',frame)
            if cv2.waitKey(1) & 0XFF == ord('q'):
               break;
        device.release()
        cv2.destroyAllWindows()

a = camera_iqc()





