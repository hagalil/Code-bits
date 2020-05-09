#Max consecutive sum (MCS) by brute force
def MCS_brute(lst):
    n = len(lst)
    loacal_max = lst[0]
    seq = (0, 0)
    for i in range(n):
        for j in range(i,n):
            buffer = sum(lst[i:j+1])
            if buffer > loacal_max:
                loacal_max = buffer
                seq = (i, j)
    print("The window is from %d to %d and the max sum is:" %(seq[0], seq[1]))
    return loacal_max
lst = [-19,-2,20,5,5]
print(MCS_brute(lst))