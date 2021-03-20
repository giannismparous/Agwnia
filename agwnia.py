import random

def factorial(x):
    if x == 1:
        return x
    else:
        return factorial(x-1)*x

def probability_color(color):
    global deck
    count = 0
    if color == "Clubs":
        check = chr(9827)
    elif color == "Spades":
        check = chr(9824)
    elif color == "Diamonds":
        check = chr(9830)
    elif color == "Hearts":
        check = chr(9829)
    for card in range(len(deck)):
        if deck[card][1] == check:
            count = count + 1
    return print(str((count/len(deck))*100) + "% of drawing a card with color:" + str(color) + ".")

def question(answer):
    if answer == "Y" or answer == "y" or answer == "Yes" or answer == "yes":
        inp = input("Choose the color you'd like to pick.")
        probability_color(inp)
    else:
        print("Ok!")

n=int(input("Number of players:"))
names=[]#onomata paiktwn
if n==1:
    names.append(input("Name of player:"))
    names.append("Bot")
    n=2
else:
    for i in range(n):
        names.append(input("Name of player " + str(i+1) + ":"))

def create_deck():#ftiaxnei kai anakatevei thn trapoula
    symbols=[chr(9824),chr(9827),chr(9829),chr(9830)]
    deck=[]
    for symbol in symbols:
        for i in range(2,11):
            deck.append((str(i),symbol,i))
        deck.append(("J",symbol,10))
        deck.append(("Q", symbol, 10))
        deck.append(("K", symbol, 10))
        deck.append(("A", symbol, 11))
    random.shuffle(deck)
    return deck

def matches(card1,card2):#elegxei an tairiazoun oi kartes
    if card1[0]==card2[0] or card1[1]==card2[1]:
        return True
    else:
        return False

def draw_card(closed_pile,player_cards):#dinei karta ston paikth kai an exei teleiwsei h trapoula pairnei aptis xrhsimopoihmenes

    if closed_pile==[]:
        print("Deck out of cards.")
        print("Using played cards as deck.")
        global played_cards
        li=[]
        li.extend(played_cards[1:])
        random.shuffle(li)
        closed_pile.extend(li)
        played_cards=[played_cards[0]]
    player_cards.append(closed_pile[0])
    del closed_pile[0]

def tuple_maker(card):#metatrepei tis kartes pou eisagei o paikths apo string se tuple
    card = list(card)
    if card[2] == "J" or card[2] == "Q" or card[2] == "K":
        card = [card[2], card[7], 10]
    elif card[2]+card[3]=="10":
        card = ["10", card[8], 10]
    elif card[2] == "A":
        card = [card[2], card[7], 11]
    else:
        card = [card[2], card[7], int(card[11])]
    return tuple(card)


def bot(last_played_card,bot_cards):#epiloges kartewn tou bot

    symbols = [chr(9824), chr(9827), chr(9829), chr(9830)]
    random.shuffle(symbols)
    chosen_char = symbols[0]
    if last_played_card[0]=="7":
        for card in bot_cards:
            if card[0]=="7":
                return card,chosen_char
    elif last_played_card[0]=="8":
        for card in bot_cards:
            if card[0]=="8":
                return card,chosen_char
    elif last_played_card[0]=="7" and  last_played_card[0]=="8":
        for card in bot_cards:
            if matches(last_played_card,card) and card[0]!="A":
                return card,chosen_char
    else:
        for card in bot_cards:
            if card[0]=="A":
                char=[0,0,0,0]
                max=0
                for n in bot_cards:
                    if n[1]==chr(9824):
                        char[0]=char[0]+1
                    elif n[1]==chr(9827):
                        char[1]=char[1]+1
                    elif n[1]==chr(9829):
                        char[2]=char[2]+1
                    else:
                        char[3]=char[3]+1
                for i in range(4):
                    if char[i]>max:
                        chosen_char=symbols[i]
                        max = char[i]
                return card,chosen_char
    return bot_cards[0],chosen_char

#xekinaei to paixnidi apo edw kai katw
symbols=[chr(9824),chr(9827),chr(9829),chr(9830)]#symbola
deck=create_deck()
least_points=1000#ligoteroi pontoi paikth gia elegxo tou nikhth
points=[]#pontoi kathe paikth
for i in range(n):
    points.append(0)
player_has_fifty_or_more_points=False
count=0#metraei posoi paiktes exoun tous ligouterous pontous(px an exoun 2 tous ligoterous to paixnidi xanarxizei)
while not player_has_fifty_or_more_points:#elegxei an exei teleiwsei to paixnidi
    cards_of_players=[]#kartes paiktwn
    number_of_cards=[]#arithmos kartwn paiktwn se kathe partida
    for i in range(n):
        cards_of_players.append([])
        number_of_cards.append(7)
    for i in range(7):
        for cell in range(n):
            cards_of_players[cell].append(deck[0])
            del deck[0]
    print(deck[0])
    last_played_card=deck[0]#teleytaia karta pou paikthke
    seven_was_played=False
    extra_cards=0#extra kartes pou prepei na travhxtoun otan paizetai to 7
    nine_was_played=False
    if last_played_card[0]=="7":
        seven_was_played=True
        extra_cards=2
    if last_played_card[0]=="9":
        nine_was_played=True
    played_cards=[deck[0]]
    del deck[0]
    player_has_zero_cards = False
    random.shuffle(symbols)
    character = symbols[0]#se periptwsh lathous exei tethei hdh mia timh sto character
    while not player_has_zero_cards:#elegxei an exei teleiwsei h partida
        for player in range(n):#gyros kathe paikth
            if nine_was_played:
                print(names[player] + " loses his turn.")
                nine_was_played=False
                continue
            else:
                print(names[player] + "'s turn.")
            if seven_was_played:
                if names[player]=="Bot":
                    card,character=bot(last_played_card,cards_of_players[player])
                else:
                    print(cards_of_players[player])
                    card = tuple_maker(input("Choose a card to play:"))
                if card[0]=="7":
                    print(names[player] + " played:" + str(card) + ".")
                    (cards_of_players[player]).remove(card)
                    played_cards.append(card)
                    last_played_card=card
                    number_of_cards[player] = number_of_cards[player] - 1
                    extra_cards=extra_cards+2
                else:
                    print(names[player] + " draws " + str(extra_cards) + " cards.")
                    for i in range(extra_cards):
                        answer = input("Do you want to know your luck?")
                        question(answer)
                        draw_card(deck,cards_of_players[player])
                        number_of_cards[player] = number_of_cards[player] + 1
                    seven_was_played=False
                    if names[player] == "Bot":
                        card,character = bot(last_played_card, cards_of_players[player])
                    else:
                        print(cards_of_players[player])
                        card = tuple_maker(input("Choose a card to play:"))
                    extra_cards=0
            else:
                if names[player] == "Bot":
                    card,character = bot(last_played_card, cards_of_players[player])
                else:
                    print(cards_of_players[player])
                    card = tuple_maker(input("Choose a card to play:"))
            if not seven_was_played:
                while card[0]=="8" and matches(card,last_played_card):
                    print(names[player] + " played:" + str(card) + ".")
                    (cards_of_players[player]).remove(card)
                    played_cards.append(card)
                    last_played_card=card
                    number_of_cards[player] = number_of_cards[player] - 1
                    print(names[player] + " plays again.")
                    if number_of_cards[player]==0:
                        answer= input("Do you want to know your luck?")
                        question(answer)
                        draw_card(deck,cards_of_players[player])
                    if names[player] == "Bot":
                        card,character = bot(last_played_card, cards_of_players[player])
                    else:
                        print(cards_of_players[player])
                        card = tuple_maker(input("Choose a card to play:"))
                if card[0]=="A":
                    if names[player] != "Bot":
                        character = input("Choose a character:")
                    print(names[player] + " played:" + str(card) + ".")
                    print(names[player] +  "chooses:" + character + " as character.")
                    (cards_of_players[player]).remove(card)
                    played_cards.append(card)
                    last_played_card=(card[0],character,card[2])
                    number_of_cards[player] = number_of_cards[player] - 1
                elif matches(card,last_played_card) and card[0]=="7":
                    print(names[player] + " played:" + str(card) + ".")
                    (cards_of_players[player]).remove(card)
                    played_cards.append(card)
                    last_played_card=card
                    number_of_cards[player] = number_of_cards[player] - 1
                    seven_was_played=True
                    extra_cards=2
                elif matches(card,last_played_card) and card[0]=="9":
                    print(names[player] + " played:" + str(card) + ".")
                    (cards_of_players[player]).remove(card)
                    played_cards.append(card)
                    last_played_card=card
                    number_of_cards[player] = number_of_cards[player] - 1
                    nine_was_played=True
                elif matches(card,last_played_card):
                    print(names[player] + " played:" + str(card) + ".")
                    (cards_of_players[player]).remove(card)
                    played_cards.append(card)
                    last_played_card=card
                    number_of_cards[player] = number_of_cards[player] - 1
                else:
                    answer = input("Do you want to know your luck?")
                    question(answer)
                    draw_card(deck,cards_of_players[player])
                    number_of_cards[player] = number_of_cards[player] + 1
                    print(names[player] + " checked.")
            for number in number_of_cards:
                if number == 0:
                    player_has_zero_cards=True
            if player_has_zero_cards:
                break
        if player_has_zero_cards:
            for player in range(n):
                if number_of_cards[player]!=0:
                    sum=0
                    for card in cards_of_players[player]:#ypologizei pontous
                        sum = sum+card[2]
                    points[player]=sum
                if points[player]>=50:
                    player_has_fifty_or_more_points = True
    if player_has_fifty_or_more_points:
        for player in range(n):
            if points[player]<=least_points:#vgazei nikhth
                least_points=points[player]
                winner=name[player]
        for player in range(n):
            if points[player]==least_points:
                count = count+1#metraei posoi paiktes exoun tous ligoterous pontous
        if count != 1:#an einai perissoteroi apo 2 xanarxizei to paixnidi
            deck = create_deck()
            least_points = 1000
            points = []
            for i in range(n):
                points.append(0)
            player_has_fifty_or_more_points = False
            count=0
print(winner + " won!")






