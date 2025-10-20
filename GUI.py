from tkinter import *
import tkinter
import re
from tkinter import messagebox,filedialog,font
from PIL import ImageTk,Image
import sqlite3
# root=Tk()
# text=Label(root,text="Hello World")

# text.pack()

# root.mainloop()

# root= Tk()
# Label1=Label(root,text="Hello World").grid(row=0,column=0)
# Label2=Label(root,text="My name is Menna").grid(row=0,column=1)
# root.mainloop()



# root=Tk()

# e=Entry(root,width=50,borderwidth=5)

# e.pack()
# e.insert(11,"Your name")

# def onclick():
#     name=e.get()
#     label=Label(root,text="Hello " + name)
#     label.pack()

# button=Button(root,text="Enter your name",command=onclick,fg="blue",bg="white")
# button.pack()

# root.mainloop()


#Simple Calculator

# root=Tk()
# root.title("Simple Calculator")
# e=Entry(root)

# e.grid(row=0,column=0,columnspan=3,padx=10,pady=10,sticky="we")

# def convert_to_int(n):
#     try :
#         x=int(n)
#     except:
#         e.insert(0,"ERROR")
#         raise ValueError
#     return x
    

# def onclick(number):
    
#     current=e.get()
#     if number =="Clear":
#         e.delete(0,END)
#         return
#     if number == 'del':
#         e.delete(len(current)-1,END)
#         return
#     elif number=="=":
        
#         e.delete(0,END)
#         eq=re.split(r'(?=[+-/*])|(?<=[+-/*])',current)
#         res=int(eq[0])
#         for i in range(len(eq)-1):
#             print(eq)
            
#             if eq[i]=='+':
#                 res=res+convert_to_int(eq[i+1])
                
#             elif eq[i]=='-':
#                 res=res-convert_to_int(eq[i+1])

#             elif eq[i]=='*':
#                 res=res*convert_to_int(eq[i+1])

#             elif eq[i]=='/':
#                 try:
#                     res=round(res/convert_to_int(eq[i+1]),5)
#                 except:
#                     e.insert(0,"ERROR")
#                     raise ZeroDivisionError
                
        
#         e.insert(0,res)

#         return
#     else:
#         e.delete(0,END)
#         e.insert(0,str(current)+str(number))
        
  

    


# def create_button(number):

#     return  Button(root,text=number,padx=40,pady=20,command=lambda:onclick(number)) 

# numbers=[str(i) for i in range(10)]

# r=1
# c=0
# for n in numbers:    
#     button=create_button(n)
#     button.grid(row=r,column=c,padx=5)
#     c+=1
#     if c%3==0:
#         r+=1
#         c=0
# clear_button = create_button("Clear")
# add_button=create_button("+")
# sub_button=create_button('-')
# mul_button=create_button('*')
# div_button=create_button("/")
# equal_button=create_button("=")
# del_button=create_button('del')

# clear_button.grid(row=5, column=1, columnspan=2, sticky="we",padx=5,pady=5)
# add_button.grid(row=5,column=0)
# sub_button.grid(row=4,column=1)
# mul_button.grid(row=6,column=0)
# div_button.grid(row=6,column=1)
# equal_button.grid(row=4,column=2,padx=5)
# del_button.grid(row=6,column=2)


# exit_button=Button(root,text="Exit",command=root.quit,borderwidth=10)
# exit_button.grid(row=7,column=0,columnspan=3,sticky="we",pady=10)
# root.bind("<Key>", lambda event: onclick(event.char))
# root.mainloop()


########### IMAGE VIEWER ##################
# root=Tk()
# root.title("IMage Viewer APP")

# my_image1=ImageTk.PhotoImage(Image.open("my_pic.jpg").resize((400,400)))
# my_image2=ImageTk.PhotoImage(Image.open("Menna Waleed.jpg").resize((400,400)))
# my_image3=ImageTk.PhotoImage(Image.open("pic.jpg").resize((400,400)))

# image_list=[my_image1,my_image2,my_image3]


# length=len(image_list)
# index=0 

# label=Label(image=image_list[index])
# label.grid(row=0,column=0,columnspan=3,sticky="we")

# status = Label(root, text=f"Image {index+1} of {length}", bd=1, relief=SUNKEN, pady=10, anchor=W)
# status.grid(row=2, column=0, columnspan=3, sticky="we")


# def onclick(symbol):
#     global index, label,status
    
    

#     if symbol=="=>":
#         index=(index+1)%3
#     if symbol=="<=":
#         index=(index-1)%3
    
#     label.grid_forget()
#     label=Label(image=image_list[index])
#     label.grid(row=0,column=0,columnspan=3,sticky="we")

#     status=Label(root,text="Image "+str(index+1)+" of " +str(length),bd=1,anchor=W)
#     status.grid(row=2,column=0,columnspan=3,sticky='we',pady=10)


# button1=Button(root,text="=>",command=lambda:onclick("=>"),padx=10,pady=10)
# exit_button=Button(root,text="Exit",command=quit,padx=10,pady=10)
# button2=Button(root,text="<=",command=lambda:onclick("<="),padx=10,pady=10)


# button1.grid(row=1,column=2)
# exit_button.grid(row=1,column=1)
# button2.grid(row=1,column=0)


##############FRAME###################
# root.mainloop()


# root=Tk()

# frame=LabelFrame(root,text="This is my Frame",padx=70,pady=5)
# frame.pack(padx=10,pady=70)

# b=Button(frame,text="Don't click here")
# b.pack()

##########RADIO BUTTON AND POPUP#################
# root=Tk()
# r=StringVar()
# r.set(None)

# Modes=[
#     ("Pepproni","Pepproni"),
#     ("Cheese","Cheese"),
#     ("Mushroom","Mushroom"),
#     ("Onion","Onion"),
# ]


   
# def onclick():
#     n=r.get()
#     print(n)
#     label.config(text=f"Selected: {n}")

# def Popup():

#     response=messagebox.askyesno("This is Popup"," Choose your Pizza topping")
#     if response==1:
#         Label(root,text="You clicked Yes").pack()
#     else:
#         Label(root,text="You clicked Yes").pack()


# for mode in Modes :
#     Radiobutton(root,text=mode[0],variable=r,value=mode[1],command=onclick).pack(anchor=W)

# Button(root,text="PoPup",command=Popup).pack()

# # Radiobutton(root,text="Option 1",variable=r,value=1,command=onclick).pack()
# # Radiobutton(root,text="Option 2",variable=r,value=2,command=onclick).pack()

# label=Label(root, text=f"Selected: {r.get()}")
# label.pack()


# root.mainloop()


#####################################

# root=Tk()

# def open():
#     global my_image
#     top=Toplevel()
#     my_image=ImageTk.PhotoImage(Image.open("pic.jpg"))
    
#     label=Label(top,image=my_image)
    
#     label.pack()
#     Button(top,text="Close the window",command=top.destroy).pack()

# btn=Button(root,text="Open second window",command=open)
# btn.pack()


# root.mainloop()


#############FILE DIALOUGE to open file##################

# root=Tk()
# def open ():
#     global my_img
#     filname=filedialog.askopenfilename(initialdir=r"C:\Users\mewal\OneDrive\Pictures\Saved Pictures",title="Select a file",filetypes=(
#         ("PNG files", "*.png *.PNG"),
#         ("JPG files", "*.jpg *.JPG"),
#         ("All files", "*.*")
#     ))

#     my_img=ImageTk.PhotoImage(Image.open(filname).resize((250,250)))
#     Label(root,image=my_img).pack()
# Button(root,text="Select Photo",command=open).pack()

# root.mainloop()

#############SLIDERS######################
# root=Tk()
# root.geometry("300x400") 


# def update_label(value):
#     # value comes as a string from the scal
#     label.config(text=value)

# # Vertical scale
# vertical = Scale(root, from_=0, to=100, orient=VERTICAL, command=update_label)
# vertical.pack(side=RIGHT, fill=Y, expand=True)

# # Horizontal scale
# horizontal = Scale(root, from_=0, to=100, orient=HORIZONTAL)
# horizontal.pack(side=BOTTOM, fill=X, expand=True)

# # Label to show vertical scale value
# label = Label(root, text=str(vertical.get()), font=("Arial", 14))
# label.pack(pady=10)

# root.mainloop()


#########CHECKbox and derop menu###############

# root=Tk()

# var1=StringVar()
# var1.set(None)

# var2=StringVar()
# var2.set(None)

# options=["Pizza","Hamburger","Salad"]

# def show():
#     x=var1.get()
#     my_label.config(text=x)

# def onclick(value):
#     print(value)



# c=Checkbutton(root,text="Check me",variable=var1,onvalue="ON",offvalue="OFF",command=show)

# menu=OptionMenu(root,var2,*options,command=onclick)

# my_label=Label(root,text=var1.get())


# c.pack()
# my_label.pack()
# menu.pack()


# root.mainloop()



##########SQLITE##############
root=Tk()
conn=sqlite3.connect("adress_book.db")

c=conn.cursor()
# c.execute("""CREATE TABLE addresses(
#           first_name text,
#           last_name text,
#           address text,
#           city text,
#           state text,
#           zipcode integer
#           )""")




def submit():
    with sqlite3.connect("adress_book.db") as conn:
        c = conn.cursor()
        c.execute("""INSERT INTO addresses
                
                Values(:f_name,:l_name,:address,:city,:state,:zipcode)""",
                {
                'f_name':f_name.get(),
                'l_name':l_name.get(),
                'address':address.get(),
                'city':city.get(),
                'state':state.get(),
                'zipcode':zipcode.get()
                } )

        conn.commit()


    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    zipcode.delete(0,END)

    


def query():
    mono_font = ('Courier', 12)
    with sqlite3.connect("adress_book.db") as conn:
        c=conn.cursor()
        c.execute(""" SELECT rowid,* FROM  addresses""")
        records=c.fetchall()
        print_records=""
        for record in records:
            
             print_records += f"{record[1]:<15} {record[2]:<15} {str(record[0]):>5}\n"

        record_label = Label(root, text=print_records, font=mono_font, justify='left', anchor='w')
        record_label.grid(row=8, column=0, columnspan=3, sticky='we', padx=10, pady=5)
            
    
def delete(name):
    with sqlite3.connect("adress_book.db") as conn:
        c=conn.cursor()

        c.execute("Delete from addresses where first_name=?",(name,))
        delete_entry.delete(0,END)
        conn.commit()       




f_name=Entry(root,width=30)
f_name.grid(row=0,column=2,padx=20)
Label(root,text="First Name",anchor=W).grid(row=0,column=0)

l_name=Entry(root,width=30)
l_name.grid(row=1,column=2,padx=20)
Label(root,text="Last Name",anchor=W).grid(row=1,column=0)

address=Entry(root,width=30)
address.grid(row=2,column=2,padx=20)
Label(root,text="Address",anchor=W).grid(row=2,column=0)


city=Entry(root,width=30)
city.grid(row=3,column=2,padx=20)
Label(root,text="City",anchor=W).grid(row=3,column=0)


state=Entry(root,width=30)
state.grid(row=4,column=2,padx=20)
Label(root,text="State",anchor=W).grid(row=4,column=0)


zipcode=Entry(root,width=30)
zipcode.grid(row=5,column=2,padx=20)
Label(root,text="Zipcode",anchor=W).grid(row=5,column=0)

delete_entry=Entry(root,width=30)
delete_entry.grid(row=9,column=2,padx=20)
Label(root,text="Name to delete").grid(row=9,column=0,pady=20)



submit_button=Button(root,text="Submit",command=submit)
submit_button.grid(row=6,column=0,columnspan=3,pady=10,sticky="we",padx=10)

query_button=Button(root,text="show records",command=query)
query_button.grid(row=7,column=0,columnspan=3,sticky="we",padx=10,pady=10)

delete_button=Button(root,text="Delete",command=lambda:delete(delete_entry.get()))
delete_button.grid(row=10,column=0,columnspan=3,sticky="we",padx=10,pady=10)


root.mainloop()