from tkinter import *


class Setup:

    # Log out user
    def logOut(self):
        self.result[0] = 1
        self.setupWin.destroy()

    def __init__(self, localUserData, result):
        self.result = result
        self.localUserData = localUserData
        self.setupWin = Tk()
        self.setupWin.title("Setup")

        self.setupWin.geometry("650x550")
        self.setupWin.configure(bg="#21a6ff")
        self.setupWin.resizable(False, False)

        self.startUpLaunch = False

        Label(self.setupWin, text="Setup", font=("Arial", 40), bg="#21a6ff", pady=20).pack()

        # Add log out button
        Button(self.setupWin, text="Log Out", font=("Arial", 20), relief="solid", borderwidth=3, height=1, width=30, command=self.logOut).pack(pady=20)

        # Add change password button
        Button(self.setupWin, text="Change Password", font=("Arial", 20), relief="solid", borderwidth=3, height=1, width=30).pack(pady=10)

        # Add del account button
        Button(self.setupWin, text="Del Account", font=("Arial", 20), relief="solid", borderwidth=3, height=1, width=30).pack(pady=10)

        # Add credit button
        Button(self.setupWin, text="Credit", font=("Arial", 20), relief="solid", borderwidth=3, height=1, width=30).pack(pady=10)

        # Add launch on pc starting check button
        Checkbutton(self.setupWin, text="Start-up launch", font=("Arial", 20), var=self.startUpLaunch, bg="#21a6ff", activebackground='#21a6ff').pack(side=RIGHT, pady=10, padx=40)



        self.setupWin.mainloop()
