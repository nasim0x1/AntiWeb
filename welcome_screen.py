from tkinter import *
from pathlib import Path
from tkinter.ttk import Progressbar, Style

import data_list
#
# password_file = Path(data_list.password_path)
# if password_file.is_file():
#     pass
# else:
#     with open(data_list.password_path,"w+") as password_file:
#         password_file.write("")
#         password_file.close()
#
# email_file= Path(data_list.email_path)
# if email_file.is_file():
#     pass
# else:
#     with open(data_list.email_path,"w+") as email_fil:
#         email_fil.write("")
#         email_fil.close()
#
# # root=tkinter.Tk()
# style = Style()
# style.theme_use("clam")
# root.after(3000,root.destroy)
# root.minsize(600,250)
# image =data_list.welcome_image
# root.wm_attributes('-type', 'splash')
# img= tkinter.PhotoImage(data=image)
# label = tkinter.Label(root,image=img)
# label.pack()
# progress = ttk.Progressbar(root, maximum=100, orient="horizontal", length=660, mode="indeterminate")
# progress.pack(side=tkinter.BOTTOM)
# progress.start(27)
# progress.after(2800,progress.destroy)
#
#
#
# root.mainloop()
class SplashScreen(Frame):
    def __init__(self, master=None, width=0.8, height=0.6, useFactor=True):
        Frame.__init__(self, master)
        self.pack(side=TOP, fill=BOTH, expand=YES)

        # get screen width and height
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        w = 600
        h = 250
        # calculate position x, y
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.master.overrideredirect(True)
        self.lift()


if __name__ == '__main__':
    password_file = Path(data_list.password_path)
    if password_file.is_file():
        pass
    else:
        with open(data_list.password_path, "w+") as password_file:
            password_file.write("")
            password_file.close()

    email_file = Path(data_list.email_path)
    if email_file.is_file():
        pass
    else:
        with open(data_list.email_path, "w+") as email_fil:
            email_fil.write("")
            email_fil.close()
    root = Tk()

    sp = SplashScreen(root)

    root.after(3000, root.destroy)
    root.minsize(650, 250)
    style = Style()
    style.theme_use("clam")
    image = data_list.welcome_image
    root.wm_attributes('-type', 'splash')
    img = PhotoImage(data=image)
    label = Label(root, image=img)
    label.pack()
    progress = Progressbar(root, maximum=100, orient="horizontal", length=660, mode="indeterminate")
    progress.pack(side=BOTTOM)
    progress.start(27)
    progress.after(2800, progress.destroy)

    root.mainloop()