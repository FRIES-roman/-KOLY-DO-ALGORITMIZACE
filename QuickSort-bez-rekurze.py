def quick_sort_iterative(array):
    stack = [(0, len(array) - 1)]
    while stack:
        left, right = stack.pop()
        if left >= right:
            continue
        
        pivot = array[(left + right) // 2]
        i, j = left, right
        while i <= j:
            while array[i] < pivot:
                i += 1
            while array[j] > pivot:
                j -= 1
            if i <= j:
                array[i], array[j] = array[j], array[i]
                i += 1
                j -= 1
        
        stack.append((left, j))
        stack.append((i, right))
    
    return array

# Testovací příklad
data = [3, 6, 8, 10, 1, 2, 1]
sorted_data = quick_sort_iterative(data)
print("Seřazený seznam:", sorted_data)
