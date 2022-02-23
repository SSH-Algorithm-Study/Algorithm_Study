def dot(n):
    if n == 0:
        for _ in range(n):
            print("*", end="")
        print("\n")
        for _ in range(n):
            print("*", end="")
            print(" *")
        print("\n")
        for _ in range(n):
            print("*", end="")
        print("\n")
        return

    else:
        return dot(n//3)


dot(9)


