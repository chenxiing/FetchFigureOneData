# -*- coding: utf-8 -*-

import config

class Login():
    def __init__(self, fetchDirector, parent = None):
        self.fetchDirector = fetchDirector
        self.loginStatus = False

    """登陆"""
    def login(self):
        data = {'f1EmailAddress': config.FIGURE1_USENAME, 'password': config.FIGURE1_PASSWD}
        if self.fetchDirector.submitLoginForm(data):
            self.loginStatus = True
        else:
            self.loginStatus = False

    """获取登陆状态"""
    def getLoginStatus(self):
        return self.loginStatus


