# Importing modules
import customtkinter as tk
from db import *
from ml import *
import matplotlib.pyplot as plt
from PIL import Image
import pandas as pd
from sklearn.linear_model import LinearRegression
from captcha.image import ImageCaptcha
import random
# Create an instance of ImageCaptcha with desired width and height
image = ImageCaptcha(width=400, height=90)

# Generate a CAPTCHA text
captcha_text =''
# Generate an image object with the CAPTCHA text
data = 0
num = 0
# Save the image to a file
#image.write(captcha_text, 'CAPTCHA.jpg')


#functions____________________________________
def login():
    global captcha_text,num
    e=name.get()
    p=pss.get()
    c=cap.get()
    if e == '' or e[len(e) - 10:len(e)] != '@gmail.com':
        tk.CTkLabel(l_frame, text='Invalid Email', fg_color="red").place(rely=0.87, relx=0.5, anchor="center")
        l_frame.pack_forget()
        l_frame.pack(expand=True, fill=tk.BOTH)
        return
    elif len(p) < 8:
        tk.CTkLabel(l_frame, text='Password should be equal or greater than 8 characters', fg_color="red").place(rely=0.87, relx=0.5, anchor="center")
        l_frame.pack_forget()
        l_frame.pack(expand=True, fill=tk.BOTH)
        return
    elif c!=captcha_text:
        tk.CTkLabel(l_frame,text="Wrong captcha").place(rely=0.87, relx=0.5, anchor="center")
        l_frame.pack_forget()
        l_frame.pack(expand=True, fill=tk.BOTH)
        return
    else:
        num= isUser(e,p)
        if num:
            head.configure(text=f"Welcome")
            l_frame.pack_forget()
            home_frame.pack(expand=True,fill=tk.BOTH)
        else:
            tk.CTkLabel(l_frame, text="Login failed", fg_color="red").place(rely=0.87, relx=0.5, anchor="center")
            l_frame.pack_forget()
            l_frame.pack(expand=True, fill=tk.BOTH)
            return

def register():
    l_frame.pack_forget()
    register_frame.pack(expand=True,fill=tk.BOTH)

def signUp():
    global num
    r=r_name.get()
    p=r_pass.get()
    m=mob.get()
    e=r_email.get()
    if e == '' or e[len(e) - 10:len(e)] != '@gmail.com':
        tk.CTkLabel(register_frame, text='Invalid Email', fg_color="red").place(rely=0.6,relx=0.5,anchor="center")
        return
    elif len(m) != 10 and m.isdigit():

        tk.CTkLabel(register_frame, text='Invalid Contact', fg_color="red").place(rely=0.6,relx=0.5,anchor="center")
        return
    elif len(p) < 8:
        tk.CTkLabel(register_frame, text='Password should be equal or greater than 8 characters', fg_color="red").place(rely=0.6,relx=0.5,anchor="center")
        return
    else:
        g = createaccount(r,p,m,e)
        head.configure(text=f"Welcome {r},ID:{g}")
        num=g
        register_frame.pack_forget()

        home_frame.pack(expand=True,fill=tk.BOTH)

def forgotpass():
    l_frame.pack_forget()
    f_frame.pack(expand=True,fill=tk.BOTH)


def validate():
    n=f_name.get()
    m=f_mob.get()
    e=f_email.get()
    if e == '' or e[len(e) - 10:len(e)] != '@gmail.com':
        tk.CTkLabel(register_frame, text='Invalid Email', fg_color="red").place(rely=0.6, relx=0.5, anchor="center")
        return
    elif len(m) != 10 and m.isdigit():
        tk.CTkLabel(register_frame, text='Invalid Contact', fg_color="red").place(rely=0.6, relx=0.5, anchor="center")
        return
    else:
        if verify(n,m,e):
            f_frame.pack_forget()
            c_frame.pack(expand=True,fill=tk.BOTH)
        else:
            tk.CTkLabel(f_frame,text="User doesn't exist").place(rely=0.60,relx=0.5,anchor="center")
            return

def change():
    n=f_name.get()
    e=f_email.get()
    p1=c1.get()
    p2=c2.get()
    if p1!=p2 and len(p1)<8:
        tk.CTkLabel(c_frame,text="Passwords don't match").place(rely=0.6,relx=0.5,anchor="center")
        return
    else:
        changepass(e,n,p1)
        head.configure(text=f"Welcome {n}")
        c_frame.pack_forget()
        home_frame.pack(expand=True, fill=tk.BOTH)

def addingData():
    s=stock.get()
    qu=q.get()
    p=price.get()
    add(num,s,qu,p)
    tk.CTkLabel(home_frame, text="Data added").place(anchor="center", relx=0.5, rely=0.2)

def update():
    global num
    s = stock.get()
    qu = q.get()
    p = price.get()
    up(num, s, qu, p)
    tk.CTkLabel(home_frame, text="Record updated").place(anchor="center", relx=0.5, rely=0.2)



def delete():
    global num
    s = stock.get()
    dele(num,s)
    tk.CTkLabel(home_frame,text="Data Deleted").place(anchor="center",relx=0.5,rely=0.2)

#Creating main window
root = tk.CTk()
root.title("Login Page")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the size of the window to be the size of the screen
root.geometry(f"{screen_width}x{screen_height}")
root.geometry(f"+0+0")#sets the window at the top left
root.configure(bg='light blue')
tk.set_appearance_mode("dark")
tk.set_default_color_theme("dark-blue")
#login frame
l_frame=tk.CTkFrame(root)
l= tk.CTkLabel(l_frame,width=1000,height=100,text='Stock Predictor', font=("Bigshouldersdisplay", 72), text_color='white')
l.place(anchor="center", relx=0.50, rely=0.43)

my_image = tk.CTkImage(light_image=Image.open("imagewithtext.jpg"), dark_image=Image.open("imagewithtext.jpg") ,size= (250,300))
i = tk.CTkLabel(l_frame, image= my_image,text='')
#i.place(rely=0.3,relx=0.5,anchor="center")
i.pack()
name= tk.CTkEntry(l_frame,width=500, height=50, placeholder_text="Email")
name.place(rely = 0.50, relx=0.5,anchor="center")

pss= tk.CTkEntry(l_frame,width=500, height=50, show="*", placeholder_text="Password")
pss.place(rely = 0.55, relx=0.5, anchor="center")
def captcha():
    # Create an instance of ImageCaptcha with desired width and height
    global captcha_text,image,data
    # Generate a CAPTCHA text
    captcha_text = chr(random.randrange(97, 122)) + chr(random.randrange(97, 122)) + chr(random.randrange(97, 122)) + chr(random.randrange(97, 122)) + chr(random.randrange(97, 122)) + chr(random.randrange(97, 122))
    # Generate an image object with the CAPTCHA text
    data = image.generate(captcha_text)
    image.write(captcha_text, 'CAPTCHA.jpg')
    my = tk.CTkImage(light_image=Image.open("CAPTCHA.jpg"), dark_image=Image.open("CAPTCHA.jpg") ,size= (200,50))
    im = tk.CTkLabel(l_frame, image= my,text='')

    im.place(rely=.63,relx=0.5,anchor="center")


captcha()
reg=tk.CTkButton(l_frame,text="Regenerate",command=captcha)
reg.place(rely = 0.69, relx=0.7,anchor="center")
cap= tk.CTkEntry(l_frame,width=400, height=50, placeholder_text="Enter above captcha")
cap.place(rely = 0.69, relx=0.5,anchor="center")

login_button=tk.CTkButton(l_frame,text="Login", command=login)
login_button.place(rely = 0.75, relx=0.5, anchor="center")

register_button=tk.CTkButton(l_frame,text="Register",command=register)
register_button.place(rely = 0.79, relx=0.5, anchor="center")

forgot_button=tk.CTkButton(l_frame,text="Forgot Password?",command=forgotpass)
forgot_button.place(rely = 0.83, relx=0.5, anchor="center")


#frame for register

register_frame=tk.CTkFrame(root)
registerHeading=tk.CTkLabel(register_frame, width=1000, height=100, text="Register", font=("Bigshouldersdisplay", 72), text_color="white")
registerHeading.place(anchor="center", relx=0.5, rely=0.2)

r_name=tk.CTkEntry(register_frame,width=500, height=50, placeholder_text="Username")
r_name.place(rely = 0.35, relx=0.5,anchor="center")

r_pass=tk.CTkEntry(register_frame, width=500, height=50, placeholder_text="Password")
r_pass.place(rely = 0.4, relx=0.5,anchor="center")

mob=tk.CTkEntry(register_frame, width=500, height=50, placeholder_text="Mobile Number")
mob.place(rely=0.45,relx=0.5,anchor="center")

r_email=tk.CTkEntry(register_frame,width=500, height=50, placeholder_text="Email")
r_email.place(rely = 0.5, relx=0.5,anchor="center")

sign=tk.CTkButton(register_frame,text="Sign Up", command=signUp)
sign.place(rely = 0.55, relx=0.5, anchor="center")

#forgot password frame

f_frame=tk.CTkFrame(root)


registerHeading=tk.CTkLabel(f_frame, width=1000, height=100, text="Enter Credentials", font=("aerial", 72), text_color="white")
registerHeading.place(anchor="center", relx=0.5, rely=0.2)

f_name = tk.CTkEntry(f_frame, width=500, height=50, placeholder_text="Username")
f_name.place(rely = 0.35, relx=0.5,anchor="center")

f_mob=tk.CTkEntry(f_frame, width=500, height=50, placeholder_text="Mobile Number")
f_mob.place(rely = 0.40, relx=0.5,anchor="center")

f_email=tk.CTkEntry(f_frame,width=500, height=50, placeholder_text="Email")
f_email.place(rely=0.45, relx=0.5,anchor="center")

v_button=tk.CTkButton(f_frame,text="Sign up",command=validate)
v_button.place(rely = 0.55, relx=0.5, anchor="center")

#change password

c_frame=tk.CTkFrame(root)

h=tk.CTkLabel(c_frame,width=1000, height=100, text="Set New Password", font=("Bigshoulderdisplay",72), text_color="white")
h.place(anchor="center", relx=0.5, rely=0.2)

c1=tk.CTkEntry(c_frame,width=500, height=50, placeholder_text="New Password")
c1.place(rely=0.4,relx=0.5,anchor="center")

c2=tk.CTkEntry(c_frame,width=500, height=50, placeholder_text="Renter New Password")
c2.place(rely=0.45,relx=0.5,anchor="center")


tk.CTkButton(c_frame,text="Change",command=change).place(rely=0.50,relx=0.5,anchor="center")
c_button=tk.CTkButton(f_frame,text="Change", command=validate)
c_button.place(rely = 0.55, relx=0.5, anchor="center")


#home
home_frame = tk.CTkFrame(root)

head=tk.CTkLabel(home_frame,width=1000, height=100, text="Welcome", font=("Bigshouldersdisplay", 72), text_color="white")
head.place(anchor="center", relx=0.5, rely=0.1)


stock= tk.CTkEntry(home_frame, width=500, height=50, placeholder_text="Stock name")
stock.place(relx=0.5,rely=0.3,anchor="center")

price= tk.CTkEntry(home_frame, width=500, height=50, placeholder_text="Stock Price")
price.place(relx=0.5,rely=0.4,anchor="center")

q=tk.CTkEntry(home_frame, width=500, height=50, placeholder_text="Quantity")
q.place(relx=0.5,rely=0.5,anchor="center")

add_button = tk.CTkButton(master=home_frame, text="ADD to dataset", height = 50, command=addingData)
add_button.place(rely = 0.6, relx=0.5, anchor="center")

update_button = tk.CTkButton(master=home_frame, text="UPDATE in dataset", height = 50, command=update)
update_button.place(rely = 0.7, relx=0.4, anchor="center")

delete_button = tk.CTkButton(master=home_frame, text="DELETE from dataset", height = 50, command=delete)
delete_button.place(rely = 0.7, relx=0.6, anchor="center")

plot_button = tk.CTkButton(master=home_frame, text="PLOT", command=lambda:plot(num), width = 400, height=50)
plot_button.place(rely = 0.8, relx=0.5, anchor="center")

predict_button = tk.CTkButton(master=home_frame, text="PREDICT", command=lambda:pr(num), width = 400, height=50)
predict_button.place(rely = 0.9, relx=0.5, anchor="center")


#-----------------------------------------------------------------------------------------------

l_frame.pack(expand=True,fill=tk.BOTH)

# Running the main loop
root.mainloop()