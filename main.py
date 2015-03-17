# -*- coding: utf-8 -*-

import sys
import time

import queryCore
import login
import jsonHander
import db

"""流程控制类"""
class FetchDirector():

    def __init__(self):
        self.login = False
        self.loginTime = None
        self.queryCore = queryCore.QueryCore(self)
        lg = login.Login(self)
        
        print '=============登陆Figure1中。。。==============='
        lg.login()
        
        if not lg.getLoginStatus():
            print '登陆Figure1失败'
            return
        
        print '=============登陆Figure1成功！==============='
        
        
        print '=============获取Figure1数据。。。==========='

        '''fix-me!---这里写循环'''
        self.queryCore.getHomeData(2, 1)
        
        
        print '=============获取Figure1完成。。。==========='
        
        
        print '=============处理JSON数据中。。。 ==========='
        
        print '=============获取JSON数据完成。   ==========='
        
        
            
    """用户登陆，保存信息"""
    def submitLoginForm(self, loginData):
        loginStatus = self.queryCore.login(loginData)
        if loginStatus:
            self.login = True
            self.loginTime = time.time()
            return self.login
        else:
            return False


if __name__ == '__main__':
    FetchDirector()
