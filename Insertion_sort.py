def insertion_sort(arr):
  n = len(arr)
  for i in range(1, n):
    temp = arr[i]
    j = i-1
    while j > =0 and temp < arr[j]:
      arr[j+1] = arr[j]
      j= j-1
    arr[j+1] = temp
"""Time Compexity = O(N) in best case and O(N^2) in worst and average cases.
