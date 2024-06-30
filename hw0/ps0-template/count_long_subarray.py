def count_long_subarray(A):
    '''
    Input:  A     | Python Tuple of positive integers
    Output: count | number of longest increasing subarrays of A
    '''
    count = 0
    currentLen = 1
    maxLen = 1
    arrLen = len(A)
    for i in range(1,arrLen):
        if(A[i-1]<A[i]):
            currentLen = currentLen + 1
        else:
            currentLen = 1    
        if(maxLen==currentLen):
                count=count+1
        elif(currentLen>maxLen):
             maxLen = currentLen
             count = 1
        

    return count
