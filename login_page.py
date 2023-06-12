import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk 

ctk.set_appearance_mode('Dark')
ctk.set_default_color_theme('blue')

def frames():
    global frame1, frame2
    frame1 =ctk.CTkFrame(window)
    frame1.grid(row = 0, column = 0, pady = (200, 0), padx = (600))

    frame2 = ctk.CTkFrame(window)
    frame2.grid(row=1, column = 0, pady = (0, 300))

    

def first_frame():
    welcome_label = ctk.CTkLabel(frame1, text='Welcome to our website', font=('montserat', 20, 'italic'))
    welcome_label.grid(row=0, column =0, padx=(20, 35), pady=(30,15))

    sign_up_button = ctk.CTkButton(frame1, text='Sign Up', font=('Montserat', 16, 'bold'), command= sign_up)
    sign_up_button.grid(row=0, column =2)

def second_frame():
    login_label = ctk.CTkLabel(frame2, text='Log In', font=('Arial', 30, 'bold'))
    login_label.grid(row=0, column=0, padx = 55)

    user_label = ctk.CTkLabel(frame2, text='Username', font=('arial', 16))
    user_label.grid(row=1,column = 0, pady=(60, 10))
    user_entry = ctk.CTkEntry(frame2, placeholder_text='Enter your Username')
    user_entry.grid(row=1,column = 1, pady=(60, 10), padx = (20, 50))
    
    password_label = ctk.CTkLabel(frame2, text='Password', font=('arial', 16))
    password_label.grid(row=2,column = 0, pady=(20, 10))
    password_entry = ctk.CTkEntry(frame2,show = '*', placeholder_text='Enter your Passowrd')
    password_entry.grid(row=2,column = 1, pady=(20, 10), padx = (20, 50))

    forget_password = ctk.CTkButton(frame2, text='Forget Password', font=('arial', 14, 'italic'), fg_color='transparent')
    forget_password.grid(row=3, column=1, pady = (5, 20), padx = (20, 50))


def all_functions():
    frames()
    first_frame()
    second_frame()

def sign_up():
    global frame3
    frame1.forget()
    frame2.forget()
    frame3 = ctk.CTkFrame(window)
    frame3.grid(row = 0, column = 0, pady = (200), padx = (600))
     #Section for the sign up page



def sigining_up():
    signup_label = ctk.CTkLabel(frame3, text='Sign Up', font=('Arial', 20, 'bold') )
    signup_label.grid(row = 0, column = 0, pady = (90, 30))

    first_name = ctk.CTkLabel(frame3, text='First Name', font=('arial', 16, 'italic'))
    first_name.grid(row = 1, column = 0)
    first_name_entry = ctk.CTkEntry(frame3, placeholder_text='Enter your Surname')
    first_name_entry.grid(row = 1, column = 1, padx = (20, 40), pady = 10)

    second_name = ctk.CTkLabel(frame3, text='Last name', font=('arial', 16, 'italic'))
    second_name.grid(row = 2, column = 0)
    second_name_entry = ctk.CTkEntry(frame3, placeholder_text='Enter your last name')
    second_name_entry.grid(row = 2, column = 1, padx = (20, 40), pady = 10)

    email = ctk.CTkLabel(frame3, text='Email', font=('arial', 16, 'italic'))
    email.grid(row = 3, column = 0)
    email_entry = ctk.CTkEntry(frame3, placeholder_text='Enter your email')
    email_entry.grid(row = 3, column = 1, padx = (20, 40), pady = 10)

    password = ctk.CTkLabel(frame3, text='Password', font=('arial', 16, 'italic'))
    password.grid(row = 4, column = 0)
    password_entry = ctk.CTkEntry(frame3, placeholder_text='Password')
    password_entry.grid(row = 4, column = 1, padx = (20, 40), pady= 10)
 
    confirm_password = ctk.CTkLabel(frame3, text='Confirm Password', font=('arial', 16, 'italic'))
    confirm_password.grid(row = 5, column = 0)
    confirm_password_entry = ctk.CTkEntry(frame3, placeholder_text='Confirm Password')
    confirm_password_entry.grid(row = 5, column = 1, padx = (20, 40), pady = (10))


if __name__ == '__main__':
    window = ctk.CTk()
    #window.geometry('400x400')
    window.iconbitmap('ayo_logo.ico')
    window.title('Code Connect')
    # img = Image.open('shutterstock-business-technology.jpg')
    # bg = ImageTk.PhotoImage(img)

    #bg_label = tk.Label(window, image=bg)
    #bg_label.grid()






    all_functions()


    #login_label = 
  
#
 




    window.mainloop()