import customtkinter as tk
from captcha.image import ImageCaptcha
import random
from PIL import Image
image = ImageCaptcha(width=400, height=90)

# Generate a CAPTCHA text
captcha_text =''
data = 0
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

def captcha():
    # Create an instance of ImageCaptcha with desired width and height
    global captcha_text,image,data
    # Generate a CAPTCHA text
    captcha_text = chr(random.randrange(97, 122)) + chr(random.randrange(97, 122)) + chr(random.randrange(97, 122)) + chr(random.randrange(97, 122)) + chr(random.randrange(97, 122)) + chr(random.randrange(97, 122))
    # Generate an image object with the CAPTCHA text
    data = image.generate(captcha_text)
    image.write(captcha_text, 'CAPTCHA.jpg')
    my = tk.CTkImage(light_image=Image.open("CAPTCHA.jpg"), dark_image=Image.open("CAPTCHA.jpg") ,size= (200,50))
    im = tk.CTkLabel(root, image= my,text='')

    im.place(rely=.1,relx=0.5,anchor="center")
def check():
    global captcha_text
    c = cap.get()
    if c != captcha_text:
        tk.CTkLabel(root, text="Wrong captcha").place(rely=0.4, relx=0.5, anchor="center")
        return
    else:
        tk.CTkLabel(root, text="Verified").place(rely=0.4, relx=0.5, anchor="center")
captcha()
reg=tk.CTkButton(root,text="Regenerate",command=captcha)
reg.place(rely = 0.2, relx=0.7,anchor="center")
cap= tk.CTkEntry(root,width=400, height=50, placeholder_text="Enter above captcha")
cap.place(rely = 0.2, relx=0.5,anchor="center")


login_button=tk.CTkButton(root,text="Verify", command=check)
login_button.place(rely = 0.3, relx=0.5, anchor="center")


root.mainloop()