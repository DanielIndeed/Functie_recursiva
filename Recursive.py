import matplotlib.pyplot as plt

def recursive_func(x, n):
    if n == 0:
        return [x]
    else:
        x_prev = recursive_func(x, n-1)[-1]
        x_n = x_prev * (1 - x_prev)
        return recursive_func(x, n-1) + [x_n]

x_values = recursive_func(0.1, 24)

plt.plot(list(range(25)), x_values)
plt.xlabel('n')
plt.ylabel('x(n)')
plt.show()

# Fiecare funcție se va trasa în parte
