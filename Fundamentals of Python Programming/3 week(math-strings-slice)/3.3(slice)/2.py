string = input()
if string.find('f') != 0:
    if 'f' not in string:
        print()
    elif string.rfind('f') != 0 and string.find('f') != string.rfind('f'):
        print(string.find('f'), string.rfind('f'))
    else:
        print(string.find('f'))
