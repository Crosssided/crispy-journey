
# blocks = int(input("Enter the number of blocks: "))


# n = 0.7
# x = 1

# while True:
#     n += 0.3
#     step = round(n)

#     print(step)

#     if step > 10:
#         break

# print(step)
# print("The height of the pyramid is:", x)



blocks = int(input("Enter the number of blocks: "))

layer = 1
height = 0

while blocks >= layer:
    blocks -= layer
    layer += 1
    height += 1

print(blocks)
print(layer)

print(f"The height of the pyramid is: {height}")