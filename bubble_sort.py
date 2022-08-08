def bubble_sort(arr):
  n = len(arr)
  for i in range(n-1): """n-1 because there woukd be len-1 passes while sorting in bubble sort. You can also use n here."""
    for j in range(n-i-1): """Done -1 because everytime we complete a pass, the biggest number is already at its sorted place. Therefore, decreasing the size by 1."""
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1], arr[j+1], arr[j]
        
arr = [2, 4, 7, 1, 20]
bubble_sort(arr)
print("After sorting {}". format(arr))


"""Time Complexity = O(n^2)"""
    
