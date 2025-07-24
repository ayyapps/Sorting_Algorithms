# 68 25 71 43 5
#Selection Sort
# time O(n²) space O(1)

def bubble_sort(arr):
    for i in range(len(arr)):
        swap_flag = False
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1], arr[j]
                swap_flag = True
        if not swap_flag:
            break

numbersval = input("Please enter numbers: ")
arr = list(map(int, numbersval.split()))
print("original array: ", arr)
bubble_sort(arr)
print("sorted array:", arr )