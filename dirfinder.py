#created by WhiteRaven

#needes modules
import sys
import requests
import threading

#banner
def banner():
	print('''\033[1;32;40m


 /$$$$$$$  /$$           /$$$$$$$$ /$$                 /$$                    
| $$__  $$|__/          | $$_____/|__/                | $$                    
| $$  \ $$ /$$  /$$$$$$ | $$       /$$ /$$$$$$$   /$$$$$$$  /$$$$$$   /$$$$$$ 
| $$  | $$| $$ /$$__  $$| $$$$$   | $$| $$__  $$ /$$__  $$ /$$__  $$ /$$__  $$
| $$  | $$| $$| $$  \__/| $$__/   | $$| $$  \ $$| $$  | $$| $$$$$$$$| $$  \__/
| $$  | $$| $$| $$      | $$      | $$| $$  | $$| $$  | $$| $$_____/| $$      
| $$$$$$$/| $$| $$      | $$      | $$| $$  | $$|  $$$$$$$|  $$$$$$$| $$      
|_______/ |__/|__/      |__/      |__/|__/  |__/ \_______/ \_______/|__/                                                                                  
       						   created by WhiteRaven



       ''')
	
	
#function to help people
def help():
		print("\n\n\t\tType: python3 dirfinder.py -u [URL] -f [wordlist file]\n\n")
		print("\n\n\t\tEXAMPLE: python3 dirfinder.py -u www.target.com -f wordlist.txt\n\n")
		exit()
#the main functio 		
def main():
	url=sys.argv[2]  #target url
	file=sys.argv[4] #wordlist file path
	#colores
	green="\033[1;32;40m"
	red="\033[1;31;40m"
	greenbg="\33[42m"
	cyan="\033[36m"
	
	print("\n\033[33mTARGET:",url)
	print("\033[33mWORDLIST:",file,"\n")
	#open file
	try:
			getfile=open(file)
	except FileNotFoundError:
			print(red,"\n\n[-]FILE NOT FOUND!!!!\n\n")
			exit()
	readfile=getfile.read()
	dirs=readfile.splitlines()
	num=1
	#bruteforce directories
	for dir in dirs:
			editedUrl=(f"{url}/{dir}")
			try:
				print(red,"TRYING:",editedUrl, end="\r")
				getResp=requests.get(editedUrl)
				#code 200
				if getResp.status_code==200:
					print(f"{green}FOUND[{getResp.status_code}]      :   {editedUrl}")
			except requests.exceptions.ConnectionError:
				print("NO ADDRESS ASSOCIATED WITH HOST NAME !!!!")
				help()
				exit()
				
#main()
if __name__=="__main__":
	  banner()
	  try:
	  	main()
	  except IndexError:
	  	help()
	  	exit()
			
