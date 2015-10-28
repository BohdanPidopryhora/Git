# Git
FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"

def first(digit):
    return FIRST_TEN[digit-1]

def second(digit):
    return SECOND_TEN[digit-1]

def others(digit):
    return OTHER_TENS[digit-2]


def checkio(number):
    result = ""
    if len(str(number)) == 1:
        result += first(number)
    if len(str(number)) == 2:
        if 9 < number < 19:
            result += second(number-9)
        else:
            result += others(number/10) + " "
            result += first(number-(number/10)*10)
    if len(str(number)) == 3:
        result += first(number/100) + " "
        result += HUNDRED + " "
        number = number - (number/100)*100
        if 9 < number < 19:
            result += second(number-9)
        else:
            result += others(number/10) + " "
            result += first(number-(number/10)*10)        


    print result


    
    #result = ""
    #if number/100 >= 1:
        #result += FIRST_TEN[number/100-1] + " "
        #result += HUNDRED + " "
        #number -= (number/100)*100
   
    #if number:
        #if number/10 >= 1:
            #if number/10 == 1:
               # result += SECOND_TEN[(number/10)*10]
                
       # print result 
checkio(33)
checkio (1)
checkio(13)
checkio (999)
checkio (100)

