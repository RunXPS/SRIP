import time
x = 0
y = time.time()
for i in range(30000):
    x = i
print("Hello World!")
y -= time.time()
print(y)