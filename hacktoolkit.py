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
3]Phishing
4]Aircrack-ng
5]Exit""")
girdi=input("------>")

if (girdi==2):
	os.system("git clone https://github.com/mrrobothack/hacktoolkit.git")
if (girdi==3):
	os.system("exit")
if (girdi==4):
	os.system("exit")
if (girdi==5):
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



