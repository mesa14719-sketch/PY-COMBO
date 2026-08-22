
import os,sys,pyfiglet
import random,string

RR = '\x1b[38;5;250m'
M = '\x1b[38;5;1m'  # أحمر
R = '\x1b[38;5;244m' # رمادي
L = '\x1b[38;5;10m' # اخضر

COLORES = [
	'\x1b[38;5;1m' , # أحمر
	#'\x1b[38;5;154m' , # اصفر
	'\x1b[38;5;244m'  # رمادي 
]

print(f"{L}-{M}-"*30)
print("")
logo = pyfiglet.figlet_format("  C O M B O O ")

lines  =logo.split("\n")

coloer = ""
for ibra, line in enumerate(lines):
	color = COLORES[ibra % len(COLORES)]
	coloer += color + line + "\n"
print(coloer)
print(f"      {R}Developer : {L}المطور إبراهيم \n")
print(f"	{R}channel : {L}https://t.me/B_R_A_H_I_M_0	\n")

print("")
print(f"{L}-{M}-"*30)


print(
    f"{R}{'┄'*30} \n"
	f"{M}  (1){R} gmail.com \n"
	f"{R}{'┄'*30} \n"
	f"{M}  (2){R} hotamil.com \n"
	f"{'┄'*30} \n"
	f"{M}  (3){R} yopamil.com \n"
	f"{'┄'*30} \n"
	f"{M}  (4){R} hi2.in \n"
	f"{'┄'*30} \n"
	f"{M}  (5){R} telegmail.com \n"
	f"{'┄'*30} \n"
	f"{M}  (6){R} yahoo.com \n"
)

print(f"{L}-{M}-"*30)
print("")
choice =input(f"{M}  <{L}•{M}> {R}choice {M} <{L}•{M}>  :{R}")

if choice == "1":
	domain = "gmail.com"
elif choice == "2":
	domain = "hotamil.com"
elif choice == "3":
	domain = "yopamil.com"
elif choice == "4":
	domain = "hi2.in"
elif choice == "5":
	domain = "telegmail.com"
elif choice == "6":
	domain = "yahoo.com"

if choice not in  ["1", "2", "3", "4", "5", "6"]:
	print(M+" اختيارك غالط ")
	sys.exit("")

ibr = string.ascii_lowercase + string.digits
ibr2 = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890@"


G = int(input(f"{M}  <{L}•{M}> {R}How do you want {M}<{L}•{M}> {R}:"))

with open("/storage/emulated/0/Download/email.txt", 'w') as file:
 for _ in range(G):
 	len1 = random.randint(3,12)
 	len2 = random.randint(3,16)
 	username ="".join(random.choice(ibr) for _ in range (len1))
 	password ="".join(random.choice(ibr2) for _ in range (len2))
 	email = f"{username}@{domain}:{password}\n"
 	file.write(email)
 
print(L+" تم حفظ في ملف اسمه 'email.txt' ")
