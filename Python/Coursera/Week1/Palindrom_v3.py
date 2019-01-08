s=input('Enter The word\n')
#j=len(s)-1
def Panlindron_v3(s):
    j = len(s) - 1
    for i in range(len(s) // 2):
        if s[i] != s[j - i]:
            return False
    return True

"""def Panlindron_v3(s):
    for i in range(len(s) // 2 + 1):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True"""
P=Panlindron_v3(s)
if P==True:
    print('Palindrom')
else:
    print('Not Palindrom')
