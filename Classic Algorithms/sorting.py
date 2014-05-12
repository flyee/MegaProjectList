import random

def quickSort(l):
    if len(l) <= 1:
        return l
    m = l[random.randrange(0,len(l))]
    left, mid, right = [], [], []
    for i in l:
        if i < m:
            left.append(i)
        elif i == m:
            mid.append(i)
        else:
            right.append(i)
    return quickSort(left) + mid + quickSort(right)

def mergeSort(l):
    if len(l) <= 1:
        return l
    m = len(l)//2
    left = l[:m]
    right = l[m:]
    # divide
    left = mergeSort(left)
    right = mergeSort(right)
    # merge
    l = []
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            l.append(left[0])
            left = left[1:]
        else:
            l.append(right[0])
            right = right[1:]
    # merge the rest
    l = l + left + right
    return l
            

def main():
    s = input("Input number array:\n")
    l0 = [int(i) for i in s.split()]
    l1 = l0[:]
    l2 = l0[:]

    print("Origin:", l0)

    l0.sort()
    print("Buildin sort:", l0)

    l1 = quickSort(l1)
    print("Quicksort:", l1)
    assert l0 == l1

    l2 = mergeSort(l2)
    print("Mergesort:", l2)
    assert l0 == l2


if __name__ == '__main__':
    main()

