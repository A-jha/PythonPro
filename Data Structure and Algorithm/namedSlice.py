items = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# Instead of doing manually we can set qa slic options
print(items[2:4])

# slice(start,end,step)

# a sile [2:4]
a = slice(2, 4)
# b slice [4: ]
b = slice(4, 8, 2)
print(items[a])
print(items[b])

# here b is an instance of slice so we can perform
# b.start
# b.end
# b.step
