import os
from tkinter import *
from tkinter import messagebox
import data_list
password_path = data_list.password_path
secret_key = '1234567890123456'

class Main(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.pw = 350
        self.ph = 155
        self.ws = self.winfo_screenwidth()
        self.hs = self.winfo_screenheight()
        self.px = (self.ws / 2) - (self.pw / 2)
        self.py = (self.hs / 2) - (self.ph / 2)
        self.geometry('%dx%d+%d+%d' % (self.pw, self.ph, self.px, self.py))
        self.title('Set Password')
        self.resizable(0, 0)
        def quit():
            import sys
            sys.exit()
        def window_close_click():
            save_password()
        self.protocol("WM_DELETE_WINDOW", quit)


        Label(self,text="Email:").place(relx=0.06, rely=0.13, height=19, width=49)
        Label(self,text="Password:").place(relx=0.06, rely=0.34, height=19, width=68)
        Label(self,text="Retype Password:").place(relx=0.06, rely=0.52, height=19, width=118)


        input_email = Entry(self)
        input_email.place(relx=0.43, rely=0.1, relheight=0.14, relwidth=0.47)
        input_password = Entry(self)
        input_password2 = Entry(self)
        input_password2.place(relx=0.43, rely=0.5, relheight=0.14, relwidth=0.47)
        input_password.place(relx=0.43, rely=0.3, relheight=0.14, relwidth=0.47)
        input_password2.config(show="*")
        input_password.config(show="*")


        def save_password():
            email = input_email.get()
            password_get = input_password.get()
            password_get2 = input_password2.get()

            if len(password_get) == 0:
                messagebox.showerror("Error", "Please Input Any Number or Text")
            else:
                if password_get==password_get2:
                    if len(email)==0:
                        messagebox.showinfo("Note","Please Input Valid Email To Recover Your Password")
                    else:
                        with open(data_list.email_path, 'r+') as file_email:
                            file_email.write(email)
                            file_email.close()

                    with open(password_path, 'r+') as file:
                        file.write(password_get2)
                        file.close()
                    self.destroy()

                else:
                    messagebox.showerror("Error","Password Do Not Match")

        Button(self,text="Save",command=save_password).place(relx=0.66, rely=0.75, height=28, width=83)
        Button(self,text="Quit",command=quit).place(relx=0.09, rely=0.77, height=28, width=83)
if os.stat(password_path).st_size == 0:
    pass_status=False
else:
    pass_status = True
if pass_status == False:
    run = Main()
    run.mainloop()
else:
    pass