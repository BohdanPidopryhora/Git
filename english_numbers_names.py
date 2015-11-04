FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"
if __name__ == '__main__':
    while True:
            number = int(raw_input("Number? "))
            leng = len(str(number))
            result = ""
            if leng == 1:
                result += FIRST_TEN[number-1]
            if leng == 2:
                if number < 20:
                    result += SECOND_TEN[number-10]
                else:
                    result += OTHER_TENS[(number//10)-2]
                    if number - (number//10)*10:
                        result += " " + FIRST_TEN[(number - (number//10)*10)-1]
            if leng == 3:
                if int(str(number)[1:]) == 0:
                    result += FIRST_TEN[number//100-1]
                    result += " " + HUNDRED
                else:            
                    result += FIRST_TEN[number//100-1]
                    result += " " + HUNDRED + " "
                    number = int(str(number)[1:])
                    if len(str(number)[1:]) == 1:
                        if number < 20:
                            result += SECOND_TEN[number-10]
                        else:
                            result += OTHER_TENS[(number//10)-2]
                            if number - (number//10)*10:
                                result += " " + FIRST_TEN[(number - (number//10)*10)-1]
                    else:
                        result += FIRST_TEN[number-1]
            print result

    
