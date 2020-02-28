# Given a list of numbers, find and print all elements that are an even number. In
# this case use a for-loop that iterates over the list, and not over its indices! That
# is, don't use range

list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print([i for i in list_ if i % 2 == 0])
