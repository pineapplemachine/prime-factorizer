#!usr/bin/env python3
# Prime Number Factorizer, written in Python 3.3
# A simple Prime Number factorization program, by Cryptoricist (March 22, 2014)
# Modified by Sophie Kirschner (April 20, 2014)
# This program checks whether the positive integer entered is prime.
# The pertinent method returns the reason for its being composite, if one exists.

def userIn():
    # User Input Validation -- tests if the datatype is INT.
    while True:
        try:
            n = int(input("Enter an integer: "))
            return abs(n)
        except EOFError:
            raise SystemExit('Terminating program...')
        except:
            print('Invalid integer. Please enter an integer.\n')

def primeTest(number):
    # check if primality can be defined for this number
    if int(number)!=number:
        return 'Primality not defined for this number. (Not an integer.)'
    if number<2:
        return 'Primality not defined for this number. (Less than 2.)'
    # test for mod 2 and mod 3
    if (number%2==0):
        return 'Number is composite. (Multiple of 2.)'
    if (number%3==0):
        return 'Number is composite. (Multiple of 3.)'
    # iterate through possible prime factors up to sqrt(number)
    goal=int(number**0.5)
    i=5
    while (i<=goal):
        # check if i is a factor
        if (number%i==0):
            return 'Number is composite. (Multiple of '+str(i)+'.)'
        # check if i+2 is a factor
        if (number%(i+2)==0):
            return 'Number is composite. (Multiple of '+str(i+2)+'.)'
        # go on to the next pair of numbers
        i+=6
    return 'Number is prime. (Found no factors.)'

def main():
    print('===PRIME NUMBER TEST===\nThis program tests whether a number N is prime.\n')
    while True:
        n = userIn()
        isPrime=primeTest(n)
        print(n, ":", isPrime, "\n")
    

if __name__=='__main__':
    main()