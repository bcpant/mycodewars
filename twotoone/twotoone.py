"""Take 2 strings s1 and s2 including only letters from a to z. 
Return a new sorted string (alphabetical ascending), the longest possible, 
containing distinct letters - each taken only once - coming from s1 or s2.

Examples:
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"""

def longest(a1, a2):
    string = ""
    union = set(a1) | set(a2)
    for c in union:
        string += str(c)
    result = sorted(string)
    string = ""
    for c in result:
        string += str(c)
    return string

print((longest("xyaabbbccccdefww", "xxxxyyyyabklmopq")))

"""

Most popular solution:

def longest(a1, a2):
    return "".join(sorted(set(a1) | (set(a2))))

"""