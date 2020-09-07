import os,sys,time,datetime,random,hashlib,re,threading,json,requests,mechanize
from urllib.request import urlopen
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
br = Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
try:
    br.open('https://m.facebook.com')
except mechanize.URLError:
    print("\n\x1b[1;96mThere is no internet connection")
print("Done!!")
