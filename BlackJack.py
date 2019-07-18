from  random  import shuffle

card_chars=['┌','─', '┐','│','░','└','┘','♠', '♥', '♣', '♦']
deck = list(range(52))
shuffle(deck)

a = "┌─────────┐"
b = "│░░░░░░░░░│"
i = "└─────────┘"

dealers_hand=[]
dealers_hand.append(deck.pop())
dealers_hand.append(deck.pop())

players_hand=[]
players_hand.append(deck.pop())
players_hand.append(deck.pop())

score_value = 0

###################################################################

def cardsuit(card):
    if card//13 == 0:
        suit = "♠"
    elif card//13 == 1:
        suit = "♥"
    elif card//13 == 2:
        suit = "♣"
    elif card//13 == 3:
        suit = "♦"

    value = card%13+1

    if value == 1:
        value = "A"
    if value == 11:
        value = "J"
    if value == 12:
        value = "Q"
    if value == 13:
        value = "K"

    print(a)
    print(b)
    if value == 10:
        print("│░",value,"░░░░░░│",sep="")
    else:
        print("│░░",value,"░░░░░░│",sep="")
    print(b)
    print("│░░░░",suit,"░░░░│",sep="")
    print(b)
    print(b)
    print(b)
    print(i)

###################################################################

def print_hand(dealers_hand, players_hand, hide_dealers_hand, i):
    print("This is the Dealers Hand:")

    if hide_dealers_hand == True:
        print(a)
        print(b)       
        print(b)
        print(b)
        print(b)
        print(b)
        print(b)
        print(b)
        print(i)

        cardsuit(dealers_hand[0])
    else:
        for i in range(len(dealers_hand)):
            cardsuit(dealers_hand[i])
    
    
    print("This is your hand:")

    
    for i in range(len(players_hand)):
        cardsuit(players_hand[i])

###################################################################

def hit():
    stay = input("Would you like to hit or stay? hit/stay: ")
    if str(stay) == "hit":
        shuffle(deck)
        players_hand.append(deck.pop())
        print("This is your hand")
        for i in range(len(players_hand)):
            cardsuit(players_hand[i])
        score()
        
        hit()
        
    else:
        hit_dealer()
##       score_dealer()

###################################################################

def hit_dealer():
    
    Dvalue = 0
    Dvalue2 = 0
    DAcounter = 0
    
    for i in range(len(dealers_hand)):
        if (dealers_hand[i]%13) + 1 == 1:
            Dvalue2 += 11
            Dvalue += 1
            DAcounter +=1
        elif (dealers_hand[i]%13) + 1 > 10:
            Dvalue += 10
            Dvalue2 += 10
        elif (dealers_hand[i]%13) + 1 <= 10:
            Dvalue += (dealers_hand[i]%13) + 1
            Dvalue2 += (dealers_hand[i]%13) + 1

    dealers_score = 0

    if Dvalue >= Dvalue2:
        dealers_score = Dvalue
    elif Dvalue2 > Dvalue:
        dealers_score = Dvalue2

    print("The dealers score is: ",dealers_score)

    if dealers_score < 17:
        shuffle(deck)
        dealers_hand.append(deck.pop())
        print("This is dealers's hand")
        
        for i in range(len(dealers_hand)):
            cardsuit(dealers_hand[i])
        ##score_dealer()

        hit_dealer()

    value = 0
    value2 = 0
    Acounter = 0
    
    for i in range(len(players_hand)):
        if (players_hand[i]%13) + 1 == 1:
            value2 += 11
            value += 1
            Acounter +=1
        elif (players_hand[i]%13) + 1 > 10:
            value += 10
            value2 += 10
        elif (players_hand[i]%13) + 1 <= 10:
            value += (players_hand[i]%13) + 1
            value2 += (players_hand[i]%13) + 1

    players_score = 0

    if value >= value2:
        players_score = value
    elif value2 > value:
        players_score = value2

    if DAcounter > 0:
        print("hi")
        if Dvalue2 <= 21 and players_score <= 21:
            print("Dealer's hand value is",Dvalue2)
            if Dvalue2 > players_score:
                print("Dealer WINS!")
            elif Dvalue2 == players_score:
                print("TIE!")
            elif Dvalue2 < players_score:
                print("You WIN!")
        elif Dvalue2 > 21 and score_value > 21:
            print("TIE!")
        elif Dvalue2 > 21 and score_value <= 21:
            print("You WIN!")
        elif Dvalue2 <= 21 and players_score > 21:
            print("Dealer WINS!")
            
    elif DAcounter == 0:
            
        if Dvalue <= 21 and players_score <= 21:
            print("Dealer's hand value is",Dvalue)
            if Dvalue > players_score:
                print("Dealer WINS!")
            elif Dvalue == players_score:
                print("TIE!")
            elif Dvalue < players_score:
                print("You WIN!")
        elif Dvalue > 21 and players_score > 21:
            print("TIE!")
        elif Dvalue > 21 and players_score <= 21:
                print("You WIN!")
        elif Dvalue <= 21 and players_score < 21:
            print("Dealer WIN!")

    return players_score
    return Dvalue
    return Dvalue2
    return dealers_score
    return value
    return value2
    return DAcounter


###################################################################

def score():
    value = 0
    value2 = 0
    Acounter = 0
    
    for i in range(len(players_hand)):
        if (players_hand[i]%13) + 1 == 1:
            value2 += 11
            value += 1
            Acounter +=1
        elif (players_hand[i]%13) + 1 > 10:
            value += 10
            value2 += 10
        elif (players_hand[i]%13) + 1 <= 10:
            value += (players_hand[i]%13) + 1
            value2 += (players_hand[i]%13) + 1

    if Acounter > 0:
        print("Your hand's value is",value,"or",value2)
        
    elif Acounter == 0:
        print("Your hand's value is",value)

    return value
    return value2

    players_score = 0

    if value >= value2:
        players_score = value
    elif value2 > value:
        players_score = value2
        
    return players_score

        
###################################################################


print_hand(dealers_hand, players_hand, True, i)

score()

hit()

















