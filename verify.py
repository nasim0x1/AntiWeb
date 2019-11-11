from tkinter import *
from tkinter import messagebox


import data_list


class Main(Tk):
    def __init__(self):
        Tk.__init__(self)
        pw = 350
        ph = 105
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        px = (ws / 2) - (pw / 2)
        py = (hs / 2) - (ph / 2)
        self.geometry('%dx%d+%d+%d' % (pw, ph, px, py))
        self.title('Set New Password')

        def quit():
            import sys
            sys.exit()
        def check_pass_and_save():
            with open(data_list.password_path,"r+") as email_file:
                v_code = email_file.read()

            in_pass = self.new_pass.get()
            input_code = self.verifi_code.get()

            if v_code == input_code:
                if len(in_pass)==0:
                    messagebox.showerror("Error",'Input  Value')
                else:
                    new_password = in_pass

                    with open(data_list.password_path,"w+") as new_pas:
                        new_pas.write(new_password)
                    ask = messagebox.showinfo("Success","Password Successfully Change")
                    if ask == "ok":
                        self.destroy()
            else:
                messagebox.showerror("Error","Email Verification Code Wrong")

        self.protocol("WM_DELETE_WINDOW", quit)
        Label(self,text="Verify Code:").place(relx=0.04, rely=0.1, height=21, width=90)
        Label(self,text="New Password:").place(relx=0.04, rely=0.41, height=21, width=103)

        self.verifi_code = Entry(self)
        self.verifi_code.place(relx=0.37, rely=0.1,height=23, relwidth=0.55)

        self.new_pass = Entry(self)
        self.new_pass.place(relx=0.37, rely=0.38,height=23, relwidth=0.55)

        self.btn_set = Button(self, text="Save",command = check_pass_and_save)
        self.btn_set.place(relx=0.68, rely=0.68, height=28, width=83)

run = Main()
run.mainloop()