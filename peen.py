from math import exp
from time import sleep

d_siz = 0.00
while True:
    try:
        d_siz = float(input("How big the dic? (inches)\n"))
    except:
        print("error: the dic no real :(, try again bit")
    if d_siz > 0:
        break

sexy = 0

if d_siz > 5.5:
    print("wow big dic")
    sexy = 2
elif 5.5 >= d_siz >= 5.2:
    print("A V E R A G E")
    sexy = 1
else:
    print("haha tiny")

print("8", end="")
for i in range(int(exp(d_siz)/30)):
    print("=", end="")
    if i > d_siz*10:
        break
print("D")
sleep(2)
if input("\nwell, thats all folks! good? (y/n): ") == "n":
    print("too bad, fuc off")
else:
    print("gud")
input()