# from Source.vectors import Vector2
#
# a = Vector2(0, 0)
# b = Vector2(1, 1)
#
# pool = []
#
# for i in range(10):
#     pool.append(a)
#
# for i in pool:
#     i.x = b.x
#     b.x += 1
#     print(i.x, end=' ')
#

# print(3//

a = []

def adder(*args):
    print(args)
    for i in args:
        a.append(i)

adder(1,2,3,4,5,6,7)

print(a)