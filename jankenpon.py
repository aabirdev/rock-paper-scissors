import random

sp = 0
sc = 0 


def game():
    print("1: SCISSORS | 2: ROCK | 3: PAPER")
    ch = int(input("Input the corresponding number: "))
    str = ""
    cstr = ""
 
    global sp 
    global sc
    
    

    
    while ch<=0 and ch>=4:
        ch = int(input("Input a valid number: "))
    
    if ch == 1:
        str = "SCISSORS"
    elif ch == 2:
        str = "ROCK"
    elif ch == 3:
        str = "PAPER"
    
    cch = random.randint(1,3)
    
    if cch == 1:
        cstr = "SCISSORS"
    elif cch == 2:
        cstr = "ROCK"
    elif cch == 3:
        cstr = "PAPER"    
    
    if ch == cch:
        print("TIE")
        
    print("PLAYER PLAYS", str)
    print("COMPUTER PLAYS", cstr)
        
    #computer win cases
    if ch == 1 and cch == 2:
        print("COMPUTER WINS")
        sc = sc+1
    elif ch == 2 and cch == 3:
        print("COMPUTER WINS")
        sc = sc+1
    elif ch == 3 and cch == 1:
        print("COMPUTER WINS")    
        sc = sc+1
        
    #player win cases
    elif cch == 1 and ch == 2:
        print("PLAYER WINS")
        sp = sp+1
    elif cch == 2 and ch == 3:
        print("PLAYER WINS")
        sp = sp+1
    elif cch == 3 and ch == 1:
        print("PLAYER WINS")    
        sp = sp+1
   
def turnin():
    print("Input number of turns you want to play for")
    turns = int(input("Input here: "))
    
    for _ in range(turns):
        game()
        
        
    
    print("PLAYER:", sp, "|", "COMPUTER:", sc)
    
    if sp>sc:
        print("PLAYER WINS THIS MATCH")
    if sc>sp:
        print("COMPUTER WINS THIS MATCH")
    else:
        print("TIE")
        
        


turnin()