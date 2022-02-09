





from polynom.lagrange import find_interval_end_index


def separtedDiffEndCase(Ys, Xs, i):
    nominator_presentation = "({first} - {second})".format(first=Ys[i + 1], second=Ys[i])
    nominator = Ys[i + 1] - Ys[i]
    denominator_presentation = "({first} - {second})".format(first=Xs[i + 1], second=Xs[i])
    denominator = Xs[i + 1] - Xs[i]
    presentation = "(" + nominator_presentation + " / " + denominator_presentation + ")"
    return (nominator / denominator, presentation)



# рассчитывает разденную разность от i до i + n по значениям Xs
def separatedDiff(Ys, Xs, i, n):
    if n <= 1:
        return separtedDiffEndCase(Ys, Xs, i)

    first_result, first_presentation = separatedDiff(Ys, Xs, i + 1, n - (i + 1))
    second_result, second_presentation = separatedDiff(Ys, Xs, i, n - 1 - i)
    nominator =  first_result -  second_result
    denominator = Xs[i + n] - Xs[i]

    presentation = "(" + first_presentation + " - " + second_presentation + ")/(" + str(Xs[i + n]) + " - " + str(Xs[i]) + ")"
    return (nominator / denominator, presentation)


def newton(Ys, Xs, n, x):
    interval_end_index = find_interval_end_index(Xs, x)
    interval_start_index = interval_end_index - n
    if interval_start_index < 0:
        interval_start_index = 0
        n = interval_end_index

    current = interval_start_index
    result = 0
    presentation = ""
    while current <= interval_end_index:
        element = 1
        element_presentation = ""
        if current - interval_start_index == 0:
            element *= Ys[interval_start_index]
            element_presentation = str(Ys[interval_start_index])
        else:
            separte_diff_result, separate_diff_presentation = separatedDiff(Ys, Xs, interval_start_index, current - interval_start_index)
            element_presentation += separate_diff_presentation + " * "

            element *= separte_diff_result

            additional_parenthis_presentation = ""
            subIndex = interval_start_index
            while subIndex < current:
                element *= (x - Xs[subIndex])
                additional_parenthis_presentation += "(x - " + str(Xs[subIndex]) + ") * "
                subIndex += 1
            additional_parenthis_presentation = additional_parenthis_presentation[0:-3]
            element_presentation += additional_parenthis_presentation
        result += element
        current += 1
        presentation += element_presentation + " + "
    presentation = presentation[0:-3]
    return (result, presentation)





# result = separatedDiff(Ys, Xs, 0, 2)
# print(result)

