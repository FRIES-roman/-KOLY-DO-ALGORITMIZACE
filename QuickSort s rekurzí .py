def quick_sort(array, level=0):
    global call_count
    call_count += 1 
    
    if len(array) <= 1:
        return array
    
    pivot = array[len(array) // 2]
    lesser = [num for num in array if num < pivot]
    equal = [num for num in array if num == pivot]
    greater = [num for num in array if num > pivot]
    
    return quick_sort(lesser, level + 1) + equal + quick_sort(greater, level + 1)

call_count = 0


data = [3, 6, 8, 10, 1, 2, 1]
sorted_data = quick_sort(data)
print("Seřazený seznam:", sorted_data)
print("Celkový počet volání rekurze:", call_count)
