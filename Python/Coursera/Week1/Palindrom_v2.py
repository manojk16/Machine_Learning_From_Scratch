"""Algorithm2:
1.Device the given string in to two parts
2.If first half is same as reverse of 2nd half then it is Palindrom else not"""
def IsPlaindrom_v2(s):
    n=len(s)
    return s[:n//2]==reverseS(s[n-n//2:])

def reverseS(s):
    rev=''
    for ch in s:
        rev = ch + rev
    return rev
print(IsPlaindrom_v2('AANYA'))
