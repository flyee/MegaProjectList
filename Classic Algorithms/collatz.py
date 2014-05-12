def main():
    while True:
        n = int(input("Input a number: "))
        steps = 0

        if n < 1:
            break;
    
        while n != 1:
            print(n, end=' -> ')
            steps += 1
            if n % 2 == 0:
                n = n // 2
            else:
                n = n * 3 + 1
    
        print(n)
        print("Steps: %d" % steps)

if __name__ == '__main__':
    main()
