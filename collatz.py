# numero entero
# n = int(input('n: '))
# while n!=1:
#     print(int(n), end=' ')
#     if n%2==0:
#         n /= 2
#     else:
#         n = n*3+1
# print(1)

# Largos
n = int(input('n: '))
j=0
for i in range(1,n+1):
    j=i
    len=1
    while j!=1:
        len+=1
        if j%2==0:
            j /= 2
        else:
            j = j*3+1
    row_output = len * '*'
    print(f'{i} {row_output}')