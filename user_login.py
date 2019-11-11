import os
import smtplib
import email.message
import socket
from tkinter import *
from tkinter import messagebox
import data_list


password_path = data_list.password_path
secret_key = '1234567890123456'

class Main(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.pw = 350
        self.ph = 110
        self.w = 600
        self.h = 350
        self.ws = self.winfo_screenwidth()
        self.hs = self.winfo_screenheight()
        self.x = (self.ws / 2) - (self.w / 2)
        self.y = (self.hs / 2) - (self.h / 2)
        self.px = (self.ws / 2) - (self.pw / 2)
        self.py = (self.hs / 2) - (self.ph / 2)
        self.geometry('%dx%d+%d+%d' % (self.pw, self.ph, self.px, self.py))
        self.title('Login')
        self.resizable(0, 0)
    ### Sending Mail

        def quit_win():
            self.forget_pass_btn.configure(state="normal")
            self.login.configure(state="normal")
            self.root.destroy()

        def forget_window():
            self.forget_pass_btn.configure(state="disable")
            self.login.configure(state="disable")


            def send_verify_code():
                with open(data_list.email_path,"r+") as email_file:
                    old_email= email_file.read()
                get_mail = self.input_email.get()
                if len(get_mail)==0:
                    messagebox.showinfo("Note","Email Required")
                else:
                    if old_email == get_mail:
                        ### SMTP setup
                        with open(data_list.password_path, "r+")as file:
                            password = file.read()
                        try:
                            server = smtplib.SMTP('smtp.gmail.com:587')
                            get_password = 35435
                            send_pass = ("Your Verification Code Is : {}".format(password))
                            msg = email.message.Message()
                            msg['Subject'] = 'AntiWeb - Verification Code'

                            msg['From'] = data_list.smpt_mail
                            msg['To'] = get_mail
                            password = data_list.smpt_mail_password
                            msg.add_header('Content-Type', 'text/html')
                            msg.set_payload(send_pass, )
                            s = smtplib.SMTP('smtp.gmail.com: 587')
                            s.starttls()

                            # Login Credentials for sending the mail
                            s.login(msg['From'], password)

                            s.sendmail(msg['From'], [msg['To']], msg.as_string())
                            self.destroy()
                            import verify
                            verify.mainloop()


                        except socket.error as e:
                            messagebox.showerror("Error", "Sending Failed")


                    else:
                        messagebox.showerror("Error", "Email Not Found")


            self.root = Toplevel(self)
            self.root.protocol("WM_DELETE_WINDOW", quit_win)
            pw = 350
            ph = 85
            ws = self.root.winfo_screenwidth()
            self.root.title('Forget Password')
            hs = self.root.winfo_screenheight()
            px = (ws / 2) - (pw / 2)
            py = (hs / 2) - (ph / 2)
            self.root.geometry('%dx%d+%d+%d' % (pw, ph, px, py))

            self.Label1 = Label(self.root)
            self.Label1.place(relx=0.11, rely=0.20, height=21, width=76)
            self.Label1.configure(text='''Email:''')
            self.Label1.configure(width=76)

            self.input_email = Entry(self.root)
            self.input_email.place(relx=0.34, rely=0.20)

            self.btn_next= Button(self.root,text="Next",command=send_verify_code)
            self.btn_next.place(relx=0.43, rely=0.58)




        def quit():
            import sys
            sys.exit()
        self.protocol("WM_DELETE_WINDOW", quit)

        self.Label1 = Label(self)
        self.Label1.place(relx=0.11, rely=0.25, height=21, width=76)
        self.Label1.configure(text='''Password:''')
        self.Label1.configure(width=76)


        input_password = Entry(self)
        input_password.place(relx=0.34, rely=0.25)
        input_password.config(show="☠")



        def user_login():
            password_get = input_password.get()


            if len(password_get) == 0:
                messagebox.showerror("Error", "Please Input Your Password")
            else:
                with open(password_path, 'r+') as file:
                    content = file.read()
                    if content == password_get:
                        self.destroy()
                    else:
                        messagebox.showerror("Error", "Your Input Password Do Not Match")



        self.login=Button(self,text="Login",command=user_login)
        self.login.place(relx=0.69, rely=0.62,)
        self.forget_pass_btn =Button(self,text="Forget",command=forget_window)
        self.forget_pass_btn.place(relx=0.16, rely=0.62,)



if os.stat(password_path).st_size == 0:
    pass_status=False
else:
    pass_status = True
if pass_status == True:
    run = Main()
    run.mainloop()
else:
    pass