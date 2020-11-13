print("""
***********************
MASTERMIND
***********************
""")
import random 
a = random.randint(10,99)
while True: 
	dogruyer= 0
	yanlısyer =0
	try:
		sayı = int(input("Lütfen tahmininizi giriniz:"))
	except:
		print("Lütfen bir sayı giriniz!!")
		continue
	if sayı not in range(10,99):
		print("Lütfen kriterlere uygun bir sayı giriniz:")
		continue
	else:
		if (sayı%10 == a%10) and (sayı//10 != a//10):
			dogruyer+=1
			yanlısyer+=1
			print("{} basamağı yanlış girdiniz!".format(yanlısyer) )
			continue

		elif (sayı%10 != a%10) and (sayı//10 == a//10):
			dogruyer+=1
			yanlısyer+=1
			print("{} basamağı yanlış girdiniz!".format(yanlısyer) )
			continue

		elif (sayı%10 != a%10) and (sayı//10 != a//10):
			yanlısyer+=2
			print("{} basamağı yanlış girdiniz!".format(yanlısyer) )
			continue

		elif (sayı%10 == a%10) and (sayı//10 == a//10):
			dogruyer+=2
			print("Tebrikler sayıyı doğru girdiniz")
			break






