# Write a function that returns the largest number in a tuple (Using Arbitrary Arguments will earn you
# bonus marks)


def largest(*numbers):  # define a function and pass it all numbers
    largeNum = 0  # variable largeNum
    for item in numbers:              # loop through the numbers
        if item > largeNum:        # if item is greater than, replace it with the larger num
            largeNum = item

    return largeNum

print(largest(23, 45, 900, 7000, 54, 23, 21, 1))
