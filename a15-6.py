def khayyam_pascal(n):
    arr1 = []
    for i in range(n):
        arr1.append([1]*(i+1))
        
    for i in range(2,n):  
        for j in range(1,i)  :
            arr1[i][j]=arr1[i-1][j-1]+arr1[i-1][j]
            
    for i in range(n):
        print(arr1[i])


if __name__ == "__main__":
    c = "y"
    while c=="y" :
        n = int(input('Enter your number : '))
        res = khayyam_pascal(n)
        print('\n')
        ch=input("Try again ? [y/n]")
        print('\n')
        if ch == "n" :
            c='n'
    