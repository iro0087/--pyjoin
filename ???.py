import matplotlib.pyplot as plt

import random
                                
import sys

import time

plt.figure(facecolor="grey")

ax = plt.axes()
              
ax.set_facecolor("grey")

limit = int(input("What is the limit?"))

l = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",

"o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D",

"E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",

"T", "U", "V", "W", "X", "Y", "Z ", "_", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

l2 = []

v = 0

print("This list contains", l.count(" "), "spaces")

print("")

print("Its lenght is equal to:", len(l))

time.sleep(1.5)

cl = []

t = 1

p = 0

pl = [0, 0]

while t < limit:

    r = random.choice(l)

    if r == " ":

        print("This sentence will never appear")

    l2.append(r)

    if l2.count(" ") > 0:

        time.sleep(5)

        print("This sentence will never appear 2")

    j = "".join(l2)

    if len(cl) > 0:

        if j.count(" ") > cl[-1]:

            p = p + 1

    cl.append(j.count(" "))

    percentage = (p / t) * 100

    pl.append(percentage)

    t = t + 1

    print(t, pl[-2], pl[-1])

    print("")

    print("------------------------------------------------------------")

    print("")

    plt.plot([t - 1, t], [pl[-2], pl[-1]], color="#000000", marker="+")

shw = str(input("Show graph? (y/n)"))

print(j)

if shw == "y":

    plt.title("...")

    plt.ylabel("Percentage of non-wanted str spaces")

    plt.xlabel("Lenght of the variable")

    plt.grid()

    plt.show()

else:

    l_teste = ["_"]

    print(l_teste.count(" "))

    sys.exit()
