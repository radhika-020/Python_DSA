# Time Complexity is : O(n^2)
# Space Complexity is : O(1)

def stockSpan(arr):
    for i in range(len(arr)):
        curr_span = 1
        j = i - 1
        while j >= 0 and arr[j] <= arr[i]:
            curr_span += 1
            j -= 1
        print(curr_span, end=" ")


# Driver Code
arr = [12, 14, 15, 7, 15, 17, 5]
stockSpan(arr)
