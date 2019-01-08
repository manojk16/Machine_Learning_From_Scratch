def get_divisor(num, possible_divisor):

    divisors=[]
    for item in possible_divisor:
        if item!=0 and num % item==0:
            divisors.append(item)
    return divisors

if __name__ == '__main__':
    import doctest
    doctest.testmod()
