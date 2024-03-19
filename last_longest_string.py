# return length of last word
s = "Hello World"
s = "   fly me   to   the moon  "
s = "luffy is still joyboy"

s = s.strip()
ls = s.split(" ")
print(ls[-1])
