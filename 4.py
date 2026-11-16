# Gradient descent

x = 2
lr = 0.1
for i in range(20):
    gradient = 2 * (x + 3)
    x = x - lr * gradient
    print(i + 1, x, (x + 3) ** 2)
print('Final x:', x)
print('Final y:', (x + 3) ** 2)
