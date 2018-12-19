import urllib.request
import re
import os

def open_url(url):
    req=urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134')
    response=urllib.request.urlopen(req)
    html=response.read().decode("utf-8")
    return html

def get_img(html):
    p=r'<img class="BDE_Image".*?src="([^"]*\.jpg)".*?>'
    imglist=re.findall(p,html)
    try:
        os.mkdir("D:/python/NewPics3")
    except FileExistError:
        pass
    os.chdir("D:/python/NewPics3")
    for each in imglist:
        filename=each.split("/")[-1]
        urllib.request.urlretrieve(each,filename,None)

if __name__=='__main__':
    url="https://tieba.baidu.com/p/3823765471"
    get_img(open_url(url))

        
