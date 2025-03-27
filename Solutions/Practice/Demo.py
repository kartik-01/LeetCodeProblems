def recursion(n, left, right):
    if left >= right:
        return n
    
    n[left], n[right] = n[right], n[left]
    
    recursion(n, left + 1, right -1)


n = list(input("Enter number: "))
print(recursion(n, 0, len(n) - 1))

st='Kartik'

print(st[0])