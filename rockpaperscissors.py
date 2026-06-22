import random


def round(o, t):
    if o>0 and o<4 and t>0 and t<4:
        if o == t:
            return "T"
        elif o == 1 and t == 3:
            return "W"
        elif t == 1 and o == 3:
            return "L"
        elif o>1:
            if o-1 == t:
                return "W"
            else:
                pass
        elif t>1:
            if t-1 == o:
                return "L"
        

def player_choice():
    inputting = True
    while inputting:
        pc = (input("Enter your choice: "))
        if pc not in ["1","2","3"]:
            print("Invalid choice, re-enter in acceptable range")    
        else:
            inputting = False   
    return int(pc)

def computer_choice(pro, ppa, psc):
    moves = [1, 2, 3]
    cc = random.choices(moves, weights=[pro,ppa,psc], k=1)[0]
   # print(f"Computer played { cc }")
    return cc

def game():
    print("1 for Rock, 2 for Paper, 3 for Scissors")
    playing = True

    plr = 1
    plp = 1
    pls = 1
    ps = 0
    cs = 0

    while playing:
        cc = computer_choice(plr,plp,pls)
       # print(f"Weightage of moves is: \nRock:{plr}\tPaper:{plp}\tScissors:{pls}")
        pc = player_choice()

        if pc == 1:
            plp+=1
        elif pc == 2:
            pls +=1
        elif pc == 3:
            plr +=1

        results = round(pc, cc)

        if results == "W":
            print("You Win!")
            ps+=1
        elif results == "L":
            print("You Lose :(")
            cs+=1
        elif results == "T":
            print("Tied")


        print(f"Current Score\nPlayer Score: {ps} \t Computer Score: {cs}")
        ch = input("R to play another round, Q to quit: ")

        if ch == "R":
            playing = True
        elif ch == "Q":
            playing = False

def main():
    game()

if __name__ ==  "__main__":
    main()
        