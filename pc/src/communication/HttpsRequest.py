import requests


class HttpsRequest:

    def __init__(self):
        # self.address = "http://thrallweb.fr:8080/"
        self.address = "laurahost.fr:8080/"

    # Send register request to server
    def register(self, email, password):
        pload = {"email": email, "username": "johndoe", "password": password}
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
            return [True, requestResult['refreshToken']['token']]
        else:
            print("Error : Token refresh failed cause of \"" + requestResult['message'] + "\"")
            return [False, requestResult["message"]]

    # Send change password request to server
    def changePassword(self, oldPassword, newPassword):
        pload = {"oldPassword": oldPassword, "newPassword": newPassword}
        r = requests.post(self.address + "user/changePassword", data=pload)
        requestResult = r.json()
        if requestResult['message'] == "Password changed successfully":
            print(requestResult["message"])
            return True
        else:
            print("Error : Password changed failed cause of \"" + requestResult['message'] + "\"")
            return False

    # Send del user account request to server
    def delAccount(self, password):
        pload = {"password": password}
        r = requests.post(self.address + "user/deleteAccount", data=pload)
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
            return True
        else:
            print("Error : Account deleted failed cause of \"" + requestResult['message'] + "\"")
            return False
