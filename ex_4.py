def fib(n):
	if int(n)<=2 :
		return 1
	else:
		return fib(n-1) + fib(n-2)

for i in range(1,31):
	print(fib(i),end=" ")