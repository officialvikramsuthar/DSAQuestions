# Input: s = "the sky is blue"
# Output: "blue is sky the"

# Input: s = "  hello world  "
# Output: "world hello"

# Input: s = "a good   example"
# Output: "example good a"

s = "a good   example"
result = ""
word = ""

s = s.strip()

for index, el in enumerate(s):
	if el.strip() != "":
		word += el

	elif word != "":
		
		result = " " + word + result
		word = ""

result = word + result

print("world hello" == result)

print(result)
