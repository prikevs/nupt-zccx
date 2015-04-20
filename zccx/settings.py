#coding:utf-8
HOST = "localhost"
USER = "****"
PASSWD = "****"
DBNAME = "zccx"
TABLE = "user"

INIT_URL = "http://zccx.tyb.njupt.edu.cn"
INFO_URL = "http://zccx.tyb.njupt.edu.cn/student"

HEAD = { 
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/41.0.2272.76 Chrome/41.0.2272.76 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'Origin': 'http://zccx.tyb.njupt.edu.cn',
    'Referer': 'http://zccx.tyb.njupt.edu.cn/'
}


FNAME_A = 'authenticityToken' 
FNAME_B = 'number'
FNAME_C = 'name'

CODE_OK = 0
CODE_FOP = 1    #"""failed to open, the website unreachable""" 
CODE_WRONG = 2  #"""wrong name or stu_id"""
CODE_UNBIND = 3 #"""unbind"""

RE_TOKEN = r'name="authenticityToken" value="(.+?)"'
RE_TIMES = r'<span class="badge">(\d+?)</span>'
RE_AN = r'(\d+?)年(\d+?)月(\d+?)日</td>'

