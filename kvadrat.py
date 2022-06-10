a, b, c = map(float, input().split())
D = b ** 2 - 4 * a * c
print('D =', D)
if D > 0:
    print('x1 =', (-b + D ** 0.5)/(2 * a))
    print('x2 =', (-b - D ** 0.5)/(2 * a))
if D < 0:
    print('Нет корней')
if D == 0:
     print('x =', -b/(2 * a))
