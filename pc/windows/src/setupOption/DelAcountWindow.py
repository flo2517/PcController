from src.communication.SocketCommunicationClient import HttpsRequest
from tkinter import Tk, Label, Button, LEFT, RIGHT


class DelAccount:
    # Add show setup window at closing window
    def onClosing(self):
        self.setupWin.deiconify()
        self.delUserWin.destroy()

    # Send delete account request to server and close or show setup window
    def request(self):
        res = self.rqt.delAccount(self.userData.getUserPassword(), self.userData.getJwtToken())
        if res:
            self.setupWin.destroy()
            self.delUserWin.destroy()
        else:
            self.setupWin.deiconify()
            self.delUserWin.destroy()

    def __init__(self, userData, setupWin):
        self.rqt = HttpsRequest()
        self.userData = userData
        self.setupWin = setupWin
        self.delUserWin = Tk()
        self.delUserWin.title('Delete Account')
        self.delUserWin.geometry("500x250")
        self.delUserWin.configure(bg="#21a6ff")
        self.delUserWin.resizable(False, False)
        self.delUserWin.iconbitmap('../pictures/pandapp.ico')

        # Add action on window close event
        self.delUserWin.protocol("WM_DELETE_WINDOW", self.onClosing)

        # Add text to window
        Label(self.delUserWin, text="Do you really want to delete this account ?", font=("Arial", 18),
              bg="#21a6ff").pack(pady=(50, 0))

        # Add confirm button
        Button(self.delUserWin, text="Confirm", font=("Arial", 25), borderwidth=1, relief="solid",
               command=self.request).pack(side=LEFT, pady=20, padx=(90, 20))

        # Add abandon button
        Button(self.delUserWin, text="Abandon", font=("Arial", 25), borderwidth=1, relief="solid",
               command=self.onClosing).pack(side=RIGHT, pady=20, padx=(15, 90))

        self.delUserWin.mainloop()