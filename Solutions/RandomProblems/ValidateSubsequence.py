# algoexpert
def isValidSubsequence(array, sequence):
    j=0

    for i in range(len(array)):
        if j < len(sequence) and array[i] == sequence[j]:
            j += 1
    return j == len(sequence)

array = [5,1,22,25,6,-1,8,10]
sequence = [1,6,-1,10]
print(isValidSubsequence(array, sequence)) 