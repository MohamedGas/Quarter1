def main():
    xmethod(1)


def xmethod(n):
    if n > 0:
        xmethod(n - 1)

        print(n)


main()
