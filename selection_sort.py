# 68 25 71 43 5
#Selection Sort

def selection_sort(arr):
    for i in range(len(arr)-1):
        minval = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minval]:
                minval = j
        arr[i], arr[minval] = arr[minval], arr[i]


user_input = input("Enter the array numbers with space: ")
arr = list(map(int, user_input.split()))
print("original array", arr)
selection_sort(arr)
print("sorted array", arr)

