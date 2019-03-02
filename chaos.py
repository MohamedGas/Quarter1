def main():
        x=eval(input("Please Enter Any number between 0 and 1: "))
        for n in range(10):
            x=3.9*x*(1-x)
            print(x)

main()
