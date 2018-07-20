# import numpy as np

import matplotlib.pyplot as plt
import sys


drawHorizontal = True
count = 0
orderCount = 0


def drawLine(x, y, len, order):
    global drawHorizontal, count, orderCount, factor

    print("OC:", orderCount)
    if order != orderCount:
        # len *= factor
        orderCount += 1
        print("mod", count%2)
        if count % 2 == 0:
            count += 1
            drawHorizontal = True
            print(">>", len)
            plt.plot([(x-len/2),(x+len/2)], [y,y], 'r-')
            print('true')
            drawLine(x+len/2, y, len*factor, order)
            print("next x")
            drawLine(x-len/2, y, len*factor, order)
        else:
            count += 1
            drawHorizontal = False
            print(">>>", len)
            plt.plot([x,x], [(y-len/2),(y+len/2)], 'r-')
            print('false')
            drawLine(x, y+len/2, len*factor, order)
            print("next y")
            drawLine(x, y-len/2, len*factor, order)
    else:
        print("else")
        return
    return



# print("Argv[0]: %s\n"
#       "Argv[1]: %s" % (sys.argv[0], sys.argv[1]))
#
# print ("This is the name of the script: ", sys.argv[0])
# print ("Number of arguments: ", len(sys.argv))
# print ("The arguments are: " , str(sys.argv))

plt.close('all')
plt.figure()

order = int(sys.argv[1])
factor = float(sys.argv[2])

print("start")
drawLine(0,0,5,order)

# drawLine(0,0,5,0)


plt.show()