def cipher(k, s):
    arr=[]
    cifrado=""
    for i in range(k):
        arr.append(s.zfill(len(s)+i))
    for i in range(n):
        x=arr[0][i]
        for j in range(0,k-1):
            if int(x)==int(arr[j+1][i]):
                x= 0
            else: 
                x=1              
        cifrado+=str((int(x)))
    print(cifrado)
first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

k = int(first_multiple_input[1])

s = input()

result = cipher(k, s)
