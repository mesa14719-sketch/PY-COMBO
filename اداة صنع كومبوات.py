
import os,sys,pyfiglet
import random,string


M = '\x1b[38;5;1m'  # أحمر
R = '\x1b[38;5;244m' # رمادي
L = '\x1b[38;5;10m' # اخضر

COLORES = [
	'\x1b[38;5;1m' , # أحمر
	'\x1b[38;5;154m' , # اصفر
	'\x1b[38;5;244m'  # رمادي 
]



logo = pyfiglet.figlet_format(" {{ COMBO }}")

lines  =logo.split("\n")

coloer = ""
for ibra, line in enumerate(lines):
	color = COLORES[ibra % len(COLORES)]
	coloer += color + line + "\n"
print(coloer)
print(f"{M }<{L}•{M}> "*15)


print(
	
	f"{'-'*60} \n"
	f"{M}  (1){R} Gmail.com \n"
	f"{'-'*60} \n"
	f"{M}  (2){R} hotamil.com \n"
	f"{'-'*60} \n"
	f"{M}  (3){R} yopamil.com \n"
	f"{'-'*60} \n"
	f"{M}  (4){R} hi2.in \n"
	f"{'-'*60} \n"
	f"{M}  (5){R} telegmail.com \n"
	f"{'-'*60} \n"
)

choice =input(f"{M}  <{L}•{M}> {M}choice {M} <{L}•{M}>  : {R}")

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

if choice not in  ["1", "2", "3", "4", "5"]:
	print(M+" اختيارك غالط ")
	sys.exit("")

ibr = string.ascii_lowercase + string.digits

G = int(input(f"{M}  <{L}•{M}> {R}How do you want {M}<{L}•{M}> {R}:"))

with open("/storage/emulated/0/Download/email.txt", 'w') as file:
 for _ in range(G):
 	len = random.randint(3,12)
 	username ="".join(random.choice(ibr) for _ in range (len))
 	email = f"{username}@{domain}:{username}\n"
 	file.write(email)
 
print(L+" تم حفظ في ملف اسمه 'email.txt' ")