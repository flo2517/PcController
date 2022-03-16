import sys
from tkinter import Tk, StringVar, Label, Entry, END, Button, LEFT, RIGHT
from src.communication.SocketCommunicationClient import HttpsRequest
import re


class Register:

    # Add close all app on closing window
    @staticmethod
    def onClosing():
        sys.exit(0)

    # Check mail address by using regex
    def checkMail(self, mail):
        print("Checking mail")
        if len(mail) > 255:
            return False
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(regex, mail):
            return True
        else:
            print("Error: Invalid e-mail")
            self.errorMessage.set("Error: Invalid e-mail")
            return False

    # Check if password and confirmation password as same
    def checkPassword(self, password1, password2):
        print("Checking passwords")
        regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$"

        if len(password1) > 255 or len(password1) < 6:
            print("Error: Invalid size of password")
            self.errorMessage.set("Error: Invalid size of password")
            return False

        if not re.fullmatch(regex, password1):
            print("Error: Password to week")
            self.errorMessage.set("Error: Password to week")
            return False

        if not password1 == password2:
            print("Error: \"Confirm password\" must be the same as \"Password\"")
            self.errorMessage.set("Error: \"Confirm password\" must be the same as \"Password\"")
            return False

        return True

    def register(self):
        rqt = HttpsRequest()
        res = rqt.register(self.localUserData.getUserID(), self.localUserData.getUserPassword())
        if res[0]:
            # Save tokens
            self.localUserData.setJwtToken(res[1])
            self.localUserData.setServerToken(None)
            return True
        else:
            # Print error message
            self.errorMessage.set("Error : "+res[1])
            self.loginWin.deiconify()
            self.registerWin.destroy()
            return False

    def login(self):
        # Close window
        self.registerWin.destroy()

        # Show login window
        self.loginWin.deiconify()

    # Check and save data entered in username and password entry
    def getUserData(self):
        print("Checking data")

        # Check username
        if not self.checkMail(self.username.get()):
            return
        # Save it
        print("Save e-mail")
        self.localUserData.setUserID(self.username.get())

        # Check password validity
        if not self.checkPassword(self.password.get(), self.passwordConf.get()):
            return
        # Save it
        print("Save password")
        self.localUserData.setUserPassword(self.password.get())

        if self.register():
            print("User well registered")
            print("Close register window")
            # Close register window
            self.registerWin.destroy()
            self.loginWin.destroy()
        else:
            return False



    def __init__(self, loginWin, localUserData):
        self.loginWin = loginWin
        self.localUserData = localUserData
        self.registerWin = Tk()
        self.registerWin.title("Register")

        self.errorMessage = StringVar()

        self.registerWin.geometry("500x500")
        self.registerWin.configure(bg="#21a6ff")
        self.registerWin.resizable(False, False)

        # Add action on window close event
        self.registerWin.protocol("WM_DELETE_WINDOW", self.onClosing)

        # Add text to window
        Label(self.registerWin, text="Register", font=("Arial", 40), bg="#21a6ff", pady=15).pack()
        Label(self.registerWin, textvariable=self.errorMessage, font=("Arial", 15, "bold"), bg="#21a6ff", pady=5).pack()

        # Add mail input
        Label(self.registerWin, text="E-mail:", font=("Arial", 15, "bold"), bg="#21a6ff", highlightbackground="#21a6ff").pack(padx=(35, 330))
        self.username = Entry(self.registerWin, font=("Arial", 25), borderwidth=3, relief="solid")
        self.username.insert(END, self.localUserData.getUserID())
        self.username.pack(pady=(0, 15))

        # Add password inputs
        Label(self.registerWin, text="Password:", font=("Arial", 15, "bold"), bg="#21a6ff", highlightbackground="#21a6ff").pack(padx=(45, 305))
        self.password = Entry(self.registerWin, font=("Arial", 25), borderwidth=3, relief="solid")
        self.password.config(show="●")
        self.password.pack(pady=(0, 15))

        # Password confirmation
        Label(self.registerWin, text="Confirm password:", font=("Arial", 15, "bold"), bg="#21a6ff").pack(padx=(45, 227))
        self.passwordConf = Entry(self.registerWin, font=("Arial", 25), borderwidth=3, relief="solid", highlightbackground="#21a6ff")
        self.passwordConf.config(show="●")
        self.passwordConf.pack(pady=(0, 15))

        # Add login button
        Button(self.registerWin, text="login", font=("Arial", 25), activebackground="#21a6ff", bg="#21a6ff", relief="flat",
               command=self.login, highlightbackground="#21a6ff").pack(side=LEFT, pady=20, padx=(140, 20))
        # Add register button
        Button(self.registerWin, text="register", font=("Arial", 20), borderwidth=1, relief="solid",
               command=self.getUserData).pack(side=RIGHT, pady=20, padx=(15, 130))

        self.registerWin.mainloop()