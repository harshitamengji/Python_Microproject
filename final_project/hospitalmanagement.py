from tkinter import *
from tkinter import messagebox
import random
root=Tk()
root.title("billing system")
root.geometry('1280x720')
bg_color='pink'

#======================variable=================
c_name=StringVar()
c_phone=StringVar()
ref_dr=StringVar()
item=StringVar()
Rate=IntVar()
quantity=IntVar()
bill_no=StringVar()
x=random.randint(1000,9999)
bill_no.set(str(x))

global l
l=[]

#=========================Functions================================

def additm():
    n=Rate.get()
    m=quantity.get()*n
    l.append(m)
    if item.get()!='':
        textarea.insert((10.0+float(len(l)-1)), f"{item.get()}\t\t{quantity.get()}\t\t{ m}\n")
    else:
        messagebox.showerror('Error','Please enter item')


def gbill():
    if c_name.get() == "" or c_phone.get() == "":
        messagebox.showerror("Error", "Customer detail are must")
    else:
        textAreaText = textarea.get(10.0,(10.0+float(len(l))))
        welcome()
        textarea.insert(END, textAreaText)
        textarea.insert(END, f"\n=======================================")
        textarea.insert(END, f"\nTotal Paybill Amount :\t\t      {sum(l)}")
        textarea.insert(END, f"\n=======================================")
        textarea.insert(END, f"\n\n*********************THANK YOU!!********************")
        save_bill()



def clear():
    c_name.set('')
    c_phone.set('')
    ref_dr.set('')
    item.set('')
    Rate.set(0)
    quantity.set(0)
    welcome()
def exit():
    op = messagebox.askyesno("Exit", "Do you really want to exit?")
    if op > 0:
        root.destroy()
def save_bill():
    op=messagebox.askyesno("Save bill","Do you want t o save the Bill?")
    if op>0:
        bill_details=textarea.get('1.0',END)
        f1=open("bills/"+str(bill_no.get())+".txt","w")
        f1.write(bill_details)
        f1.close()
        messagebox.showinfo("Saved",f"Bill no, :{bill_no.get()} Saved Successfully")
    else:
        return
def welcome():
    textarea.delete(1.0,END)
    textarea.insert(END,"\t  Welcome to Billing Section")
    textarea.insert(END,f"\n\nBill Number:\t\t{bill_no.get()}")
    textarea.insert(END,f"\nCustomer Name:\t\t{c_name.get()}")
    textarea.insert(END,f"\nPhone Number:\t\t{c_phone.get()}")
    textarea.insert(END,f"\nReference Dr:\t\t{ref_dr.get()}")

    textarea.insert(END,f"\n\n-----------------------------------------------------------------")
    textarea.insert(END,"\nProduct\t\tQTY\t\tPrice")
    textarea.insert(END,f"\n-----------------------------------------------------------------\n")

    textarea.configure(font='arial 15 bold')



title=Label(root,pady=2,text="+CLINIC BILLING SYSTEM+",bd=12,bg=bg_color,fg='green',font=('times new roman', 25 ,'bold'),justify=CENTER)
title.pack(fill=X)

#=================Product Frames=================
F1=LabelFrame(root,text='Patient Details',font=('times new romon',15,'bold'),fg='black')
F1.place(x=0,y=80,relwidth=1)

cname_lbl=Label(F1,text='Patient Name',font=('times new romon',18,'bold'),bg='white',fg='black').grid(row=0,column=0,padx=20,pady=5)
cname_txt=Entry(F1,width=15,textvariable=c_name,font='arial 15 bold').grid(row=0,column=1,padx=10,pady=5)

cphone_lbl=Label(F1,text='Phone No. ',font=('times new romon',18,'bold'),bg='white',fg='black').grid(row=0,column=2,padx=20,pady=5)
cphone_txt=Entry(F1,width=15,font='arial 15 bold',textvariable=c_phone).grid(row=0,column=3,padx=10,pady=5)

refDR_lbl=Label(F1,text='Refrence DR. ',font=('times new romon',18,'bold'),bg='white',fg='black').grid(row=0,column=4,padx=20,pady=5)
refDR_txt=Entry(F1,width=15,font='arial 15 bold',textvariable=ref_dr).grid(row=0,column=5,padx=10,pady=5)


F2 = LabelFrame(root, text='Item Details', font=('times new romon', 18, 'bold'), fg='black',bg='white')
F2.place(x=20, y=180,width=630,height=500)

itm= Label(F2, text='Item Name', font=('times new romon',18, 'bold'), bg='white', fg='black').grid(
row=0, column=0, padx=30, pady=20)
itm_txt = Entry(F2, width=20,textvariable=item, font='arial 15 bold').grid(row=0, column=1, padx=10,pady=20)

rate= Label(F2, text='Item Price', font=('times new romon',18, 'bold'), bg='white', fg='black').grid(
row=1, column=0, padx=30, pady=20)
rate_txt = Entry(F2, width=20,textvariable=Rate, font='arial 15 bold').grid(row=1, column=1, padx=10,pady=20)

n= Label(F2, text='Item Quantity', font=('times new romon',18, 'bold'), bg='white', fg='black').grid(
row=2, column=0, padx=30, pady=20)
n_txt = Entry(F2, width=20,textvariable=quantity, font='arial 15 bold',).grid(row=2, column=1, padx=10,pady=20)

#========================Bill area================
F3=Frame(root)
F3.place(x=700,y=180,width=500,height=500)

bill_title=Label(F3,text='Bill Section',font='arial 15 bold',fg='green').pack(fill=X)
scrol_y=Scrollbar(F3,orient=VERTICAL)
textarea=Text(F3,yscrollcommand=scrol_y)
scrol_y.pack(side=RIGHT,fill=Y)
scrol_y.config(command=textarea.yview)
textarea.pack()
welcome()
#=========================Buttons======================
btn1=Button(F2,text='Add item',font='arial 15 bold',fg='green',command=additm,padx=5,pady=10,bg='pink',width=15)
btn1.grid(row=3,column=0,padx=10,pady=30)
btn2=Button(F2,text='Generate Bill',font='arial 15 bold',fg='green',command=gbill,padx=5,pady=10,bg='pink',width=15)
btn2.grid(row=3,column=1,padx=10,pady=30)
btn3=Button(F2,text='Clear',font='arial 15 bold',fg='green',padx=5,pady=10,command=clear,bg='pink',width=15)
btn3.grid(row=4,column=0,padx=10,pady=30)
btn4=Button(F2,text='Exit',font='arial 15 bold',fg='green',padx=5,pady=10,command=exit,bg='pink',width=15)
btn4.grid(row=4,column=1,padx=10,pady=30)

root.mainloop()