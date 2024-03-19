# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.


s = "badc"
t = "baba"

# s = "paper"
# t = "title"

# will loop throught string from 0 to length as length of both the strings are same.
# then we will check if the mapping of the s current element of s exist in s_char_map 
# if not we will check if the mapping of t element exist in t_char_map, if do than return false 



def is_ismophomic_string(s=s, t=t):
	s_char_map = {}
	t_char_map = {}

	for i in range(0, len(s)):
		s_char = s[i]
		t_char = t[i]

		if s_char not in s_char_map and t_char not in t_char_map:
				s_char_map[s_char] = t_char
				t_char_map[t_char] = s_char

		s_mapped = s_char_map.get(s_char, "")

		if t_char != s_mapped:
			return False

	return True

print(is_ismophomic_string())



################
### Best Solution
################

def is_ismophomic_string(s=s, t=t):
	map1 = []
	map2 = []
	for idx in s:
	    map1.append(s.index(idx))
	for idx in t:
	    map2.append(t.index(idx))
	if map1 == map2:
	    return True
	return False

