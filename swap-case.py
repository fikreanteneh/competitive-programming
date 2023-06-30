def swap_case(s):
    new = []
    for i in s:
        if i.isalpha():
            if i.isupper(): new.append(i.lower())
            else: new.append(i.upper())
        else:new.append(i)
    return "".join(new)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
