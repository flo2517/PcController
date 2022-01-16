from tkinter import *
import re


class Register:

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
        if len(password1) > 255 or len(password1) < 6:
            print("Error: Invalid size of password")
            self.errorMessage.set("Error: Invalid size of password")
            return False

        if not password1 == password2:
            print("Error: \"Confirm password\" must be the same as \"Password\"")
            self.errorMessage.set("Error: \"Confirm password\" must be the same as \"Password\"")
            return False

        return True

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

        print("Close register window")
        self.registerWin.destroy()

    def __init__(self, localUserData, errorMessage):
        self.localUserData = localUserData
        self.registerWin = Tk()
        self.registerWin.title("Register")

        self.errorMessage = StringVar()
        self.errorMessage.set(errorMessage)

        self.registerWin.geometry("500x500")
        self.registerWin.configure(bg="#21a6ff")
        self.registerWin.resizable(False, False)

        # Add text to window
        Label(self.registerWin, text="Register", font=("Arial", 40), bg="#21a6ff", pady=15).pack()
        Label(self.registerWin, textvariable=self.errorMessage, font=("Arial", 15, "bold"), bg="#21a6ff", pady=5).pack()

        # Add mail input
        Label(self.registerWin, text="E-mail:", font=("Arial", 15, "bold"), bg="#21a6ff").pack(padx=(35, 330))
        self.username = Entry(self.registerWin, font=("Arial", 25), borderwidth=3, relief="solid")
        if self.localUserData.getUserID() != "[]" and self.localUserData.getUserID() != "":
            self.username.insert(END, self.localUserData.getUserID())
        self.username.pack(pady=(0, 15))

        # Add password inputs
        Label(self.registerWin, text="Password:", font=("Arial", 15, "bold"), bg="#21a6ff").pack(padx=(45, 305))
        self.password = Entry(self.registerWin, font=("Arial", 25), borderwidth=3, relief="solid")
        self.password.config(show="●")
        self.password.pack(pady=(0, 15))

        # Password confirmation
        Label(self.registerWin, text="Confirm password:", font=("Arial", 15, "bold"), bg="#21a6ff").pack(padx=(45, 227))
        self.passwordConf = Entry(self.registerWin, font=("Arial", 25), borderwidth=3, relief="solid")
        self.passwordConf.config(show="●")
        self.passwordConf.pack(pady=(0, 15))

        # Add register button
        Button(self.registerWin, text="register", font=("Arial", 20), borderwidth=1, relief="solid",
               command=self.getUserData).pack(padx=20)

        self.registerWin.mainloop()
