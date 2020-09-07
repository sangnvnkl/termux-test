import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
def keluar():
	print "\x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')
    
def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.07)
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)

back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')		
	except (KeyError,IOError):
		os.system('clear')
		jalan('   Note: Use a New Account To Login' )
		print('	  	LOGIN WITH FACEBOOK' )
		print('	' )
		id = raw_input('ID/Email: ')
		pwd = raw_input('Password: ')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"There is no internet connection"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		print url
# 		if 'save-device' in url:
# 			try:
# 				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
# 				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
# 				x=hashlib.new("md5")
# 				x.update(sig)
# 				a=x.hexdigest()
# 				data.update({'sig':a})
# 				url = "https://api.facebook.com/restserver.php"
# 				r=requests.get(url,params=data)
# 				z=json.loads(r.text)
# 				unikers = open("login.txt", 'w')
# 				unikers.write(z['access_token'])
# 				unikers.close()
# 				print '\n\x1b[1;95mLogin Successful...'
# 				toket = open('login.txt','r')				
# 			except requests.exceptions.ConnectionError:
# 				print"\n\x1b[1;91mThere is no internet connection"
# 				keluar()
# 		if 'checkpoint' in url:
# 			print("\n\x1b[1;91mYour Account is on Checkpoint")
# 			os.system('rm -rf login.txt')
# 			time.sleep(1)
# 			keluar()
# 		else:
# 			print("\n\x1b[1;93mPassword/Email is wrong")
# 			os.system('rm -rf login.txt')
# 			time.sleep(1)
# 			login()
login()
print toket
