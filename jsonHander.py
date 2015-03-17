# -*- coding: utf-8 -*-

'''Figure1获取到的JSON数据处理'''
class JsonHander():
    def __init__(self, fetchDirector, parent = None):
        self.fetchDirector = fetchDirector
    
    def get(self):
        print '-------' 