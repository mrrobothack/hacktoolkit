import os

os.system("clear")


banner="""


                                                                ______
                                                             .-"      "-.	
                                                            /            \	
   __  __   ___   ___    ___    ___    ___    _____        |              |	
  |  \/  | | _ \ | _ \  / _ \  | _ )  / _ \  |_   _|       |,  .-.  .-.  ,|
  | |\/| | |   / |   / | (_) | | _ \ | (_) |   | |         | )(__/  \__)( |
  | |\/| | |   / |   / | (_) | | _ \ | (_) |   | |         |/     /\     \|
  |_|  |_| |_|_\ |_|_\  \___/  |___/  \___/    |_|         (_     ^^     _)
  .:.:. Every System is Insecure! Don't Forget! .:.:.       \__|IIIIII|__/
                                                             | \IIIIII/ |
                                                             \          /
                                                              `--------`
"""
print(banner)
print("""
1]Linux Update
2]Hack Tool Kit Update
-----Phishing-----
3]Blackeye
4]Shellphish
5]Aircrack-ng
6]Exit""")
girdi=input("------>")

if (girdi==2):
	os.system("cd .. && git clone https://github.com/mrrobothack/hacktoolkit.git")


if (girdi==3):
	os.system("clear")
	print(banner)
	print("""
1111]Kur
2222]Devam Et""")
girdi72=input("------>")
if (girdi72==1111):
	os.system("clear && git clone https://github.com/thelinuxchoice/blackeye.git && exit")
if (girdi72==2222):
	os.system("clear && cd blackeye && bash blackeye.sh")


if (girdi==5):
	os.system("exit")

if (girdi==4):
	os.system("clear")
	print(banner)
	print("""
11111]Kur
22222]Devam Et""")
girdi74=input("------>")
if (girdi74==11111):
	os.system("clear && git clone https://github.com/thelinuxchoice/shellphish.git && exit")
if (girdi74==22222):
	os.system("clear && cd shellphish && bash shellphish.sh")


if (girdi==6):
	os.system("exit")


if (girdi==1):
	os.system("clear")
	print(banner)
	print("""
11]apt-get update
22]apt-get upgrade
33]apt-get dist-upgrade""")
girdii=input("------>")
if (girdii==11):
	os.system("sudo apt-get update")
if (girdii==22):
	os.system("sudo apt-get upgrade")
if (girdii==33):
	os.system("sudo apt-get dist-upgrade")






