# Algorithm 1 :
# # Reverse the given string and compare with the original

def reverseS(s):
    rev=''
    for ch in s:
        rev = ch + rev
    return rev



def is_palindrom_v1(s):
    return s==reverseS(s)

print(is_palindrom_v1('racecar'))
