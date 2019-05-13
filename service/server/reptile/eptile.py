import requests
from bs4 import BeautifulSoup
import time
import re

def getLink():
    # 请求路径
    url = 'https://www.zhihu.com/topic/19550517/hot'
    # http://cwiki.apachecn.org/
    # 请求头http://www.dytt8.net/html/gndy/dyzz/index.html
    # 鲁迅说过的话http://cx.luxunmuseum.com.cn/ALLfINDlX35.ASPX?ybiaozhi=1
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'
    }
    # 假装我是浏览器
    response = requests.get(url, headers=header)
    # 乱码问题
    html_doc = response.content.decode('utf8')
    # 解析器   默认html.parse
    soup = BeautifulSoup(html_doc, 'lxml')
    links = []
    download_link = []
    for a in soup.select('.ContentItem-title'):
        # pattern = re.compile(r'\s|\n|<.*?>|.*?《|》.*?', re.S)
        pattern = re.compile(r'\s|\n|<.*?>',re.S)
        a = pattern.sub('', str(a))
        print(a)
        download_link.append(a)
        # print(a.text())
        # href = 'http://www.dytt8.net'+a['href']
        # print(href)
        # title = a.string
        # print(title)
        # links.append(href)  #添加电影链接到列表
    # for link in links:      #添加电影链接到列表
    #     response = requests.get(link)
    #     html_doc = response.content.decode('gbk')
    #     soup = BeautifulSoup(html_doc,'lxml')
    #     ftp = soup.select('#Zoom tbody a')[0]     #select查找方法   形象的比喻 扒衣服的操作，一层一层
    #     download_link.append(ftp['href'])  #获取电影的迅雷链接
        # time.sleep(5)
    return download_link