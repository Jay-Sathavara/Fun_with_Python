# JP0030

def nearestMultiple(num):
    if num >= 4:
        near = num + (4 - (num % 4))
    else:
        near = 4
    return near
 
def lose1():
    print ("\n\nYOU LOSE !")
    print("Better luck next time !")
    exit(0)
     
# checks whether the numbers are consecutive
def check(xyz):
    i = 1
    while i<len(xyz):
        if (xyz[i]-xyz[i-1])!= 1:
            return False
        i = i + 1
    return True
 
# starts the game
def start1():
    xyz = []
    last = 0
    while True:
        print ("Enter 'F' to take the first chance.")
        print("Enter 'S' to take the second chance.")
        chance = input('> ')
         
        # player takes the first chance
        if chance == "F":
            while True:
                if last == 20:
                    lose1()
                else:
                    print ("\nYour Turn.")
                    print ("\nHow many numbers do you wish to enter?")
                    inp = int(input('> '))
                     
                    if inp > 0 and inp <= 3:
                        comp = 4 - inp
                    else:
                        print ("Wrong input. You are disqualified from the game.")
                        lose1()

                        
                    i, j = 1, 1
 
                    print ("Now enter the values")
                    while i <= inp:
                        a = input('> ')
                        a = int(a)
                        xyz.append(a)
                        i = i + 1
                     
                    # store the last element of xyz.
                    last = xyz[-1] 
                     
                    # checks whether the input 
                    # numbers are consecutive
                    if check(xyz) == True: 
                        if last == 21:
                            lose1()
                             
                        else:
                            #"Computer's turn."
                            while j <= comp:
                                xyz.append(last + j)
                                j = j + 1
                            print ("Order of inputs after computer's turn is: ")
                            print (xyz)
                            last = xyz[-1]
                    else:
                        print ("\nYou did not input consecutive integers.")
                        lose1()