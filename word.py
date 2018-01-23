# -*- coding: utf-8 -*-
import json, urllib, urllib2, base64
from base import Base

class Ai(Base):
    def getGeneralWord(self, data):
        url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token=%s"%self.token
        print url
        req = urllib2.urlopen(url, urllib.urlencode(data))
        return req.read()



if __name__ == '__main__':
    params = {
        'url': 'http://haijia.bjxueche.net/images/logo.png',
        #'url': 'https://www.baidu.com/img/bd_logo1.png',
        'detect_direction': "true",
        "language_type": "CHN_ENG",
        "detect_language": 'true',
        'probability': 'true'
    }

    print Ai().getGeneralWord(params)
