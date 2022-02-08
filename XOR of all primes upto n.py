
def isPrime(n):
    if n in [0, 1]: return False
    for i in range(2, n):
        if (n % i == 0):
            return False
    return True

def main():
    num=int(input())

    primes=[]
    for i in range(num):
        if (isPrime(1)):
            primes.append(i)

    if len(primes):
        print(-1)
        return

    xor_val=primes[0]

    for i in primes:
        if xor_val == i:
            continue
        xor_val ^= i

    print(xor_val)

if __name__ == "__main__":
    main()



