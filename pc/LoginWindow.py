from tkinter import *
import re


class Login:

    # Check mail address by using regex
    def checkMail(self, mail):
        if len(mail) > 255 : return False
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(regex, mail):
            return True
        else:
            return False

    # Check and save data entered in username and password entry
    def getUserData(self):
        # Check username
        if not self.checkMail(self.username.get()):
            self.errorMessage.set("Error : Invalid email")
            return
        # Save it
        self.localUserData.setUserID(self.username.get())

        if len(self.password.get()) < 6:
            self.errorMessage.set("Error : Invalid password")
            return

        self.localUserData.setUserPassword(self.password.get())
        self.loginWin.destroy()

    def __init__(self, localUserData, errorMessage):
        self.localUserData = localUserData
        self.loginWin = Tk()
        self.loginWin.title("Login")

        self.errorMessage = StringVar()
        self.errorMessage.set(errorMessage)

        self.loginWin.geometry("500x400")
        self.loginWin.configure(bg="#21a6ff")
        self.loginWin.resizable(False, False)

        # Add text to window
        Label(self.loginWin, text="Login", font=("Arial", 40), bg="#21a6ff", pady=20).pack()
        self.error = Label(self.loginWin, textvariable=self.errorMessage, font=("Arial", 15, "bold"), bg="#21a6ff", pady=5).pack()

        # Add login inputs
        self.username = Entry(self.loginWin, font=("Arial", 25), borderwidth=3, relief="solid")
        if self.localUserData.getUserID() != "[]" and self.localUserData.getUserID() != "":
            self.username.insert(END, self.localUserData.getUserID())
        else:
            self.username.insert(END, "Username")
        self.username.pack(pady=20)
        self.password = Entry(self.loginWin, font=("Arial", 25), borderwidth=3, relief="solid")
        self.password.config(show="*")
        self.password.pack(pady=20)

        # Add login button
        Button(self.loginWin, text="login", font=("Arial", 25), borderwidth=1, relief="solid",
               command=self.getUserData).pack(pady=20)

        self.loginWin.mainloop()
