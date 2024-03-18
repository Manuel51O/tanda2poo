from duration import Duration

t1 = Duration(1, 20, 30)
t2 = Duration(2, 75, -10)
t3 = Duration(t2)

print(f'Duration 1: {t1}')
print(f'Duration 2: {t2}')
print(f'Duration 3: {t3}')

print(f't1 + t2 = {t1.__add__(t2)}')
print(f't2 + t3 = {t2.__add__(t3)}')
print(f't3 + t2 = {t3.__add__(t2)}')
print(f't1 + 1h 20m 30s = {t1.__add__(1, 20, 30)}')
print(f't1 + 1h 20m 30s = {t1.__add__(1, 20, 30)}')

print(f't1 - t2 = {t1.__sub__(t2)}')
print(f't2 - t3 = {t2.__sub__(t3)}')
print(f't2 - 1h 20m 30s = {t2.__sub__(1, 20, 30)}')
print(f't2 - 1h 20m 30s = {t2.__sub__(1, 20, 30)}')