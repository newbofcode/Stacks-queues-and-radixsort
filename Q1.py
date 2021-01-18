# CPS305 Fall 2020
# Lab 4 Q1
# Yong Kang He
# 500570639

# Impement radix sort
# Input is a list of vectors, and an integer n, the number of vectors in the list
# Each vector is a list of digits
# Every vector is the same length
# Sort ascending
def radixSort(n, vectors):
    base = 10
    placement = 1
    while placement < len(vectors[0]):
        buckets = [list() for i in range(base)]
        for i in vectors:
            temp = i[placement*-1]
            buckets[temp].append(i)
        a=0
        for b in range( base ):
            buck = buckets[b]
            for i in buck:
                vectors[a] = i
                a += 1
        placement += 1


    return vectors
    # Your code here


# DO NOT EDIT THE FOLLOWING CODE
vectors = [
    [3,3,3,3,3,2,2,2,2,2],
    [2,3,2,2,2,2,2,2,2,2],
    [1,3,0,0,2,1,0,0,0,0],
    [1,3,0,0,2,1,0,0,0,0],
    [2,3,2,1,2,2,2,2,2,2],
]

sortedVectors = radixSort(5, vectors)
for vector in sortedVectors:
    print(vector)