# from cs50 import get_int


def main():
    i = get_positive_int()
    print(i)


# Prompt user for positive integer
def get_positive_int():
    while True:
        # n = get_int("Positive Integer: ")
        n = int(input("Positive Integer: "))
        if n > 0:
            break
    return n


if __name__ == "__main__":
    main()
