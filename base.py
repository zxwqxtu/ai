# -*- coding: utf-8 -*-
import json, urllib, urllib2, sys, ssl

class Base:
    token = ''
    ak = 'UV6HyMKwetEZcfkNIdTYKutC'
    sk = 'HumqHaVRETQDUBGb6PQaGQkuKzj7xYY6'

    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    def getToken(self, ak, sk):
        url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s'%(ak, sk)
        response = urllib2.urlopen(url)
        return json.load(response)['access_token']

    def __init__(self):
        self.token = self.getToken(self.ak, self.sk)
