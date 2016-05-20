#File:creditcard86448.py
#Author:Simmy Payyappilly Varghese,Student ID:86448
#This is a program to validate credit card number.A credit card must have between 13 and 16 digits. It must start with 4-Visa Crad,5 for Master cards,37 for American Express cards,6 for Discover cards
#Modified Date:03/24/2015-Added cardNum.isdigit() verification to isValid function-To avoid program crash when invalid num spl alphanumeric input is given
def main():
    cardNum=input("Enter a credit card number:")
    if isValid(cardNum):
        print("This a good ",end="")
    else:
        print("This an invalid ",end="")
    if cardNum[0]=='4':                                                      #Prints the type of credit card based on first digits.If 4-Visa Crad,5 for Master cards,37 for American Express cards,6 for Discover cards
        print("Visa card number ")
    elif cardNum[0]=='5':
        print("MasterCard card number")
    elif cardNum[0]=='6':  
        print("Discover card number")
    elif cardNum[:2]=='37':
        print("American Express card number")
    else:
        print("card number")                                                 #If card number is invalid,prints "This is invalid number"


def isValid(cardNum):
    """:param cardNum-Credit card Number enter by user(String)
       :return True or False-True if card is valid else False                 
    """
                                                                              #Without cardNum.isdigit() program will crash for alphanumeric input
    if len(cardNum)>=13 and len(cardNum)<=16 and cardNum.isdigit()            #Valid card must have number of digits is between 13 and 16
       total=sumOfEvenPosition(cardNum)+sumOfOddPosition(cardNum)
       if (total%10==0):                                                      #Modulus 10 check-Valid cars must have sum of even and odd indexed digits must be divisible by 10
           return True
       else:
           return False

    else:
        return False


def sumOfEvenPosition(cardNum):
    """:param cardNum-Credit card Number enter by user(String)
       :return sumEven-Sum of the product of even indexed digits multiplied by 2
    """
    sumEven=0
    for i in range(-2,-len(cardNum)-1,-2):                                    #Every second digit from right to left(Array begns with -1 and ens with -len(cardNum)-1) is multiplied by 2
       product=eval(cardNum[i])*2
       if product>9:
          product=getDigitSum(product)  
       sumEven=sumEven+product
    return sumEven


def getDigitSum(product):                                                    #If product is two digit number,sum up the digits and is assigned to same variable product
    """:param product-Product of every even indexed digits multiplied by two
       :return product-Sum of the digits ,for two digit products
    """
    product=product//10+product%10
    return product


def sumOfOddPosition(cardNum):
    """:param cardNum-Credit card Number enter by user(String)
       :return sumOdd-Sum of the odd indexed digits 
    """
    sumOdd=0
    for i in range(-1,-len(cardNum)-1,-2):                                     #Sum up every odd indexed digits from right to left
       sumOdd=sumOdd+eval(cardNum[i])
    return sumOdd

main()
