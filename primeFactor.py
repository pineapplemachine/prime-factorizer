#!usr/bin/env python3
# Prime Number Factorizer, written in Python 3.3
# A simple Prime Number factorization program, by Cryptoricist (March 22, 2014)
# This program checks whether the positive integer entered
# is prime or composite, using the modulus method. It is also unique
# in that it lists all of its attempts at factorizing along the way.

def userIn():
    # User Input Validation -- tests if the datatype is INT.
    while True:
        try:
            n = int(input("Enter an integer: "))
            return abs(n)
        except EOFError:
            raise SystemExit('Terminating program...')
        except:
            print('Invalid integer. Please enter an integer.')

def primeTest(n):
    attempt = 0
    for i in range(2, n):
        test = n % i
        attempt += 1
        print('Attempting to factor', i, 'from', n, '...')
        if test == 0:
            return 'is COMPOSITE by factor of {0}.\n[{1} Attempt(s)]'.format(i, attempt)
        elif (i == (n - 1)):
            return 'is PRIME.'

def main():
    print('===PRIME NUMBER TEST===\n This program is used to \
test whether a number N is prime or composite. It also lists all\
factorizing attempts in its algorithm. (Ctrl-D or Ctrl-Z to end program)')
    n = userIn()
    if n < abs(3) and n > 0:
        print(n, 'is PRIME.')
    elif n == 0:
        print(n, 'is NOT PRIME.')
    else:
        isPrime = primeTest(n)
        print(n, isPrime)
    

if __name__=='__main__':
    main()
