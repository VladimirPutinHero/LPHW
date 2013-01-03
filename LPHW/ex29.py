#encoding=utf-8


def wh(c, step):
    numbers = []
    i = 0
    while i < c:
        print "At the top i is %d" % i
        numbers.append(i)
        i = i + step
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
    return numbers


def wh_for(c, step):
    numbers = []
    for i in range(0, c, step):
        print "At the top i is %d" % i
        numbers.append(i)
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
    return numbers

c = 10
step = 2
numbers = wh_for(c, step)
print "The numbers: "

for num in numbers:
    print num,
