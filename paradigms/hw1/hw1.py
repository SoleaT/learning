# imrepative
def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_el = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_el]:
                min_el = j
        (arr[i], arr[min_el]) = (arr[min_el], arr[i])


arr = [6, 2, 7, 1, 3, 5, 9, 11, 0]
selection_sort(arr)
print(arr)

# declarative
arr = [6, 2, 7, 1, 3, 5, 9, 11, 0]
print(sorted(arr))
