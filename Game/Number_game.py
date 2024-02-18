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