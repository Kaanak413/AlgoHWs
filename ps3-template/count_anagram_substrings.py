def are_anagrams(s1, s2):
    # Count the frequency of each character in both strings and compare
    from collections import Counter
    return Counter(s1) == Counter(s2)

def count_anagram_substrings(T, S):
    '''
    Input:  T | String
            S | Tuple of strings S_i of equal length k < |T|
    Output: A | Tuple of integers a_i:
              | the anagram substring count of S_i in T
    '''
    A = [0] * len(S)
    k = len(S[0])
    
    # Create all substrings of T of length k
    substrings = []
    for i in range(len(T) - k + 1):
        substrings.append(T[i:i+k])
    
    # Count anagram matches for each S_i
    for idx, si in enumerate(S):
        for substr in substrings:
            if are_anagrams(substr, si):
                A[idx] += 1

    return tuple(A)
