# -*-coding:utf-8-*-
"""
作者：白浪
日期：2022年03月26日
"""

# -*-coding:utf-8-*-
"""
作者：白浪
日期：2021年07月18日
"""
from push import *
import time
import urllib.request,urllib.error  #制定URL+获取网页数据



def main():
    baseurl = "https://yz.chsi.com.cn/kyzx/kydt/?start=0"     #爬取网址
    askURL(baseurl)


def askURL(url):
    head = {  # 模拟浏览器头部信息，向服务器发送消息
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 86.0.4240.198Safari / 537.36"
    }  # 用户代理——表示告诉服务器，我们是什么类型的机器·浏览器（本质上是告诉浏览器，我们可以接受什么水平的文件内容）

    request = urllib.request.Request(url, headers=head)
    html = ''

    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        print("---正在爬取页面HTML，请稍等---")
        print(html)       #测试：查看电影全部页面HTML

        date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        if date in html:
            push(1)
            print("更新啦")
        else:
            push(0)
            print("未更新")
    except urllib.error.URLError as e:
        if hasattr(e,"code"):       #判断e对象是否包含对应的属性
            e = str(e.code)
            print("爬取失败，e.code" + e)
        if hasattr(e,"reason"):
            e = str(e.reason)
            print("爬取失败，e.reason:" + e)
    return html


if __name__ == "__main__":
    #调用函数
    main()
    print("运行完毕")
