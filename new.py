import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv('colors.csv') #CSV file read
img=cv2.imread('download.jpeg') #image read my opencv
img = cv2.resize(img, (800,600)) #resizing a image
clicked=False
r=g=b=xpos=ypos=0
"get color name fuction is use for getting a color name by RGB values"
def get_color_name(R,G,B):
    minium=1000
    for i in range(len(df)):
        d=abs(R - int(df.iloc[i,3])) + abs(G - int(df.iloc[i,4])) + abs(B - int(df.iloc[i,5]))
        if d<=minium:
            minium=d
            cname=df.iloc[i,1]
    return str(cname)
"click function create for  getting pixle value and RGB"
def click(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global clicked,r,g,b,xpos,ypos
        clicked=True
        xpos=x
        ypos=x
        b,g,r=img[y,x]
        b=int(b)
        g=int(g)
        r=int(r)
        
cv2.namedWindow('image')
cv2.setMouseCallback('image',click)
#print(clicked,b,g,r,xpos,ypos)
while True:
    
    
    cv2.imshow('image',img)
    if clicked:
        cv2.rectangle(img,(20,20),(600 ,60),(b,g,r),-1) # putting rectangel on image
        text=get_color_name(r,g,b) +'R='+str(r)+'G='+str(g)+'B='+str(b)
        cv2.putText(img,text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA) # putting text on image
        if r+g+b>=600:
            cv2.putText(img,text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
    if cv2.waitKey(20)& 0xff==27:
        
        break
cv2.destroyAllWindows()
