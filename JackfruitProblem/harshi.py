import tkinter as tk
from tkinter import messagebox

users_allowed=['Alice Johnson',"Bob Smith"]
password_allowed=['Alice_Johnson@123','Bob_smith@123']

root=tk.Tk()
root.title("Restraunt Booking")
root.geometry('800x600')
root.resizable(True,True)

user_id=tk.StringVar()
password=tk.StringVar()





def Submit():
    user=user_id.get()
    pasw=password.get()
    
    if user in users_allowed and pasw in password_allowed:
        messagebox.showinfo(f"Login Successful!","Welcome "+user)
        
        root.destroy()
        root2=tk.Tk()
        root2.title("Restraunt Booking System")
        root2.geometry("800x600")
        root2.resizable(True,True)
        
        with open(r'D:\Hamza\Python\Hackathon_Question\Hackathon_Question\restaurants.csv')
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    else: 
        messagebox.showerror("Login Failed!","Try Again")
    
    print(f"The user is: {user}")
    print(f"The password is: {pasw}")
    
    user_id.set("")
    password.set("")
    

def show_hide():
    if password_entry.cget("show")=="":
        password_entry.config(show="*")
        password_ticker.config(text="Show Password")
    else: 
        password_entry.config(show="")
        password_ticker.config(text="Hide Password")
    



id_label=tk.Label(root,text="User Id",font=("calibre",15,'bold'))
id_entry=tk.Entry(root,textvariable=user_id,font=("calibre",15,"normal"))




password_ticker=tk.Checkbutton(root,text="Show Password",onvalue=1,offvalue=0,command=show_hide)
password_label=tk.Label(root,text="Password",font=("calibre",15,"bold"))
password_entry=tk.Entry(root,textvariable=password,font=("calibre",15,"normal"),show="*")




sub_btn=tk.Button(root,text="Submit",font=("calibre",10,'normal'),command=Submit)

id_label.grid(row=50,column=50,padx=50,pady=50)
id_entry.grid(row=50,column=60)
password_label.grid(row=60,column=50)
password_entry.grid(row=60,column=60)
password_ticker.grid(row=90,column=55)
sub_btn.grid(row=80,column=60)





root.mainloop()