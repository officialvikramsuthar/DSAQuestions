
def pow(x, n):
	result = 1

	if n >= 0:
		for i in range(0, n):
			result = result * x
	else: 
		for i in range(0, n, -1):
			result = result / x

	return result

print(pow(2, -3))