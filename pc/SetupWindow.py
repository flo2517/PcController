from tkinter import *
from PIL import Image, ImageTk
import os.path

class Setup:

    def onSetupClose(self):
        if self.credWin is not None:
            if self.credWin is not None:
                try:
                    self.credWin.destroy()
                except TclError:
                    pass
            self.creditBtn.configure(state=ACTIVE)

    def onCreditsClose(self):
        self.creditBtn.configure(state=ACTIVE)
        self.credWin.destroy()

    # Display the beautiful and too cute little panda at the bottom of the credit window
    def displayCutePanda(self):
        path = 'pictures/panda.png'
        # Check file existence
        if os.path.exists(path):
            panda = Canvas(self.credWin, bg="#aaaaaa", bd=0, highlightthickness=0, relief="ridge")

            # Load and resize picture
            img = Image.open(path)
            img = img.resize((64, 64))
            img = ImageTk.PhotoImage(master=self.credWin, image=img)

            # Place picture
            panda.create_image(380, 70, anchor=SE, image=img)

            # Display canvas
            panda.pack()
            panda.mainloop()
            return
        else:
            print('Picture not found')
            return

    # Open credit window
    def creditsWin(self):
        self.creditBtn.configure(state=DISABLED)
        self.credWin = Tk()
        self.credWin.title("Credits")
        self.credWin.geometry("550x550")
        self.credWin.configure(bg="#aaaaaa")
        self.credWin.resizable(False, False)
        self.credWin.protocol("WM_DELETE_WINDOW", self.onCreditsClose)

        creditText = "Welcome to PC Remote Controller,\n\nThis is our end-of-licence project at the \ncomputer science university of Besançon.\n\nUnder the supervision of our teachers Mrs. \nFelea and Mr. Merlet, this project was \ncarried out by Laura Bobillier, Florian \nJeandenans and Maxime Caron.\n\nThank you for using our app !\n\n\nWe especially thank the Stackoverflow \ncommunity as well as the Indian youtube \nchannels for their precious help."

        textArea = Text(self.credWin, state='normal', padx=50, pady=10, bd=0, highlightthickness=0, relief="ridge")
        textArea.insert('end', creditText)
        textArea.configure(state='disabled', bg="#aaaaaa", font=("Arial", 15, 'bold'), width=100, height=17)
        textArea.pack()

        self.displayCutePanda()

        self.credWin.mainloop()

    # Log out user
    def logOut(self):
        self.result[0] = 1
        self.setupWin.destroy()

    # End program
    def exitApp(self):
        self.result[0] = 2
        if self.credWin is not None:
            try:
                self.credWin.destroy()
            except TclError:
                pass
        self.setupWin.destroy()

    def __init__(self, localUserData, result):
        self.credWin = None
        self.result = result
        self.localUserData = localUserData
        self.setupWin = Tk()
        self.setupWin.title("Setup")

        self.setupWin.geometry("750x600")
        self.setupWin.configure(bg="#21a6ff")
        self.setupWin.resizable(False, False)

        self.setupWin.protocol("WM_DELETE_WINDOW", self.onSetupClose)

        self.startUpLaunch = False

        Label(self.setupWin, text="Setup", font=("Arial", 40), bg="#21a6ff", pady=20).pack()

        # Add log out button
        Button(self.setupWin, text="Log Out", font=("Arial", 20), relief="solid", borderwidth=3, height=1, width=30,
               command=self.logOut).pack(pady=20)

        # Add change password button
        Button(self.setupWin, text="Change Password", font=("Arial", 20), relief="solid", borderwidth=3, height=1,
               width=30).pack(pady=10)

        # Add del account button
        Button(self.setupWin, text="Del Account", font=("Arial", 20), relief="solid", borderwidth=3, height=1,
               width=30).pack(pady=10)

        # Add credit button
        self.creditBtn = Button(self.setupWin, text="Credits", font=("Arial", 20), relief="solid", borderwidth=3,
                                height=1,
                                width=30, command=self.creditsWin)
        self.creditBtn.pack(pady=10)

        # Add close app button
        Button(self.setupWin, text="Exit app", font=("Arial", 20), relief="solid", borderwidth=3, height=1, width=30,
               command=self.exitApp).pack(pady=10)

        # Add launch on pc starting check button
        Checkbutton(self.setupWin, text="Start-up launch", font=("Arial", 20), var=self.startUpLaunch, bg="#21a6ff",
                    activebackground='#21a6ff').pack(side=RIGHT, pady=10, padx=40)

        self.setupWin.mainloop()
