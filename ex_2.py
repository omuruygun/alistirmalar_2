def toplam(i):
	if i == 1 :
		return 1
	else:
		return i + toplam(i-1)

print(toplam(9))
