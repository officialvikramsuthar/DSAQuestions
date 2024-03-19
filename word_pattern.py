# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

# Example 1:

# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
# Example 2:

# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false
# Example 3:

# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false

# pattern = "aaa"
# s = "aa aa aa aa"

pattern = "ab"
s = "happy hacking"

def wordPattern(p=pattern, s=s):

	words, w_to_p = s.split(' '), dict()
	if len(p) != len(words): return False
	if len(set(p)) != len(set(words)): return False # for the case w = ['dog', 'cat'] and p = 'aa'

	for i in range(len(words)):
	    if words[i] not in w_to_p: 
	        w_to_p[words[i]] = p[i]
	    elif w_to_p[words[i]] != p[i]: 
	        return False
	print(w_to_p)
	return True

print(wordPattern())

