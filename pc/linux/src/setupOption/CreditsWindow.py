from tkinter import Tk, Canvas, ACTIVE, SE, Text, font
from PIL import Image, ImageTk
import os.path


class Credits:

    def onClosing(self):
        self.creditsBtn.configure(state=ACTIVE)
        self.exitBtn.configure(state=ACTIVE)
        self.credWin.destroy()

    # Display the beautiful and too cute little panda at the bottom of the credit window
    def displayCutePanda(self):
        path = '/home/pandapp/Documents/DEV/Pandapp/pc/pictures/pandapp_white.png'
        # Check file existence
        if os.path.exists(path):
            panda = Canvas(self.credWin, bg="#aaaaaa", bd=0, highlightthickness=0, relief="ridge")

            # Load and resize picture
            img = Image.open(path)
            img = img.resize((70, 70))
            img = ImageTk.PhotoImage(master=self.credWin, image=img)

            # Place picture
            panda.create_image(380, 70, anchor=SE, image=img)

            # Display canvas
            panda.pack()
            panda.mainloop()
            return
        else:
            print('Picture not found')
            return

    def __init__(self, setupWin, accessBtn, exitBtn):
        self.exitBtn = exitBtn
        self.creditsBtn = accessBtn
        self.setupWin = setupWin
        self.credWin = Tk()
        self.credWin.title("Credits")
        self.credWin.geometry("550x400")
        self.credWin.configure(bg="#aaaaaa")
        self.credWin.resizable(False, False)
        myfont = font.Font(family='Arial')

        self.credWin.protocol("WM_DELETE_WINDOW", self.onClosing)

        creditText = "Welcome to Pandapp,\n\nThis is our end-of-licence project at the \ncomputer science university of Besançon.\n\nUnder the supervision of our teachers Mrs. \nFelea and Mr. Merlet, this project was \ncarried out by Laura Bobillier, Florian \nJeandenans and Maxime Caron.\n\nThank you for using our app !\n\n\nWe especially thank the Stackoverflow \ncommunity as well as the Indian youtube \nchannels for their precious help."

        textArea = Text(self.credWin, state='normal', padx=50, pady=10, bd=0, highlightthickness=0, relief="ridge")
        textArea.insert('end', creditText)
        textArea.configure(state='disabled', bg="#aaaaaa", font=("Arial", 12, 'bold'), width=100, height=17)
        textArea.pack()

        self.displayCutePanda()

        self.credWin.mainloop()