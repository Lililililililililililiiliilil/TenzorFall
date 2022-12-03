coefs = list(map(float, input('Input coefficients of the equation ').split()))
coefs = list(map(complex, coefs))
discriminant = coefs[1] ** 2 - 4 * coefs[0] * coefs[2]
if coefs[0] == 0.0:
    print("Linear equation!")
elif discriminant != 0:
    x1 = (-coefs[1] - discriminant ** 0.5) / (2 * coefs[0])
    x2 = (-coefs[1] + discriminant ** 0.5) / (2 * coefs[0])
    x1 = complex(x1.real, x1.imag)
    x2 = complex(x2.real, x2.imag)
    if x1.imag == 0.0:
        x1 = x1.real
    if x2.imag == 0.0:
        x2 = x2.real
    print('X_1 = {:.2f}'.format(x1))
    print('X_2 = {:.2f}'.format(x2))
elif discriminant == 0.0:
    x = -coefs[1] / (2 * coefs[0])
    x = complex(x.real, x.imag)
    print('X = {:.2f}'.format(x))
else:
    print('Incorrect input')
