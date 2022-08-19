# Block 1 computes the summation: Sum_{j = 0}^17 (3j + 2)
sum = 0
for j in range(0,18):
    sum = sum + (3*j + 2)
    
print('Sum_{j = 0}^17 (3j + 2) = ' + str(sum))
print(' ')

# Block 2 computes the summation: Sum_{j = 0}^17 3j + 2
sum = 0
for j in range(0,18):
    sum = sum + 3*j
sum = sum + 2

print('Sum_{j = 0}^17 3j + 2 = ' + str(sum))
print(' ')

# Block 3 computes the summation: Sum_{j = -2}^4 (2j + 1)^2
sum = 0
for j in range(-2,5):
    sum = sum + (2*j + 1)**2
    
print('Sum_{j = -2}^4 (2j + 1)^2 = ' + str(sum))
print(' ')

# Block 4 computes the summation: Sum_{j = -1}^8 2^{j+4} + 17
sum = 0
for j in range(-1,9):
    sum = sum + 2**(j+4)
sum = sum + 17
    
print('Sum_{j = -1}^8 2^{j+4} + 17 = ' + str(sum))
print(' ')

# Block 5 computes the summation: Sum_{j = 3}^8 (2^{j-1} + 3j + 1) - 13
sum = 0
for j in range(3,9):
    sum = sum + (2**(j-1) + 3*j + 1)
sum = sum - 13
    
print('Sum_{j = 3}^8 (2^{j-1} + 3j + 1) - 13 = ' + str(sum))
print(' ')

# Block 6 computes the sum of the even integers between 5 and 17
sum = 0
for j in range(6,18,2):
    sum = sum + j
    
print('The the sum of the even integers between 5 and 17 is ' + str(sum))
print(' ')

# Block 7 computes the sum of the odd integers between 8 and 32
sum = 0
for j in range(9,33,2):
    sum = sum + j

print('The the sum of the odd integers between 8 and 32 is ' + str(sum))