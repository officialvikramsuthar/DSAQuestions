haystack = "mississippi"
needle = "issip"

n_pointer = 0
h_pointer = 0
h_length = len(haystack)
n_length = len(needle)
temp_pointer = n_pointer + h_pointer

while n_pointer < n_length and temp_pointer < h_length and n_length <= h_length:
    
    if haystack[temp_pointer] == needle[n_pointer]:
        n_pointer += 1
    else:
        h_pointer +=1
        n_pointer = 0

    temp_pointer = h_pointer + n_pointer
if n_pointer == n_length:
    print(h_pointer)
