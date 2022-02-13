import os

import requests


class HttpsRequest:

    def __init__(self):
        self.address = "http://pandapp.thrallweb.fr/"

    # Send register request to server
    def register(self, email, password):
        pload = {"email": email, "password": password}
        r = requests.post(self.address + "register", data=pload)
        requestResult = r.json()
        if requestResult['success']:
            print(requestResult['message'])
            return [True, requestResult['token']]
        else:
            print(requestResult['message'])
            return [False, requestResult['message']]

    # Send login request to server
    def login(self, email, password):
        pload = {"email": email, "password": password}
        r = requests.post(self.address + "login", data=pload)
        requestResult = r.json()
        if requestResult['success']:
            print(requestResult['message'])
            return [True, requestResult['token'], requestResult['refreshToken']]
        else:
            print(requestResult['message'])
            return [False, requestResult['message']]

    # Send refresh token request to server
    def refreshToken(self, serverToken):
        pload = {"refreshToken": serverToken}
        r = requests.post(self.address + "refreshToken", data=pload)
        requestResult = r.json()
        if requestResult['success']:
            print("Token refreshed successfully")
            return [True, requestResult['accessToken']]
        else:
            print("Error : Token refresh failed cause of \"" + requestResult['message'] + "\"")
            return [False, requestResult["message"]]

    # Send change password request to server
    def changePassword(self, oldPassword, newPassword, token):
        header = {'x-access-token': token}
        pload = {"oldPassword": oldPassword, "newPassword": newPassword}
        r = requests.post(self.address + "user/changePassword", data=pload, headers=header)
        requestResult = r.json()
        if requestResult['message'] == "Password changed successfully":
            print(requestResult["message"])
            return True
        else:
            print("Error : Password changed failed cause of \"" + requestResult['message'] + "\"")
            return False

    # Send del user account request to server
    def delAccount(self, password, jwt):
        header = {'x-access-token': jwt}
        pload = {"password": password}
        r = requests.post(self.address + "user/deleteAccount", data=pload, headers=header)
        requestResult = r.json()
        if requestResult['message'] == "Account deleted successfully":
            print(requestResult["message"])
            return True
        else:
            print("Error : Account deleted failed cause of \"" + requestResult['message'] + "\"")
            return False

    # Send reset password mail
    def passwordForget(self, mail):
        pload = {"email": mail}
        r = requests.post(self.address + "resetPasswordMail", data=pload)
        requestResult = r.json()
        if requestResult['success']:
            print(requestResult["message"])
            return [True, requestResult["message"]]
        else:
            print("Error : Mail send failed cause of \"" + requestResult['message'] + "\"")
            return [True, "Error : Mail send failed cause of \"" + requestResult['message'] + "\""]

    # Send request to add new device to server
    def addDevice(self, userData):
        header = {'x-access-token': userData.getJwtToken()}
        pload = {"uuid": userData.getToken(), "name": os.environ['COMPUTERNAME']}
        r = requests.post(self.address + "device/add", data=pload, headers=header)
        requestResult = r.json()
        if requestResult["success"]:
            print(requestResult["message"])
            return True
        else:
            print(requestResult["message"])
            return False
