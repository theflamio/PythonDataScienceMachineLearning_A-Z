import numpy as np

#convert list intro array

# Obs List can contain any type of data
# starts from 0
ListA = [232, 34, 232, 43, -25]

# Arrays can only obtain one kind of data string, int, float ect.
a = np.array(ListA)

print(a)

#b = np.array([1 ,-32, 45.3, "hello", True])

#print(b ,"because there is a string in the list the array has converted all data into strings !!!")


#slicing Array's "OBS" when slicing you do not make a copy of that array but with list's you do copy when slicing

print(a[2:])
print(a[2:4])

b = a[2:4]

b[:] = 111

print(b[:])
# OBS this is the proff of that b is not a copy of the a array when you change the values in b you also change the values in a since it is the same array.
print(a[:]) 