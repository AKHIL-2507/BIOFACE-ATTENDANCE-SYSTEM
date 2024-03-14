import streamlit as st
from sklearn.neighbors import KNeighborsClassifier
import cv2
import os
import joblib
import pandas as pd
from datetime import datetime
from datetime import date
import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def app():
    emaillist=[]
    st.header("ADD YOUR ATTENDANCE")
    if st.button("TAKE ATTENDANCE"):
        datetoday2= datetime.today().strftime("%d-%m-%Y")

        cap = cv2.VideoCapture(0)
        face_detector=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        model = joblib.load('stati/face_recognition.pkl')
        ret = True
        i=0
        nimgs=10
        while True:
            ret,frame=cap.read()
            face=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            face = face_detector.detectMultiScale(face,1.2,5,minSize=(20,20))
            for (x, y, w, h) in face:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 20), 2)
                
                face = cv2.resize(frame[y:y+h, x:x+w], (50, 50))
                identified_person =face.reshape(1,-1)
                print(identified_person)
                print(model.predict(identified_person))
                details=model.predict(identified_person)
                for i in details:

                    cv2.putText(frame,f'{i}', (30, 30),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 20), 2, cv2.LINE_AA)
                    username= i.split('_')[0]
                    userid = i.split('_')[1]
                    current_time = datetime.now().strftime("%I:%M:%S")
                    path="Emaildetail/"
                    
                    for j in os.listdir(path):
                        #print(i)
                        gmail=j.split('_')[1]
                        if gmail == userid:
                            
                            Email=j.split('_')[0]
                            findmail=j
                    print(Email)
                    emaillist.append(Email)
                    print(emaillist)
                    joblib.dump(emaillist,"stati\email.pkl")
                    df = pd.read_csv(f'Attendanc/Attendanc-{datetoday2}.csv')
                    if username not in list(df['name']):
                        print(userid)
                        print(username)
                        
                        with open(f'Attendanc/Attendanc-{datetoday2}.csv', 'a') as f:
                            f.write(f'\n{username},{userid},{current_time},{Email}')
                    ''' datetoday2= datetime.today().strftime("%d-%m-%Y")
                        emailsender="akhilking25007@gmail.com"
                        password="zoyf ftay gnoo rtvh"
                        subject="Status report"
                        #mailto="akhilbabu250007@gmail.com"
                        with open(f'Attendanc/Attendanc-{datetoday2}.csv','r') as f:
                                reader=csv.reader(f)
                                print(reader)
                                for line in reader:
                                    if line[3] == Email:
                                        if line[3] not in reader:

                                    
                                            text=f"Hello mam/sir we are from KG COLLEGE OF ARTS AND SCIENCE your son/daughter {line[0]} reached our college campus on {datetoday2} at {line[2]}"
                                            #print(text)
                                            email_send =line[3]
                                            msg  =MIMEMultipart()
                                            msg['From'] = emailsender
                                            msg['To'] =email_send
                                            msg['subject']=subject
                                            msg.attach(MIMEText(text,"plain"))
                                            text = msg.as_string()
                                            with smtplib.SMTP_SSL("smtp.gmail.com",465) as server:
                                                    print("hello")
                                                    server.ehlo()
                                                    #server.starttls()
                                                    server.login(emailsender,password)
                                                    server.sendmail(emailsender,email_send,text)
                                                    server.quit()'''
            cv2.imshow("adding new image",frame)
            if cv2.waitKey(1) == 27:
                break

        cap.release()
        cv2.destroyAllWindows()
    if st.button("Email"):
        emaillist=joblib.load("stati\email.pkl")
        print(emaillist)
        for name in set(emaillist):
            datetoday2= datetime.today().strftime("%d-%m-%Y")
            emailsender="akhilking25007@gmail.com"
            password="zoyf ftay gnoo rtvh"
            subject="Status report"
            #mailto="akhilbabu250007@gmail.com"
            with open(f'Attendanc/Attendanc-{datetoday2}.csv','r') as f:
                    reader=csv.reader(f)
                    print(reader)
                    for line in reader:
                        if line[3] == name:
                            if line[3] not in reader:

                        
                                text=f"Hello mam/sir we are from KG COLLEGE OF ARTS AND SCIENCE your son/daughter {line[0]} reached our college campus on {datetoday2} at {line[2]}"
                                #print(text)
                                email_send =line[3]
                                msg  =MIMEMultipart()
                                msg['From'] = emailsender
                                msg['To'] =email_send
                                msg['subject']=subject
                                msg.attach(MIMEText(text,"plain"))
                                text = msg.as_string()
                                with smtplib.SMTP_SSL("smtp.gmail.com",465) as server:
                                        print("hello")
                                        server.ehlo()
                                        #server.starttls()
                                        server.login(emailsender,password)
                                        server.sendmail(emailsender,email_send,text)
                                        server.quit()
                                        st.info("EMAIL SENT")
        if os.path.isdir('stati/email.pkl'):
             os.removedirs('stati/email.pkl')

                        




