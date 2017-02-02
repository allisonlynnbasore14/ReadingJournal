fin = open('words.txt')

def is_palindrome(string):
    if len(string)%2 != 0:
        return False
    s = string
    first = s[0]
    last = s[-1]
    middle = s[1:len(s)-1]
    if len(s)==2:
        if first != last:
            return False
        return True
    if first == last:
        return is_palindrome(middle)

def find_pal():
    output = []
    for line in fin:
        if is_palindrome(line) == 1:
            output.append(line)
    return output





val = is_palindrome('testtset')
print(val)
