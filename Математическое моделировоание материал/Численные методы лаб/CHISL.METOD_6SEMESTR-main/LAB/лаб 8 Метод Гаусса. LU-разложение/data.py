import decimal as dec

MATRIX = [
    [dec.Decimal("4.3"), dec.Decimal("-12.1"), dec.Decimal("23.2"), dec.Decimal("-14.1"), dec.Decimal("15.5")],
    [dec.Decimal("2.4"), dec.Decimal("-4.4"), dec.Decimal("3.5"), dec.Decimal("5.5"), dec.Decimal("2.5")],
    [dec.Decimal("5.4"), dec.Decimal("8.3"), dec.Decimal("-7.4"), dec.Decimal("-12.7"), dec.Decimal("8.6")],
    [dec.Decimal("6.3"), dec.Decimal("-7.6"), dec.Decimal("1.34"), dec.Decimal("3.7"), dec.Decimal("12.1")],
]

TEST1_MATRIX = [
    [dec.Decimal("3"), dec.Decimal("-1"), dec.Decimal("0"), dec.Decimal("5")],
    [dec.Decimal("-2"), dec.Decimal("1"), dec.Decimal("1"), dec.Decimal("0")],
    [dec.Decimal("2"), dec.Decimal("-1"), dec.Decimal("4"), dec.Decimal("15")],
]

TEST2_MATRIX = [
    [dec.Decimal("1"), dec.Decimal("2"), dec.Decimal("3"), dec.Decimal("5")],
    [dec.Decimal("0"), dec.Decimal("0"), dec.Decimal("1"), dec.Decimal("1")],
    [dec.Decimal("0"), dec.Decimal("2"), dec.Decimal("5"), dec.Decimal("4")],
]

TEST3_MATRIX = [
    [dec.Decimal("1"), dec.Decimal("2"), dec.Decimal("3"), dec.Decimal("5")],
    [dec.Decimal("0"), dec.Decimal("0"), dec.Decimal("1"), dec.Decimal("1")],
    [dec.Decimal("0"), dec.Decimal("0"), dec.Decimal("15"), dec.Decimal("15")],
]

TEST4_MATRIX = [
    [dec.Decimal("1"), dec.Decimal("2"), dec.Decimal("3"), dec.Decimal("5")],
    [dec.Decimal("0"), dec.Decimal("1"), dec.Decimal("2"), dec.Decimal("3")],
    [dec.Decimal("0"), dec.Decimal("0"), dec.Decimal("0"), dec.Decimal("1")],
]

TEST5_MATRIX = [
    [dec.Decimal("1"), dec.Decimal("2"), dec.Decimal("3"), dec.Decimal("4"), dec.Decimal("10")],
    [dec.Decimal("2"), dec.Decimal("4"), dec.Decimal("6"), dec.Decimal("8"), dec.Decimal("20")],
    [dec.Decimal("1"), dec.Decimal("2"), dec.Decimal("2"), dec.Decimal("2"), dec.Decimal("7")],
    [dec.Decimal("2"), dec.Decimal("4"), dec.Decimal("5"), dec.Decimal("4"), dec.Decimal("15")],
]

TEST6_MATRIX = [
    [dec.Decimal("1"), dec.Decimal("2"), dec.Decimal("3"), dec.Decimal("4"), dec.Decimal("10")],
    [dec.Decimal("2"), dec.Decimal("4"), dec.Decimal("6"), dec.Decimal("8"), dec.Decimal("20")],
    [dec.Decimal("4"), dec.Decimal("8"), dec.Decimal("12"), dec.Decimal("16"), dec.Decimal("40")],
    [dec.Decimal("2"), dec.Decimal("4"), dec.Decimal("5"), dec.Decimal("4"), dec.Decimal("15")],
]
