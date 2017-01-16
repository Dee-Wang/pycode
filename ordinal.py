digitals = range(1,101)
for digital in digitals:
	if (digital % 10) == 1:
		print(str(digital)+"st")
	elif (digital % 10) == 2:
		print(str(digital)+"nd")
	else:
		print(str(digital)+"th")

