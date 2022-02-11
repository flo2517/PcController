import sys
import pystray
from pystray import MenuItem as item
from PIL import Image


class Icon:

    def showWin(self):
        self.setupWin[0] = 4

    def closeIcon(self):
        self.setupWin[0] = 5
        self.icon.stop()

    def main(self, icon):
        icon.visible = True
        while True:
            if self.shmIcon[0] == 1:
                #print('Closing icon')
                icon.stop()

    def __init__(self, shmSetupWin, shmIcon):
        self.setupWin = shmSetupWin
        self.shmIcon = shmIcon

        path = 'pictures/panda.png'
        img = Image.open(path)

        menu = (item('Show Window', self.showWin), item('Exit', self.closeIcon))

        icon = pystray.Icon("PcController", img, "PcController", menu=menu)
        self.icon = icon
        icon.run(self.main)
        print('test')
