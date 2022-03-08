import sys
from tkinter import Tk, Label, Button, Entry, END, StringVar, LEFT, RIGHT
from src.loginRegister.RegisterWindow import Register
from src.communication.SocketCommunicationClient import HttpsRequest
import re


class Login:

    # Add close all app on closing window
    @staticmethod
    def onClosing():
        sys.exit(0)

    # Send change password https request
    def forgetPassword(self):
        self.errorMessage.set("")
        if self.username.get() == "":
            self.errorMessage.set("Please fill in the email field")
        rqt = HttpsRequest()
        r = rqt.passwordForget(self.username.get())
        self.errorMessage.set(r[1])
        return

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
            # Save tokens
            self.localUserData.setJwtToken(res[1])
            self.localUserData.setServerToken(res[2]['token'])
            return True
        else:
            # Print error message
            self.errorMessage.set("Error : "+res[1])
            self.errorMessage.set("Error : "+res[1])
            return False

    # Change window for registering
    def register(self):
        # Hide window
        self.loginWin.withdraw()

        # Launch register window
        self.registerWin = Register(self.loginWin, self.localUserData)

    def __init__(self, localUserData, errorMessage):
        self.registerWin = None
        self.localUserData = localUserData
        self.loginWin = Tk()
        self.loginWin.title("Login")

        self.errorMessage = StringVar()
        if not errorMessage == "":
            self.errorMessage.set("Error : "+errorMessage)
        else:
            self.errorMessage.set(errorMessage)

        self.loginWin.geometry("500x480")
        self.loginWin.configure(bg="#21a6ff")
        self.loginWin.resizable(False, False)
        self.loginWin.iconbitmap('pictures/premote.ico')


        # Add action on window close event
        self.loginWin.protocol("WM_DELETE_WINDOW", self.onClosing)

        # Add text to window
        Label(self.loginWin, text="Login", font=("Arial", 40), bg="#21a6ff", pady=20).pack()
        Label(self.loginWin, textvariable=self.errorMessage, font=("Arial", 15, "bold"), bg="#21a6ff", pady=5).pack()

        # Add mail input
        Label(self.registerWin, text="E-mail:", font=("Arial", 15, "bold"), bg="#21a6ff").pack(padx=(35, 330))
        self.username = Entry(self.loginWin, font=("Arial", 25), borderwidth=3, relief="solid")
        if type(self.localUserData.getUserID()) == str:
            print(type(self.localUserData.getUserID()))
            print('Is string')
            self.username.insert(END, self.localUserData.getUserID())
        else:
            print("Is bytecode")
            self.username.insert(END, self.localUserData.getUserID().decode('utf-8'))

        self.username.pack(pady=(0, 15))

        # Add password input
        Label(self.registerWin, text="Password:", font=("Arial", 15, "bold"), bg="#21a6ff").pack(padx=(45, 305))
        self.password = Entry(self.loginWin, font=("Arial", 25), borderwidth=3, relief="solid")
        self.password.config(show="●")
        self.password.pack(pady=(0, 15))

        # Add forget password button
        Button(self.loginWin, text="Password forget", font=("Arial", 15), bg="#21a6ff", relief="flat", command=self.forgetPassword).pack(padx=(230, 15))

        # Add login button
        Button(self.loginWin, text="login", font=("Arial", 25), borderwidth=1, relief="solid",
               command=self.getUserData).pack(side=LEFT, pady=(5, 20), padx=(140, 20))
        # Add register button
        Button(self.loginWin, text="register", font=("Arial", 20), bg="#21a6ff", relief="flat",
               command=self.register).pack(side=RIGHT, pady=(5, 20), padx=(15, 130))

        self.loginWin.mainloop()