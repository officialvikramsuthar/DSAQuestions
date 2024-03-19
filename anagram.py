s = "rat"
t = "car"
letter_dict = {}
t_dict = {}

for i in s:
	value = letter_dict.get(i, 0)
	letter_dict[i] = value + 1

for i in t:
	value = t_dict.get(i, 0)
	t_dict[i] = value + 1

	
print(letter_dict == t_dict)

