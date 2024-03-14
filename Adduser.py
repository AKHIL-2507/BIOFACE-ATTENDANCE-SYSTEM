import cv2
#import pandas
import numpy as np
from datetime import datetime
from sklearn.neighbors import KNeighborsClassifier
import os
import joblib
import streamlit as st
from streamlit_option_menu import option_menu

#datetime
date= datetime.today().strftime("%d-%m-%Y")
# creating the folders

#no of images to be taken 
nimgs=50
def app():
    #add user details and train the images
    st.title('BIOFACE ATTENDANCE SYSTEM')
    Name = st.text_input('Name')
    userid = st.text_input("USER_ID")
    emailid= st.text_input('EMAIL')
    print(f"{str(emailid)}fdsfds")
    #st.markdown("", unsafe_allow_html=True)
    if  not os.path.isdir('stati'):
        os.makedirs('stati')
    if  not os.path.isdir(r'stati\face'):
        os.makedirs(r'stati\face')

    if not os.path.isdir('Emaildetail'):
        os.makedirs('Emaildetail')
    if not os.path.isdir(r"Attendanc"):
        os.makedirs(r"Attendanc")
    if not os.path.isdir(f"Attendanc\Attendanc-{date}.csv"):
        with open (f"Attendanc\Attendanc-{date}.csv","w") as f:
            f.write("name,userid,time,email")
    face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    facefolder="stati/face/"
    emailfolder="Emaildetail/"
    if st.button('ADD USER'):
        if not os.path.isdir(facefolder+Name+"_"+str(userid)):
            os.makedirs(facefolder+Name+"_"+str(userid))
        if not os.path.isdir(emailfolder+emailid+"_"+str(userid)):
            os.makedirs(emailfolder+emailid+"_"+str(userid))   
        cap=cv2.VideoCapture(0)
        i=0
        j=0
        while True:
            ret,frame=cap.read()
            face=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            face = face_detector.detectMultiScale(face,1.2,5,minSize=(20,20))
            for (x, y, w, h) in face:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 20), 2)
                cv2.putText(frame, f'Images Captured: {i}/{nimgs}', (30, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 20), 2, cv2.LINE_AA)
                if j % 5==0:
                    cv2.imwrite(f"stati/face/{Name}_{str(userid)}/{Name}_{i}.jpg",frame[y:y+h, x:x+w] )
                    i+=1
                j+=1
            if j == nimgs * 5:
                break
            cv2.imshow("adding new image",frame)
            if cv2.waitKey(1)==27:
                break
        cap.release()
        cv2.destroyAllWindows()
    # To train the images
    if st.button("TRAIN MODEL"):
        knn = KNeighborsClassifier(n_neighbors=5)
        faces=[]
        label=[]
        facefolders="stati/face"
        for user in os.listdir(facefolders):
            for i in os.listdir(f"stati/face/{user}"):
                img=cv2.imread(f"stati/face/{user}/{i}")
                img=cv2.resize(img,(50,50))
                faces.append(img.ravel())
                label.append(user)
        faces=np.array(faces)
        knn.fit(faces,label)
        joblib.dump(knn,"stati/face_recognition.pkl")
        st.info("Model Trained Successfully")
    