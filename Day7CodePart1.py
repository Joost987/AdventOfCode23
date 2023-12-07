def FindType(card):
    cardlength=len(card)
    setlength=len(set(card))
    if setlength==cardlength:
        return 0 #high card
    elif setlength==cardlength-1:
        return 1 #one pair
    elif setlength==cardlength-2:
        for individcard in set(card):
            if list(card).count(individcard)==3:
                return 3
        return 2
        #either two pair or three of a kind
    elif setlength==cardlength-3:
        for individcard in set(card):
            if list(card).count(individcard)==3:
                return 4
        return 5
        #either full house or four of a kind
    elif setlength==cardlength-4:
        return 6 #five of a kind
    
def Orderkey(card):
    orderlst=[ordering[card[i]]*15**(len(card)-i) for i in range(len(card))]
    return sum(orderlst)



f=open("Day7Input.txt")
biddict={}
cardslst=[]
ordering={"2":2,"3":3,"4": 4, "5":5,"6":6,"7":7,"8":8,"9":9,"T":10,"J":11,"Q":12,"K":13,"A":14}
for line in f:
    cards,bid=line.split(" ")
    bid=int(bid)
    biddict.update({cards:bid})
    cardslst.append(cards)
    
cardstyped=[[] for i in range(7)] #first sort the cards according to their type
for card in cardslst:
    cardstyped[FindType(card)].append(card)
for i in range(7):
    cardstyped[i].sort(key=Orderkey)

cardslst=[card for cardstype in cardstyped for card in cardstype]
print(sum([(i+1)*biddict[cardslst[i]] for i in range(len(cardslst))]))