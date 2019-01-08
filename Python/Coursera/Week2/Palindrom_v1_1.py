def is_palindrom_v1(s):
    return reverseS(s)==s

def reverseS(s):
    rev=''
    for ch in s:
        rev = ch + rev
    return rev
if __name__=='__main__':
    print('Name of the module',__name__)
    word=input('Enter a word\n')
    if is_palindrom_v1(word):
        print(word,'is a Palindrom')
    else:
        print(word,'Not a palindrom')
