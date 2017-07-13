'''
Simple idea of the Kadane's algorithm is to look for all positive contiguous segments of the array (max_ending_here is used for this).
And keep track of maximum sum contiguous segment among all positive segments (max_so_far is used for this).
Each time we get a positive sum compare it with max_so_far and update max_so_far if it is greater than max_so_far

Mateus Sousa, Maio de 2017
'''
def kadanes_method(A):
    max_so_far = 0
    max_ending_here = 0
    for i in range(0,len(A)):
        max_ending_here += A[i]
        if max_ending_here < 0:
            max_ending_here = 0
        elif max_ending_here > max_so_far:
            max_so_far = max_ending_here

    return max_so_far

array = [-2, -3, 4, -1, -2, 1, 5, -3]
print kadanes_method(array)
