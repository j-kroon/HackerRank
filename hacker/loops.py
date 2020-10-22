def fruityLoop(n):
    """
    for all non-negative integers i < n, print i^2
    """
    for i in range(n):
        print(i*i)
    return


def main():
    print("Hello, World!")
    
    n = int(input())
    fruityLoop(n)

    print("Goodbye, World!")

if __name__ == '__main__':
    main()