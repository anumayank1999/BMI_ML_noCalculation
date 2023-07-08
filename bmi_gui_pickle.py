import pickle
from sklearn.ensemble import RandomForestClassifier
file=open('bmi.model','rb')
rfc=pickle.load(file)
from tkinter import *   #TKINTER IS LIBRARY CONTAINS GUI FILES
screen=Tk()             #WE MAKE A SCREEN VARIABLE HERE
#screen.geometry('200x300') #WE MAKE INTIAL SCREEN SIZE
screen.state('zoomed')  #HERE SCREEN IS SETTED TO FULL SCREEN VIEW
screen.configure(background='red')  #BACKGROUND OF SOFT GUI
text=Label(screen,text='BMI Calc',bg='yellow',font=('Algerian','25','bold'),fg='grey')  #LABEL CONSIST OF TEXT AND TEXT VARIOUS PARAMETERS
text.place(x=500 , y=200)   #TEXT FIELD PLACED VALUES/POSITION
text=Label(screen,text='HEIGHT IN M',bg='yellow',font=('Algerian','25','bold'),fg='grey')
text.place(x=200 , y=300)
text=Label(screen,text='WEIGHT IN KG',bg='yellow',font=('Algerian','25','bold'),fg='grey')
text.place(x=200 , y=400)
text=Label(screen,text='RESULT',bg='yellow',font=('Algerian','25','bold'),fg='grey')
text.place(x=200 , y=500)
h=Entry(screen,text='enter height',bg='black',font=('Algerian','15','italic'),fg='white') #INPUT SCREENAND ITS VARIOUS PARAMETERS
h.place(x=500 ,y=300)
w=Entry(screen,text='enter weight',bg='pink',font=('Algerian','15','italic'),fg='brown')
w.place(x=500 ,y=400)
r=Entry(screen,text='result',bg='white',font=('Algerian','15','italic'),fg='blue')
r.place(x=500 ,y=500)

def calc():
    r.delete(0,100)
    h1=h.get()  #I/P FROM TEXT DATA IS SENDED
    w1=w.get()
    t=rfc.predict([[h1,w1]])
    o=t[0]

    r.insert(0,o)
    if(o==0): #NOW ALL OTHER CONDITIONS
        c="underweight"
        
        
    if(o==1):
        c="-healthy"
        

    if(o==2):
        c="-overweight"
        

        
    if(o==3):
        c="-obese"
       

        
    if(o==4):
        c="-severly obese"
        

        
    if(o==5):
        c="-morbidy obese"
        
    r.insert(1,c)
       
       
    

press=Button(screen,text='clac',bg='green',font=('Algerian','20','bold'),fg='red',command=calc)    #BUTTON IS CREATED HERE AND ITS PARAMETERS AND WHERE FUNCTION IS TO BE SEND WHEN IT IS PRESSED IS TOLD HERE
press.place(x=500, y=600)
screen.mainloop() #TO HOLD THE O/P SCREEN  SO ALWAYS AT LAST