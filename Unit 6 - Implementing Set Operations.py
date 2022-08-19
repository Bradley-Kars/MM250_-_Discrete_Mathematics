# Initialize sets A and B
A = { 'a', 'b', 'c', 'd', 'e', 'f' }
B = { 'c', 'd', 'f', 'h', 'j', 'k' }

print('A = ', sorted(A))
print('B = ',sorted(B))
print(' ')
#Block 1: computes and prints out the set A - B

AminusB = set()
for element in A:   # this line runs through every element in A
    if not(element in B): #A - B is the set of elements that are in A and are not in B
        AminusB.add(element) # Add it AminusB every element in A if the element is also not in B
        
print('A - B = ', sorted(AminusB))
print(' ')
        
#Block 2: computes and prints out the set B - A

BminusA = set()
for element in B:   # this line runs through every element in B
    if not(element in A): #B - A is the set of elements that are in B and are not in A
        BminusA.add(element) # Add it BminusA every element in B if the element is also not in A
        
print('B - A = ', sorted(BminusA))
print(' ')

#Block 3: computes and prints out the symmetric difference of A and B

AsymdiffB = set()
for element in A:
    if not(element in B):
        AsymdiffB.add(element)
for element in B:
    if not(element in A):
        AsymdiffB.add(element)
        
print('Symmetric Difference of A and B = ', sorted(AsymdiffB))