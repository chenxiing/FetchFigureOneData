# -*- coding: utf-8 -*-

import cookielib
import urllib2
import urllib
import httplib
import urlparse


'''网络数据查询实现类，负责网络数据交互，包括登陆和JSON数据获取'''
class QueryCore():
    def __init__(self, ctr):
        self.ctr = ctr
        self.setCookies()

    """ 设置cookie"""
    def setCookies(self):   
        self.cookieFile = "cookies.txt"
        self.cookies = cookielib.MozillaCookieJar(self.cookieFile)
        
        try:
            self.cookies.load(ignore_discard = True, ignore_expires = True)
        except Exception:
            self.saveCookie()

        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies))
        urllib2.install_opener(self.opener)

        try:
            response = self.opener.open(urllib2.Request('https://app.figure1.com'))
            response.read()
        except:
            pass
        self.saveCookie()

    """保存cookie"""
    def saveCookie(self):
        self.cookies.save(self.cookieFile, ignore_discard = True, ignore_expires = True)

    """获得全部cookie数据"""
    def readAllCookie(self):
        cookieMap = {}
        if self.cookies is not None:
            for cookie in self.cookies:
                one = cookie.name + '=' + str(cookie.value) + ('; expires=' + str(cookie.expires) if cookie.expires is not None else '' ) + '; domain=' + str(cookie.domain) + '; path=' + str(cookie.path)
                cookieMap.update({cookie.name: one})
        return cookieMap

    """更新cookie"""
    def updateCookie(self):
        self.saveCookie()
        self.cookies.load(ignore_discard = True, ignore_expires = True)
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies))
        urllib2.install_opener(self.opener)
        
    '''异步登陆Figure1，实际上直接用login就行了'''
    def loginAync(self, postData):
        def run(self, postData):
            try:
                url = 'https://app.figure1.com/login'
                req = urllib2.Request(url, urllib.urlencode(postData))
                
                req.add_header('Host', 'app.figure1.com')
                req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36')
                req.add_header('Referer', 'https://app.figure1.com/login')
                req.add_header('Connection', 'keep-alive')
                req.add_header('X-Requested-With', 'XMLHttpRequest')
                req.add_header('Content-Type', 'application/x-www-form-urlencoded')
                
                response = urllib2.urlopen(req)
                #print response.read()
                
                return {'s': True, 'r': response.read()}
            except:
                return {'s': False, 'r': ''}

        re = run(self, postData)

        while not re['s']:
            re = run(self, postData)

        ''' fix-me! 这里还要对返回的re['r']做处理，判断是否登陆成功，由于本程序有特定用途，这里就不做太多判断了。'''
        return True

    """用户登陆，返回登陆状态码"""
    def login(self, loginData):
        if self.loginAync(loginData):
            try:
                '''
                url = "https://app.figure1.com/login"
                req = urllib2.Request(url, urllib.urlencode(loginData))
                
                req.add_header('Host', 'app.figure1.com')
                req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36')
                req.add_header('Referer', 'https://app.figure1.com/login')
                req.add_header('Connection', 'keep-alive')
                req.add_header('X-Requested-With', 'XMLHttpRequest')
                req.add_header('Content-Type', 'application/x-www-form-urlencoded')
                
                response = urllib2.urlopen(req)
                '''
            except:
                return False

            return True
        else:
            return False


    '''获取Figure1首页JSON。pageSize为每页面显示数据条数，skip为页码。目前数据量为16500左右。'''
    def getHomeData(self, pageSize, skip):
        def run(self):
            try:
                url = 'https://app.figure1.com/s/feeds/home?pageSize=' + str(pageSize) + '&skip=' + str(skip)
                req = urllib2.Request(url)
                req.add_header('Host', 'app.figure1.com')
                req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36')
                req.add_header('Referer', 'https://app.figure1.com/login')
                req.add_header('Connection', 'keep-alive')
                req.add_header('X-Requested-With', 'XMLHttpRequest')
                req.add_header('Content-Type', 'application/x-www-form-urlencoded')

                response = urllib2.urlopen(req)
                #self.updateCookie()
                print response.read()
                
                return {'s': True, 'r': response.read().decode()}
            except:
                return {'s': False, 'r': ''}

        re = run(self)

        while not re['s']:
            re = run(self)

        return True

