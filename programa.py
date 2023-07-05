def StockPicker(arr):
    maxcost = 0

    mini = arr[0]
    for i in range(0, len(arr)):
        mini = min(mini, arr[i])
        cost = arr[i] - mini
        maxcost = max(maxcost, cost)
    return maxcost


print(StockPicker([44, 30, 24, 32, 35, 30, 40, 38, 15]))