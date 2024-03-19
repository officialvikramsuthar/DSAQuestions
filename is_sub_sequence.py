t = "ahbgdc"
s = "abc"
t_index = 0 
s_index = 0 
s_length = len(s)
t_length = len(t)

while s_index < s_length and t_index < t_length:
	
	if s[s_index] == t[t_index]:
		s_index += 1
		t_index += 1
	else:
		t_index += 1


if s_length == s_index:
	return True
else:
	return False 