import requests
import os

def urldownload(url,filename=None):
    """
    下载文件到指定目录
    :param url: 文件下载的url
    :param filename: 要存放的目录及文件名，例如：./test.xls
    :return:
    """
    down_res = requests.get(url)
    with open(filename,'wb') as file:
        print(down_res.content)
        file.write(down_res.content)


save_list = [
    'http://localhost:3000/users/1/web_requests/9/github-trending-rss.xml',
    'http://localhost:3000/users/1/web_requests/12/v2ex-creating-rss.xml',
    'http://localhost:3000/users/1/web_requests/14/w2solo-rss.xml',
    'http://localhost:3000/users/1/web_requests/16/Indie-Hackers-Popular-rss.xml'
]

# 下载列表中的rss文件
for url in save_list:
    filename = url.split('/')[-1]
    urldownload(url, 'rss/' + filename)
    print(filename + ' download succuess!')

# 提交 git
os.system("auto-push.sh")
# os.system("git commit -m 'auto update'")
# os.system("git push")
# 求两个数中的最大值
# def max(a,b):
#     if a > b:
#         return a
#     else:
#         return b

print('auto push success')