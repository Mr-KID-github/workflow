# -*-coding:utf-8-*-
"""
作者：白浪
日期：2022年03月26日
"""
import requests
import json

def push():
    datas = json.dumps({
                    "appToken":"AT_JoGFbfbWLR3D7n0HaWraUDd92lSIwxBy",
                    "content":"研招网更新了！快去看看是不是你需要的内容！",
                    "contentType": 1,
                    "summary":"研招网更新了!",
                    "uids":["UID_JFMEhBSDqKj7AjaILStgmrDi8kOb"],
                    "url":"https://yz.chsi.com.cn/kyzx/kydt/?start=0"
                })
    headers = {'Content-Type': 'application/json'}
    r = requests.post("http://wxpusher.zjiecode.com/api/send/message", data=datas,headers=headers)
    print(r.text)
    print(r.status_code)