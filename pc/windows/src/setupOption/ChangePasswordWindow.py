import re
from src.communication.SocketCommunicationClient import HttpsRequest
from tkinter import Tk, Button, Entry, Label


class ChangePassword:
    # Add show setup window at closing window
    def onClosing(self):
        self.setupWin.deiconify()
        self.chgPassWin.destroy()

    # Check if old password is correct
    def checkOldPassword(self):
        if not self.oldPassword.get() == self.userData.getUserPassword():
            print("Error: Old password is incorrect")
            return False
        return True

    # Check validity of new password
    def checkNewPassword(self):
        print("Checking new passwords")
        regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$"

        if len(self.newPassword1.get()) > 255 or len(self.newPassword1.get()) < 6:
            print("Error: Invalid size of password")
            return False

        if self.oldPassword.get() == self.newPassword1.get():
            print("Error : New password need to be different as old password")
            return False

        if not re.fullmatch(regex, self.newPassword1.get()):
            print("Error: Password to week")
            return False

        if not self.newPassword1.get() == self.newPassword2.get():
            print("Error: \"Confirm new password\" must be the same as \"New Password\"")
            return False

        return True

    # Send change password request to server
    def sendRequest(self):
        res = self.rqt.changePassword(self.oldPassword.get(), self.newPassword1.get(), self.userData.getJwtToken())
        return res

    # Check data and send request to server
    def submit(self):
        print("Checking old password")
        if not self.checkOldPassword():
            return False

        print("Checking new password")
        if not self.checkNewPassword():
            return False

        print('submit')
        if not self.sendRequest():
            return False

        # Show setup window
        self.setupWin.deiconify()
        self.chgPassWin.destroy()

    def __init__(self, userData, setupWin):
        self.rqt = HttpsRequest()
        self.userData = userData
        self.setupWin = setupWin
        self.chgPassWin = Tk()
        self.chgPassWin.title('Change Password')
        self.chgPassWin.geometry("500x500")
        self.chgPassWin.configure(bg="#21a6ff")
        self.chgPassWin.resizable(False, False)
        self.chgPassWin.iconbitmap('pictures/premote.ico')

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