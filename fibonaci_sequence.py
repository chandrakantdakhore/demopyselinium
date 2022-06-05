a = 0
b = 1

print(a)
print(b)
for i in range(2, 20):
    c = a + b
    a = b
    b = c
    print(c)
    if c == 89:
        quit()
