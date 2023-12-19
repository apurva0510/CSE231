#write your code here
#you should only write all your functions in the same file
#Nothing outside of the functions

def leap_year(y):
    y = int(y)
    if y%100 == 0 and y%400 != 0 or y%4 != 0 :
        return False
    return True

def rotate(s, n):
    n = int(n)
    l = len(s)
    if n > l:
        return s
    return s[l-n:] + s[:l-n]

def digit_count(n):
    even_count = 0
    odd_count = 0
    zero_count = 0

    n = str(n)

    for i,ch in enumerate(n):
        if ch == '.':
            break

        ch = int(ch)

        if ch == 0:
            zero_count += 1
        elif ch%2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return (even_count, odd_count, zero_count)

def float_check(n):
    n = str(n)
    if 'e' in n:
        return False
    try:
        float(n)
        return True
    except ValueError:
        return False