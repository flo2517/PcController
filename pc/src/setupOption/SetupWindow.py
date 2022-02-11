from tkinter import *
from pc.src.setupOption.ChangePasswordWindow import ChangePassword
from pc.src.setupOption.CreditsWindow import Credits
from pc.src.setupOption.DelAcountWindow import DelAccount


class Setup:

    # Hide window
    def onClosing(self):
        self.setupWin.withdraw()
        pass

    # Show window
    def showWindow(self):
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
        self.result[0] = 1
        self.setupWin.destroy()

    # End program
    def exitApp(self):
        self.result[0] = 2
        self.setupWin.destroy()

    # Del user account
    def delUserAccount(self):
        # Hide window
        self.setupWin.withdraw()
        DelAccount(self.localUserData, self.setupWin, self.result)

    def main(self, win):
        win.visible = True
        while True:
            if self.result[0] == 4:
                self.setupWin.deiconify()
                self.result[0] = 0
            if self.result[0] == 5:
                self.exitApp()

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

        self.setupWin.protocol("WM_DELETE_WINDOW", self.onClosing)

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

        # Add launch on pc starting check button
        Checkbutton(self.setupWin, text="Start-up launch", font=("Arial", 20), var=self.startUpLaunch, bg="#21a6ff",
                    activebackground='#21a6ff').pack(side=RIGHT, pady=10, padx=40)

        self.setupWin.mainloop(self.main)
