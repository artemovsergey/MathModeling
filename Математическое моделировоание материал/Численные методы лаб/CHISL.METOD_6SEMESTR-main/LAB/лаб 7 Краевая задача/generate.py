def getRange(start, end, step, accuracy):
    prev, arr = start, [start]
    while end >= prev:
        prev += step
        if prev > end:
            break
        arr.append(round(prev, accuracy))
    return arr
