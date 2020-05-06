# Given reversed_number 32-bit signed integer, reverse digits of an integer.

#Example input: 123 output: 321
#Example input: -123 output: -321
#Example input: 120 output: 21

#Naive solution: push and pop method
#Time complexity 0(n)

#We can use pythons built in reverse method 

#Function parameter will be set to an integer
# if number is positive then simply reverse number with built in reverse method
# if number is negative reverse the number and then mulitply by -1
#Also check to see if number is in the range of -2^32 to 2^32
#if the number is not in the range then return 0 else return reversed integer





def reverse_int(x:int) -> int:

    if x > 0:
        reversed_number = int(str(x)[::-1])

    if x < 0:
        reversed_number = -1 * int(str(x * -1)[::-1])

    minimum = -2**31
    maximum = 2**31 -1

    if reversed_number not in range(minimum, maximum):
        return 0
    else:
        return reversed_number



def main():
    number = input("Enter Number: ")
    print(reverse_int(number))

    #Variable Tables:
    #print(reverse_int(2324)) => Returns 4232
    #print(reverse_int(56)) => Returns 65
    #print(reverse_int(1000)) => Returns 0
    #print(reverse_int(2**38, 2**40)) => Returns 0

if __name__ == "__main__":
    main()