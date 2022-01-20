from tkinter import *
from RegisterWindow import Register
from APICommunication import HttpsRequest

import re


class Login:

    # Check mail address by using regex
    def checkMail(self, mail):
        if len(mail) > 255:
            return False
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(regex, mail):
            return True
        else:
            self.errorMessage.set("Error: Invalid e-mail")
            return False

    # Check and save data entered in username and password entry
    def getUserData(self):
        # Check username
        if not self.checkMail(self.username.get()):
            return
        # Save it
        self.localUserData.setUserID(self.username.get())

        if len(self.password.get()) < 6 or len(self.password.get()) > 255:
            self.errorMessage.set("Error : Invalid password")
            return

        self.localUserData.setUserPassword(self.password.get())

        if self.login():
            self.loginWin.destroy()
            return True

        return False

    def login(self):
        rqt = HttpsRequest()
        res = rqt.login(self.localUserData.getUserID(), self.localUserData.getUserPassword())
        if res[0]:
            # Save token
            self.localUserData.setServerToken(res[1])
            return True
        else:
            # Print error message
            self.errorMessage.set("Error : "+res[1])
            return False

    # Change window for registering
    def register(self):
        # Close window
        self.loginWin.withdraw()

        # Launch register window
        self.registerWin = Register(self.loginWin, self.localUserData)

    def __init__(self, localUserData, errorMessage):
        self.registerWin = None
        self.localUserData = localUserData
        self.loginWin = Tk()
        self.loginWin.title("Login")

        self.errorMessage = StringVar()
        self.errorMessage.set("Error : "+errorMessage)

        self.loginWin.geometry("500x420")
        self.loginWin.configure(bg="#21a6ff")
        self.loginWin.resizable(False, False)

        # Add text to window
        Label(self.loginWin, text="Login", font=("Arial", 40), bg="#21a6ff", pady=20).pack()
        Label(self.loginWin, textvariable=self.errorMessage, font=("Arial", 15, "bold"), bg="#21a6ff", pady=5).pack()

        # Add mail input
        Label(self.registerWin, text="E-mail:", font=("Arial", 15, "bold"), bg="#21a6ff").pack(padx=(35, 330))
        self.username = Entry(self.loginWin, font=("Arial", 25), borderwidth=3, relief="solid")
        self.username.insert(END, self.localUserData.getUserID())
        self.username.pack(pady=(0, 15))

        # Add password input
        Label(self.registerWin, text="Password:", font=("Arial", 15, "bold"), bg="#21a6ff").pack(padx=(45, 305))
        self.password = Entry(self.loginWin, font=("Arial", 25), borderwidth=3, relief="solid")
        self.password.config(show="●")
        self.password.pack(pady=(0, 15))

        # Add login button
        Button(self.loginWin, text="login", font=("Arial", 25), borderwidth=1, relief="solid",
               command=self.getUserData).pack(side=LEFT, pady=20, padx=(140, 20))
        # Add register button
        Button(self.loginWin, text="register", font=("Arial", 20), bg="#21a6ff", relief="flat",
               command=self.register).pack(side=RIGHT, pady=20, padx=(15, 130))

        self.loginWin.mainloop()
