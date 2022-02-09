left_der = lambda yi, h: [(yi[i] - yi[i - 1]) / h for i in range(1, len(yi))]

right_der = lambda yi, h: [(yi[i + 1] - yi[i]) / h for i in range(0, len(yi) - 1)]

central_der = lambda yi, h: [(yi[i + 1] - yi[i - 1]) / (2 * h) for i in range(1, len(yi) - 1)]

approximate_second_der = lambda yi, h: [(yi[i + 1] - (2 * yi[i]) + yi[i - 1]) / (h ** 2) for i in range(1, len(yi) - 1)]
