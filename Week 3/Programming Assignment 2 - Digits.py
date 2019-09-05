x=input()
y, z= x.count('0'), x.count('1')
print("YES" if y==1 or z==1 else "NO", end="")