import cap as cap
import cv2
import time

import Detector as detector
import numpy as np
import HandTrackingModule as htm
import math
from ctypes import cast,POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities,IAudioEndpointVolume
wcam ,hcam= 640,480
while True:
    success,img=cap.read()
    img=detector.findHands(img)
    lmlist=detector.findPosition(img,draw=False)
    if len(lmlist)!=0:
        length=math.hypot(40-10,20-10)
        vol=np.interp(length,[50,300],[0,100])
        volBar=np.interp(length,[50,300],[400,150])
        volPer=np.interp(length,[50,300],[0,100])
        print(int(length),vol)
        vol.SetMasterVolumeLevel(vol,None)
        if length<50:
            cv2.circle(img, (100,100), 15, (0,255,0), cv2, cv2.FILLED)




