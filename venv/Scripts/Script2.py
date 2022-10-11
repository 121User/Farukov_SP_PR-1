try:
    file = open('Info.txt', 'r')
    fileR = file.read()
    if fileR == '':
        raise Exception
    print(fileR)
except FileNotFoundError:
    print('Файла не существует')
except Exception:
    print('Файл пуст')
else:
    file.close()