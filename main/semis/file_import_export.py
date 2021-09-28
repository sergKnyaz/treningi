

def file_read(fileneme):
    ''' Считывает из файла, формирует и взвращает двумерный список
    Reads from a file, forms and rotates a two-dimensional list'''
    ret = []
    try:
        f = open(fileneme, 'r', encoding='utf-8')
        for line in f.readlines():
            line = line.replace("\n", "")
            line = line.split(" ")
            ret.append(line)

        f.close()
    except:
        print('ОШИБКА ОТКРЫТИЯ ФАЙЛА! ПРОВЕРЬТЕ ПРАВИЛЬНОСТЬ ИМЕНИ И ПУТИ!!!')

    return ret


def file_rewriting(filename, variable):
    '''перезаписывает в файл данные'''
    try:
        f = open(filename, 'w', encoding='utf-8')
        f.write(str(variable))
        f.close()
    except:
        print('ОШИБКА ОТКРЫТИЯ ФАЙЛА! ПРОВЕРЬТЕ ПРАВИЛЬНОСТЬ ИМЕНИ И ПУТИ!!!')
