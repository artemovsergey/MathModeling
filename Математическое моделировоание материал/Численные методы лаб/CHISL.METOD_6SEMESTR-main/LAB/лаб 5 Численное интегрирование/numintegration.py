Xk = [-0.93247, -0.66121, -0.23862, 0.238619, 0.661209, 0.93247]
Ck = [0.171324, 0.360762, 0.46793, 0.46793, 0.360762, 0.171324]

left_rectangles = lambda yi, h: sum(yi[:len(yi)-1]) * h

right_rectangles = lambda yi, h: sum(yi[1:]) * h

central_rectangles = lambda func, xi, h: sum([func(xi[i] + (h / 2)) for i in range(0, len(xi)-1)]) * h

trapezoids = lambda yi, h: (h / 2) * (yi[0] + yi[len(yi)-1] + 2 * sum(yi[1:len(yi)-1]))

parabolas = lambda yi, h: (h / 3) * (yi[0] + sum([y * 4 if i % 2 != 0 else y * 2 for i, y in enumerate(yi)
                                                  if i != 0 and i != len(yi) - 1]) + yi[len(yi)-1])

gauss = lambda a, b, fi, n: ((b - a) / 2) * sum([Ck[i] * fi[i] for i in range(0, n)])
