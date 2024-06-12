str = input("Enter String: ")

n = len(str)
n = int(n/2)
str = list(str)

for i in range(n):
    str[i],str[-i-1] = str[-i-1],str[i]

str = ''.join(str)

print(str)