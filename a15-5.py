flag = False
c='y'

while c == 'y' :
    arr = input('Enter your numbers with space(e.g. : 1 2 3) : ')
    Array = arr.split(' ')
    leng = len(Array)

    for i in range(leng) :
        j=leng-i-1
        if Array[i] == Array[j]:
            flag = True
        else :
            flag = False
            break

    if flag == True:
        print("Symmetrical")
    if flag == False:
        print('Asymmetrical')    

    ch=input("Try again ? [y/n]")
    if ch == "n" :
        c='n'

