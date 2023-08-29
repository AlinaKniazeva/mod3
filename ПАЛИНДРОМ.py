a = 'кот'

def pol(a):
    if a == a[::-1]:    #Переворот строки в обратную сторону
        print('True')
    else:
        print('false')
pol(a)