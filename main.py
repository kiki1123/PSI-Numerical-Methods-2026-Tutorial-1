# Hello World for PSI Numerical Methods 2026
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 2* np.pi, .1)
y1 = np.sin(x)
y2 = np.cos(x)

fig = plt.figure()
plt.plot(x, y1, color='g',label='sin')
plt.plot(x, y2, color='r', label='cos')
plt.legend()
plt.savefig("trig.png")

print(np.exp(1.2))
print("Hello PSI 2026!")

def myexp(x, N=10):
    """
    This function computes exp(x) via the Taylor Series using terms up to
    order N.
    """

    t = 1.0  # The value of the current term
    y = 1.0  # The value of exp(x) up to this point

    # We initialize with the 0th order term, so run the loop
    # for the remaining N terms.
    for i in range(1, N+1):
        t *= x/i  # Update the term: tn = x^n / n!
        y += t    # add tn to y

    # We're done!
    return y


if __name__ == "__main__":

    print("Hello, world!")

    print("e(1) with  5 terms is", myexp(1.0, 5))
    print("e(1) with 10 terms is", myexp(1.0, 10))
    print("e(1) with 20 terms is", myexp(1.0, 20))
    print("e(1) with 40 terms is", myexp(1.0, 40))
