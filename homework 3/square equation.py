coefs = list(map(float, input('Input coefficients of the equation ').split()))

discriminant = coefs[1] ** 2 - 4 * coefs[0] * coefs[2]

if coefs[0] == 0:
    print('Linear equation!')
elif discriminant > 0:
    x1 = (-coefs[1] - discriminant ** 0.5) / (2 * coefs[0])
    x2 = (-coefs[1] + discriminant ** 0.5) / (2 * coefs[0])
    print('X_1 = %.2f; X_2 = %.2f' % (x1, x2))
elif discriminant == 0:
    x = - discriminant ** 0.5 / (2 * coefs[0])
    print('X = %.2f' % x)
elif discriminant < 0:
    print('Has no real solutions')
else:
    print('Incorrect input')
