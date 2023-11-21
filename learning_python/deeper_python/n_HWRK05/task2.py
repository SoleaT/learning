names = ['вася', 'ася', 'лена']
rates = [11, 22, 33]
bonus = ['10.25%', '15.4%', '2.0%']

bux = {x: y + y * (float(z[:-1]) / 100) for x, y, z in zip(names, rates, bonus)}

print(bux)
