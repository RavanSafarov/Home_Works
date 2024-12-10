from random import randint

#Task1

#print("Enter the number. You have only 10 chances. If you want, you can end the game by entering 0. Good luck!!!")
#zero = 0
#random = randint(1, 100)
#while zero<=10:
    #zero +=1
    #userint = int(input("Enter the number: "))
    #if userint == random:
        #print("You won!!!")
        #break
    #elif userint > random:
        #print("Number is greater than chosen")
    #elif userint < random:
        #print("Number is less than chosen")
    #if userint == 0:
        #print("You ended the game!")
        #break
    #if zero == 10:
        #print("You don't have any chances.You lose!!!")
        #break



#Task2

#print("Enter the numbers begin and end. You have chances which are depend on chosen difficulty: easy(15) , normal(10), or hard(5).Good luck!!!")

#begin = int(input("Chose the number from which  you want start: "))
#end = int(input("Chose the number from which  you want end: "))

#if begin >= end:
    #print("Error!!! The start number must be less than the end number.")
#else:
    #level = str(input("Choose difficulty: easy, normal, or hard "))
    #random = randint(begin, end)
    #zero = 0
    #while zero <= 15:
        #zero += 1
        #answer = int(input("Chose the answer: "))
        #if answer == random:
            #print("You won!!!")
            #break
        #elif level == "easy" and zero == 15:
            #print("You don't have any chances.You lose!!!")
            #break
        #elif level == "normal" and zero == 10:
            #print("You don't have any chances.You lose!!!")
            #break
        #elif level == "hard" and zero == 5:
            #print("You don't have any chances.You lose!!!")
            #break
        #elif answer > random:
            #print("Number is greater than chosen")
            #if answer - random <= 10:
                #print("But,you are close")
            #else:
                #print("You are far")
        #elif answer < random:
            #print("Number is less than chosen")
            #if random - answer <= 10:
                #print("But,you are close")
            #else:
                #print("You are far")

