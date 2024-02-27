array = [64, 34, 25, 12, 22, 11, 90, 11]

def sort_insertion(array):
    length = len(array)
    for i in range(1, length):
        key = array[i]
        j = i - 1

        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key    

sort_insertion(array)
for e in array:
    print(e)