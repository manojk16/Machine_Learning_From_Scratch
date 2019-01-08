import Palindrom_v1_1
def reverseS(s):
    rev=''
    for ch in s:
        rev = ch + rev
    return rev

def IsPlaindrom_v2(s):
    n=len(s)
    return s[:n//2]==reverseS(s[n-n//2:])
