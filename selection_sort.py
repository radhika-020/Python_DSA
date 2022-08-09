def selection_sort(arr):
  n = len(arr)
  for i in range(0, n-1):
    min = i
    for j in range(i + 1, n):
      if arr[min] > arr[j]:
        min = j
     arr[i], arr[min] = arr[min], arr[i]
     
"""Time complexity = O(N^2)"""
