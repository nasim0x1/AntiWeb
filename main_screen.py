import os
import webbrowser
from tkinter import *
from tkinter import messagebox, ttk,PhotoImage
from tkinter.ttk import Style, Notebook
import data_list


class Main(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title('AntiWeb - Smart Shield')
        self.style = Style()
        self.style.theme_use("clam")
        self.resizable(0, 0)
        self.pw = 350
        self.ph = 100
        self.w = 600
        self.h = 350
        self.ws = self.winfo_screenwidth()
        self.hs = self.winfo_screenheight()
        self.x = (self.ws / 2) - (self.w / 2)
        self.y = (self.hs / 2) - (self.h / 2)
        self.px = (self.ws / 2) - (self.pw / 2)
        self.py = (self.hs / 2) - (self.ph / 2)
        self.geometry('%dx%d+%d+%d' % (self.w, self.h, self.x, self.y))
        img = PhotoImage(data=data_list.window_icon)
        self.call('wm', 'iconphoto', self._w, img)
        ####Host File Editing
        hosts_path = data_list.hosts_path
        website_list =data_list.website_list
        password_path = data_list.password_path
        secret_key = '1234567890123456'

        ###Get  Password
        with open(password_path, 'r+') as file:
            content = file.read()
            get_password = content
        ### Password Check
        if os.stat(password_path).st_size == 0:
            pass_status = False
        else:
            pass_status = True

        #Password Change
        def change_pass():
            get = self.old_pass.get()

            if get_password == get:
                input_new_pass = self.new.get()
                input_new_pass_retype=self.new_retype.get()

                if input_new_pass == input_new_pass_retype:
                    new_pass = str(input_new_pass_retype)
                    with open(password_path, 'r+') as file:
                        file.truncate()
                        file.write(new_pass)
                    ask = messagebox.showinfo("Success","Password Change Successfully.")

                else:
                    messagebox.showerror("Error",'New password do not match')
            else:
                messagebox.showerror("Error", 'Old password do not match')

        ### Status
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    self.status = True
                else:
                    self.status = False

        ##Decticvating Shelid
        def deactivating():
            if self.status == True:
                with open(hosts_path, 'r+') as file:
                    file.truncate()


        def quit():
            import sys
            sys.exit()

        self.protocol("WM_DELETE_WINDOW", quit)

        # Define Active Button
        def active():
            if pass_status == True:
                ask = messagebox.askyesno("", "This window will close after activated shield.Do you want?")
                if ask == True:
                    import active_shield
                    active_shield
                    self.after(900, self.destroy)
            else:
                check_password()

        # Define Deactivated Button
        def deactivate():
            top = Toplevel()
            top.title("Password")
            top.resizable(0, 0)
            top.geometry('%dx%d+%d+%d' % (self.pw, self.ph, self.px, self.py))

            Label(top, text='Input Password ').pack()
            pass_entry = Entry(top, )
            pass_entry.config(show="☠")
            pass_entry.pack()

            def close_window():
                get = pass_entry.get()

                if get_password == get:
                    top.destroy()

                    def deactivating_window():
                        self.DeactiveButton.configure(state="disable")
                        top = Tk()
                        top.wm_attributes('-type', 'splash')
                        prgrassingbar = ttk.Progressbar(top, maximum=100, orient="horizontal", length=100,
                                                        mode="indeterminate")
                        prgrassingbar.pack()

                        prgrassingbar.start(10)

                        def alert():
                            prgrassingbar.stop()
                            top.destroy()
                            messagebox.showinfo("Success", "Your Shield Deactivated")
                            self.DeactiveButton.destroy()
                            self.Status_Active.destroy()
                            self.Status_Deactive.pack(expand=1, fill="both")
                            self.ActiveButton.pack(expand=1, fill="both")

                        prgrassingbar.after(1190, alert)

                    deactivating()
                    deactivating_window()

                else:
                    messagebox.showerror("Error", "Wrong Password")

            Button(top, text="OK", command=close_window, ).pack()

        # Verify Activation
        def Status():
            if self.status == True:
                self.Status_Active.pack(expand=1, fill="both")
                self.DeactiveButton.pack(expand=1, fill="both")
            if self.status == False:
                self.Status_Deactive.pack(expand=1, fill="both")
                self.ActiveButton.pack(expand=1, fill="both")

        # Installing Tabs

        tab = Notebook(self, style='lefttab.TNotebook')
        self.activation = Frame(tab)

        ## Active Deactive Button

        self.Status_Active = Label(self.activation, text="Shield Activated", fg="blue")
        self.Status_Deactive = Label(self.activation, fg="red", text="Shield Deactivate Now")
        self.DeactiveButton = Button(self.activation, text="Deactivate Shield", command=deactivate)
        self.ActiveButton = Button(self.activation, text="Activated Shield", command=active)

        # change password page
        change_password = Frame(tab)


        self.TSizegrip1 = ttk.Sizegrip(change_password)
        self.TSizegrip1.place(anchor=SE, relx=1.0, rely=1.0)

        self.label_top = ttk.Label(change_password)
        self.label_top.place(relx=0.40, rely=0.12, )
        self.label_top.configure(background="#d9d9d9")
        self.label_top.configure(foreground="red")
        self.label_top.configure(relief=FLAT)
        self.label_top.configure(text='''Change Password''')



        self.TLabel1 = ttk.Label(change_password)
        self.TLabel1.place(relx=0.17, rely=0.27,)
        self.TLabel1.configure(background="#d9d9d9")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(relief=FLAT)
        self.TLabel1.configure(text='''Old Password:''')

        self.TLabel1_1 = ttk.Label(change_password)
        self.TLabel1_1.place(relx=0.17, rely=0.39,)
        self.TLabel1_1.configure(background="#d9d9d9")
        self.TLabel1_1.configure(foreground="#000000")
        self.TLabel1_1.configure(relief=FLAT)
        self.TLabel1_1.configure(text='''New Password:''')

        self.TLabel1_2 = ttk.Label(change_password)
        self.TLabel1_2.place(relx=0.17, rely=0.52,)
        self.TLabel1_2.configure(background="#d9d9d9")
        self.TLabel1_2.configure(foreground="#000000")
        self.TLabel1_2.configure(relief=FLAT)
        self.TLabel1_2.configure(text='''Retype Password:''')

        self.old_pass = Entry(change_password)
        self.old_pass.config(show="*")
        self.old_pass.place(relx=0.39, rely=0.27, relheight=0.06, relwidth=0.32)

        self.new = Entry(change_password, )
        self.new.config(show="*")
        self.new.place(relx=0.39, rely=0.39, relheight=0.06, relwidth=0.32)

        self.new_retype = Entry(change_password, )
        self.new_retype.config(show="*")
        self.new_retype.place(relx=0.39, rely=0.52, relheight=0.06, relwidth=0.32)

        change_btn = Button(change_password, command=change_pass)
        change_btn.place(relx=0.39, rely=0.67, height=28, width=83)
        change_btn.configure(takefocus="")
        change_btn.configure(text='''Save''')


        ###Change Email
        change_email = Frame(tab,)




        def change_email_file():
            new_mail = self.new_email.get()
            if len(new_mail)==0:
                messagebox.showinfo("Note","Type A Email")
            else:
                with open(data_list.email_path,"w+") as new_email:
                    new_email.write(new_mail)
                messagebox.showinfo('Success', "Email Change")

        with open(data_list.email_path,"r+") as read_email:
            show_email= read_email.read()


        self.label_top_email = ttk.Label(change_email)
        self.label_top_email.place(relx=0.40, rely=0.12, )
        self.label_top_email.configure(background="#d9d9d9")
        self.label_top_email.configure(foreground="red")
        self.label_top_email.configure(relief=FLAT)
        self.label_top_email.configure(text='''Change Email''')


        email_show=str("Your Mail : {}".format(show_email))
        Label(change_email,text=email_show).place(relx=0.30, rely=0.28)


        self.Label1 = Label(change_email)
        self.Label1.place(relx=0.29, rely=0.40, height=21, width=55)
        self.Label1.configure(text='''Email:''')
        self.Label1.configure(width=55)


        self.new_email = Entry(change_email,)
        self.new_email.place(relx=0.45, rely=0.40, relheight=0.06, relwidth=0.34)

        change_btn = Button(change_email, text="Change Email", command=change_email_file)
        change_btn.place(relx=0.42, rely=0.54)


        # ##Website List Tab
        # web_list = Frame(tab)
        # listNodes = Listbox(web_list, width=64, height=20, font=("Helvetica", 12))
        # listNodes.pack(side="left", fill="y")
        # scrollbar = Scrollbar(web_list, orient="vertical")
        # scrollbar.config(command=listNodes.yview)
        # scrollbar.pack(side="right", fill="y")
        # listNodes.config(yscrollcommand=scrollbar.set)
        # if self.status==True:
        #     with open(hosts_path) as fp:
        #         line = fp.readline()
        #         for line in fp:
        #             web_list_with_number=line.replace("127.0.0.1","⋇")
        #             listNodes.insert(END, str(web_list_with_number))
        # else:
        #     listNodes.insert(END, str("Shield Do Not Active"))
        ##other
        other = Frame(tab,)
        def fb_page():
            webbrowser.open(data_list.facebook_link)

        def developer():
            def about_window_close():
                about_info.config(state="normal")
                root.destroy()
            about_info.config(state="disable")
            root = Toplevel(self)
            root.title('About Developer')
            root.resizable(0, 0)
            root.geometry('%dx%d+%d+%d' % (self.w, self.h, self.x, self.y))
            image =data_list.about_developer_image
            img= PhotoImage(data=image)
            label = Label(root, image=img).pack()
            root.protocol("WM_DELETE_WINDOW", about_window_close)
            root.mainloop()
        fb_btn=Button(other,text="Like Our Facebook Page",command=fb_page)
        fb_btn.pack(expand=1, fill="both")
        about_info=Button(other,text="About Developer",command=developer)
        about_info.pack(expand=1, fill="both")



        tab.add(self.activation, text='Shield Status', compound=TOP)
        tab.add(change_password, text='Change Password')
        tab.add(change_email, text='Change Email')
        # tab.add(web_list, text='Block Web List')
        tab.add(other, text='About Us')
        tab.pack(expand=1, fill="both")

        ## Password Setting Sector
        def check_password():
            if pass_status == False:
                set_password = messagebox.showinfo("", "Set Password. It's Need To Active Your Shield")
                if set_password == 'ok':
                    import user_account_setup
                    user_account_setup
        def user_login():
            messagebox.showinfo("")

        ##Call All Funcatins
        check_password()
        Status()
##Run Main Class
def splash_screen():
    import welcome_screen
    welcome_screen
    import user_login
    user_login
    import user_account_setup
    user_account_setup

splash_screen()
run = Main()
run.mainloop()