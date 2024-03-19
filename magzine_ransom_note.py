ransomNote = "aa"
magzineNote = "aab"

def checkRansomeNote(ransomNote=ransomNote, magzineNote=magzineNote):
	magzineDict = {}

	for el in magzineNote:
		value = magzineDict.get(el, 0)
		value += 1
		magzineDict[el] = value

	for el in ransomNote:
		value = magzineDict.get(el, -1)
		if value <= 0:
			return False

		value -= 1
		magzineDict[el] = value

	return True

print(checkRansomeNote())