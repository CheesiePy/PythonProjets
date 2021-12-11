def tylorPi(epsilon):
    denominator = 1.0
    numerator = 4.0
    acumulator = (numerator/denominator)

    while epsilon < abs(numerator/denominator):
        denominator += 2
        numerator *= (-1)  # flip sign with every iteration
        acumulator += (numerator/denominator)

    return acumulator


print(tylorPi(0.0001))

