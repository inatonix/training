def check_double(st):
    check = [False] * 128
    for s in st:
        h = ord(s)
        if check[h]:
            return True
        check[h] = True
    return False

if __name__ == '__main__':
    print(check_double('abcdedf'))