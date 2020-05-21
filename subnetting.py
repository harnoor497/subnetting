from tkinter import *
import random
import sys
import tkinter.messagebox


def showclass():
    list1 = ['2','6','14','30','62','126','254','510','1022','2046','4094','8190','16382','32766','65534','131070','262142','524286','1048574','2097150','4194302','8388606','16777214'];
    list2 = ['2','6','14','30','62','126','254','510','1022','2046','4094','8190','16382','32766','65534']
    list3 = ['2','6','14','30','62','126','254']
    a=entry_1.get()
    b=[]
    b=a.split('.')
    c=int(b[0])
    if(c>=255):
        root.destroy()
        print("INVALID IP ADDRESS")
    if (c>=1 and c<=127):
        cl='A'
        label_2.configure(text='CLASS                          A')
        listshow=list1
        entry_3 = OptionMenu(root,tkvar,*listshow)
        entry_3.place(x=240,y=205)
    if (c>=128 and c<=191):
        cl='B'
        label_2.configure(text='CLASS                          B')
        listshow=list2
        entry_3 = OptionMenu(root,tkvar,*listshow)
        entry_3.place(x=240,y=205)
    
    if (c>=192 and c<=223):
        cl='C'
        label_2.configure(text='CLASS                          C')
        listshow=list3
        entry_3 = OptionMenu(root,tkvar,*listshow)
        entry_3.place(x=240,y=205)
    if (c>=224 and c<=255):
        if(c>=224 and c<=239):
            cl='D'
            print('Given IP belongs to class: ',cl)
            root.destroy()
        else:
            cl='E'
            print('Given IP belongs to class: ',cl)
            root.destroy()
        print('It doesnot have any subnet masking.')
def subnet():
    subnet=''
    z=0
    ip_add=entry_1.get()
    n=tkvar.get()
    no_comp=int(n)
    b=[]
    b=ip_add.split(".")
    c=int(b[0])
    if (c>=1 and c<=127):
        subnet='255.'*1
        z=254**3
        cl='A'
        
        if(no_comp>=65534):
            x=16777214-no_comp
            add=x//(256*256)
            output='255.'+str(add)+'.0.0'
            label_4.configure(text=output)
        elif(no_comp>=254):
            x=65534-no_comp
            add=x//256
            output='255.'*2+str(add)+'.0'
            label_4.configure(text=output)
        else:
            add=254-no_comp
            output='255.'*3+str(add)
            label_4.configure(text=output)      
    elif (c>=128 and c<=191):
        cl='B'
        label_2.configure(text='CLASS                          B')
        if(no_comp>254):
            x=65534-no_comp
            add=x//256
            output='255.'*2+str(add)+'.0'
            label_4.configure(text=output)
        else:
            add=254-no_comp
            output='255.'*3+str(add)
            label_4.configure(text=output)     
    elif (c>=192 and c<=223):
        cl='C'
        label_2.configure(text='CLASS                          C')
        add=254-no_comp
        output='255.'*3+str(add)
        label_4.configure(text=output)     

    elif (c>=224 and c<=255):
        if(c>=224 and c<=239):
            cl='D'
            label_2.configure(text='CLASS        D')
            label_4.configure(text="RESERVED IP")
        else:
            cl='E'
            label_2.configure(text='CLASS        E')
            label_4.configure(text="RESERVED IP")                  
    else:
        label_2.configure(text='INVALID CLASS')  
          
def iExit():
    iExit=tkinter.messagebox
    root.destroy()
        #return
root = Tk()
root.geometry('500x500')
root.title("SUBNET CALCULATOR")

label_0 = Label(root, text="SUBNET CALCULATOR",width=20,font=("bold", 20))
label_0.place(x=30,y=53)


label_1 = Label(root, text="ENTER THE IP ADDRESS",width=20,font=("bold", 10))
label_1.place(x=80,y=125)

entry_1 = Entry(root)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="CLASS",width=20,font=("bold", 10))
label_2.place(x=80,y=160)




label_3 = Label(root, text="HOSTS PER SUBNET ",width=20,font=("bold", 10))
label_3.place(x=80,y=205)
listd=[0]

tkvar=StringVar(root)
entry_3 = OptionMenu(root,tkvar,*listd)
entry_3.place(x=240,y=205)
Button(root,text='SHOW',width=20,bg='blue',fg='white',command=showclass).place(x=370,y=125)
Button(root,text='Exit',width=20,bg='blue',fg='white',command=iExit).place(x=180,y=420)
Button(root, text='Calculate',width=20,bg='blue',fg='white',command=subnet).place(x=180,y=380)

label_4 = Label(root, text="__________________",width=20,font=("bold", 10))
label_4.place(x=220,y=240)
label_5 = Label(root, text="SUBNET MASK",width=20,font=("bold", 10))
label_5.place(x=45,y=240)


root.mainloop()
