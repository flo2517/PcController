import re
from tkinter import *
from APICommunication import HttpsRequest
from PIL import Image, ImageTk
import os.path


class ChangePassword:
    def getWindow(self):
        return self.chgPassWin

    def onClosing(self):
        self.changePasswordBtn.configure(state=ACTIVE)
        self.exitBtn.configure(state=ACTIVE)
        self.chgPassWin.destroy()

    def checkOldPassword(self):
        if not self.oldPassword.get() == self.userData.getUserPassword():
            print("Error: Old password is incorrect")
            return False
        return True

    def checkNewPassword(self):
        print("Checking new passwords")
        # regex = r'^(?=.[a-z])(?=.[A-Z])(?=.\d)(?=.[@$!%?&])[A-Za-z\d@$!%?&]{8,}$'

        if len(self.newPassword1.get()) > 255 or len(self.newPassword1.get()) < 6:
            print("Error: Invalid size of password")
            return False

        if self.oldPassword.get() == self.newPassword1.get():
            print("Error : New password need to be different as old password")
            return False

        """
        if not re.fullmatch(regex, self.newPassword1.get()):
            print("Error: Password to week")
            return False
        """

        if not self.newPassword1.get() == self.newPassword2.get():
            print("Error: \"Confirm new password\" must be the same as \"New Password\"")
            return False

        return True

    def sendRequest(self):
        rqt = HttpsRequest()
        res = rqt.changePassword(self.oldPassword.get(), self.newPassword1.get())
        return res

    def submit(self):
        print("Checking old password")
        if not self.checkOldPassword():
            return False

        print("Checking new password")
        if not self.checkNewPassword():
            return False

        """
        print('submit')
        if not self.sendRequest():
            return False
        """

        # Show setup window
        self.setupWin.deiconify()
        self.chgPassWin.destroy()

    def __init__(self, userData, changePasswordBtn, exitBtn):
        self.userData = userData
        self.changePasswordBtn = changePasswordBtn
        self.exitBtn = exitBtn
        self.chgPassWin = Tk()
        self.chgPassWin.title('Change Password')
        self.chgPassWin.geometry("500x500")
        self.chgPassWin.configure(bg="#21a6ff")
        self.chgPassWin.resizable(False, False)
        # Add action on window close event
        self.chgPassWin.protocol("WM_DELETE_WINDOW", self.onClosing)

        # Add text to window
        Label(self.chgPassWin, text="Change Password", font=("Arial", 40), bg="#21a6ff", pady=15).pack()

        # Old password input
        Label(self.chgPassWin, text="Old password:", font=("Arial", 15, "bold"), bg="#21a6ff").pack(padx=(70, 290))
        self.oldPassword = Entry(self.chgPassWin, font=("Arial", 25), borderwidth=3, relief="solid")
        self.oldPassword.config(show="●")
        self.oldPassword.pack(pady=(0, 15))

        # New password input
        Label(self.chgPassWin, text="New password:", font=("Arial", 15, "bold"), bg="#21a6ff").pack(padx=(70, 285))
        self.newPassword1 = Entry(self.chgPassWin, font=("Arial", 25), borderwidth=3, relief="solid")
        self.newPassword1.config(show="●")
        self.newPassword1.pack(pady=(0, 15))

        # New password confirmation input
        Label(self.chgPassWin, text="Confirm new password:", font=("Arial", 15, "bold"), bg="#21a6ff").pack(
            padx=(70, 207))
        self.newPassword2 = Entry(self.chgPassWin, font=("Arial", 25), borderwidth=3, relief="solid")
        self.newPassword2.config(show="●")
        self.newPassword2.pack(pady=(0, 15))

        # Add submit button
        Button(self.chgPassWin, text="submit", font=("Arial", 25), borderwidth=1, relief="solid",
               command=self.submit).pack(pady=(30, 0))

        self.chgPassWin.mainloop()


class Credits:

    def onCreditsClose(self):
        self.creditsBtn.configure(state=ACTIVE)
        self.exitBtn.configure(state=ACTIVE)
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

    def __init__(self, setupWin, accessBtn, exitBtn):
        self.exitBtn = exitBtn
        self.creditsBtn = accessBtn
        self.setupWin = setupWin
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


class Setup:

    def onSetupClose(self):
        pass

    # Open credit window
    def creditsWin(self):
        self.exitBtn.configure(state=DISABLED)
        self.creditBtn.configure(state=DISABLED)
        self.credWin = Credits(self.setupWin, self.creditBtn, self.exitBtn)

    def changePassword(self):
        # Hide window
        self.changePasswordBtn.configure(state=DISABLED)
        self.exitBtn.configure(state=DISABLED)
        ChangePassword(self.localUserData, self.changePasswordBtn, self.exitBtn)

    # Log out user
    def logOut(self):
        self.result[0] = 1
        self.setupWin.destroy()

    # End program
    def exitApp(self):
        self.result[0] = 2
        self.setupWin.destroy()



    def __init__(self, localUserData, result):
        self.chgPassWin = None
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
        self.changePasswordBtn = Button(self.setupWin, text="Change Password", font=("Arial", 20), relief="solid",
                                        borderwidth=3, height=1,
                                        width=30, command=self.changePassword)
        self.changePasswordBtn.pack(pady=10)

        # Add del account button
        Button(self.setupWin, text="Del Account", font=("Arial", 20), relief="solid", borderwidth=3, height=1,
               width=30).pack(pady=10)

        # Add credit button
        self.creditBtn = Button(self.setupWin, text="Credits", font=("Arial", 20), relief="solid", borderwidth=3,
                                height=1,
                                width=30, command=self.creditsWin)
        self.creditBtn.pack(pady=10)

        # Add close app button
        self.exitBtn = Button(self.setupWin, text="Exit app", font=("Arial", 20), relief="solid", borderwidth=3,
                              height=1, width=30,
                              command=self.exitApp)
        self.exitBtn.pack(pady=10)

        # Add launch on pc starting check button
        Checkbutton(self.setupWin, text="Start-up launch", font=("Arial", 20), var=self.startUpLaunch, bg="#21a6ff",
                    activebackground='#21a6ff').pack(side=RIGHT, pady=10, padx=40)

        self.setupWin.mainloop()
