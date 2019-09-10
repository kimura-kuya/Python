f = [1,1]
index = 2

for i in range(100):
     x = f[index-1]
     y = f[index-2]
     f.append(x+y)
     index += 1

print(f)
