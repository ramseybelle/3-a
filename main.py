n = int(input("How many integers would you like to enter?\n"))
print("Please enter %d integers." % n)
small: int = 999999999999999  # initialize small with some large number.
large: int = -99999999999999  # initialize large with some lease number.
for i in range(0, n):  # loop will run up to a number of integers.
    k: int = int(input())  # read the integer one by one.
if k < small:  # if the integer is less than the small.
    small = k  # stores the integer in small
if k > large:  # if the integer is more than the large.
    large = k  # stores the integer in large
print("min:", small)  # printing the small value
print("max:", large)  # print the large value.
