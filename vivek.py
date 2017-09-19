def number(num):
	for i in range(0,num):
		if i%7==0:
			yield int(i)


num = number(100)
print list(num)