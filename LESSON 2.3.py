a = 'ABCAAC1C'

def strcounter(a):    #8*8 операций
    for char in a:
        counter=0
        for sub_char in a:
            if char == sub_char:
                counter+=1
        print(char,counter)

def strcounter1(a):    #8*4 операций(кол-во всех символов*кол-во уникальных)
    for char in set(a):
        counter=0
        for sub_char in a:
            if char == sub_char:
                counter+=1
        print(char,counter)

def strcounter2(a):  #8 операций
    syms_counter={}
    for char in a:
        syms_counter[char]=syms_counter.get(char,0)+1
    print(syms_counter)

strcounter2(a)