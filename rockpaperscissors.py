import random


def winner(o, t):
        if o == t:
            return "T"
        elif o == 1 and t == 3:
            return "W"
        elif t == 1 and o == 3:
            return "L"
        if o>t:
            if o>1:
                if o-1 == t:
                    return "W"
        if t>o:           
            if t>1:
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
            plp+=0.1
        elif pc == 2:
            pls +=0.1
        elif pc == 3:
            plr +=0.1

        results = winner(pc, cc)

        if results == "W":
            print("You Win!")
            ps+=1
        elif results == "L":
            print("You Lose :(")
            cs+=1
        elif results == "T":
            print("Tied")


        print(f"Current Score\nPlayer Score: {ps} \t Computer Score: {cs}")

        while True:
            ch = input("R to play another round, Q to quit: ")
            ch = ch.lower().strip()
            if ch not in ["r", "q"]:
                print("Invalid input, please re-enter the letters R or Q (Case does not matter)")
            else:
                if ch == "r":
                    playing = True
                    break   
                elif ch == "q":
                    playing = False
                    break

def main():
    game()

if __name__ ==  "__main__":
    main()
        
