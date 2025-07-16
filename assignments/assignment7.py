def right_triangle(lines):
    for i in range(1, lines+1):
        print("*" * i)


def equilateral_triangle(lines):
    for i in range(1, lines+1):
        print(" "*(lines-i) + "*"*(2*i - 1))

def hollow_square(n):
    for i in range(n):
        if i == 0 or i == n-1:
            print("*" * n)
        else:
            print("*" + " "*(n-2) + "*")


def hollow_rhombus(n):
    for i in range(n):
        print(" "*(n-i-1), end="")
        if i == 0 or i == n-1:
            print("*" * n)
        else:
            print("*" + " "*(n-2) + "*")

def pascal_triangle(n):
    for i in range(n):
        print(" "*(n-i), end="")
        val = 1
        for j in range(i+1):
            print(val, end=" ")
            val = val * (i - j) // (j + 1)
        print()



def x_shape(n):
    for i in range(n):
        for j in range(n):
            if i == j or j == n - i - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

def x_in_hollow_square(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or j == 0 or i == n-1 or j == n-1 or i == j or j == n-i-1:
                if n % 2 == 1 and i == j == n//2:
                    print("0", end="")
                else:
                    print("*", end="")
            else:
                print(" ", end="")
        print()

def benzene_ring(n=5):
    for i in range(n):
        print(" " * (n - i) + "*" + " " * (2 * i) + "*")
    for i in range(n-2, -1, -1):
        print(" " * (n - i) + "*" + " " * (2 * i) + "*")
