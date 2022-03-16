from tkinter import Tk, Button, Label, DISABLED, PhotoImage
from src.setupOption.ChangePasswordWindow import ChangePassword
from src.setupOption.CreditsWindow import Credits
from src.setupOption.DelAcountWindow import DelAccount


class Setup:

    # Hide window
    def onClosing(self):
        pass

    # Open credit window
    def creditsWin(self):
        self.exitBtn.configure(state=DISABLED)
        self.creditBtn.configure(state=DISABLED)
        self.credWin = Credits(self.setupWin, self.creditBtn, self.exitBtn)

    def changePassword(self):
        # Hide window
        self.setupWin.withdraw()
        ChangePassword(self.localUserData, self.setupWin)

    # Log out user
    def logOut(self):
        self.restart = True
        self.setupWin.destroy()

    # End program
    def exitApp(self):
        self.restart = False
        self.setupWin.destroy()

    # Del user account
    def delUserAccount(self):
        # Hide window
        self.setupWin.withdraw()
        self.restart = True
        DelAccount(self.localUserData, self.setupWin)

    def addButton(self):
        # Add log out button
        Button(self.setupWin, text="Log Out", font=("Arial", 20), relief="solid", borderwidth=3, height=1, width=30,
               command=self.logOut).pack(pady=20)

        # Add change password button
        self.changePasswordBtn = Button(self.setupWin, text="Change Password", font=("Arial", 20), relief="solid",
                                        borderwidth=3, height=1,
                                        width=30, command=self.changePassword)
        self.changePasswordBtn.pack(pady=10)

        # Add del account button
        self.delAccountBtn = Button(self.setupWin, text="Del Account", font=("Arial", 20), relief="solid",
                                    borderwidth=3,
                                    height=1,
                                    width=30, command=self.delUserAccount)
        self.delAccountBtn.pack(pady=10)

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

    def showWin(self):
        self.icon.stop()
        self.setupWin.deiconify()

    def getEndResult(self):
        return self.restart

    def __init__(self, localUserData):
        self.icon = None
        self.exitBtn = None
        self.creditBtn = None
        self.delAccountBtn = None
        self.changePasswordBtn = None
        self.chgPassWin = None
        self.credWin = None

        self.restart = False
        self.localUserData = localUserData
        self.setupWin = Tk()

        self.setupWin.title("Setup")
        self.setupWin.geometry("750x600")
        self.setupWin.configure(bg="#21a6ff")
        self.setupWin.resizable(False, False)

        self.setupWin.protocol("WM_DELETE_WINDOW", self.onClosing)

        Label(self.setupWin, text="Setup", font=("Arial", 40), bg="#21a6ff", pady=20).pack()

        # Add all buttons
        self.addButton()

        self.setupWin.mainloop()
