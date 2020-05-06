#Determine whether an integer is a palindrome. An integer is a palindrome when 
#it reads the same backward as forward.

#Example Input: 121 output: True
#Example Input -121 output: False




def is_palindrome(x:int)-> int:
    number = str(x)
    reversed_number = ''.join(list(reversed(number)))
    if reversed_number != number:
        return False
    else:
        return True



def main():
    number = input("Enter a number: ")
    is_palindrome(number)

    #Variable Tables:
        #print(is_palindrome(232)) => Returns True
        #print(is_palindrome(23032)) => Returns True
        #print(is_palindrome(23)) => Returns False
        #print(is_palindrome(24533452)) => Returns True


if __name__ == "__main__":
    main()

