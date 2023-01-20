# IQC Scripts for Cameras
This repository contains IQC Scripts to test cameras. It is aimed to determine attributes/parameters of the video device connected: Serial No., Model ID, build ID, frame per second, Resolution, etc. More capabilities can be added to this script if required. 


1. Clone this repository.
2. Navigate to the cloned repository and open the terminal.
3. Run `chmod +x ./job.sh`
4. Run `./job.sh`  


# Device Setup

200, 300 and TTP trucks uses Cameras conected to the framegabber using the FAKRA cables. In order to test these cameras, following items are required :
1. Deserializer with power cord
2. USB Micro B to USB 3
3. FKRA cable 

Assemble the items as shown below. Connect the USB to a linux device and run the script.


![PXL_20230120_000809525(1)](https://user-images.githubusercontent.com/103149798/213590965-103d69a4-5227-411c-8efe-db5dd8c15bf8.jpg)
![PXL_20230120_000826453_2(1)](https://user-images.githubusercontent.com/103149798/213590955-42d93240-08bf-4377-999e-b67d021ab118.jpg)

#Result
Succesful running of this script should provide details of the selected device along with its streaming capabilities. A sample output should look like :

![Screenshot from 2023-01-19 16-32-27](https://user-images.githubusercontent.com/103149798/213592573-68a5a115-2d91-40a8-b1d1-5657e83ba030.png)
