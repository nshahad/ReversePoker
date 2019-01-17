import random
import time


def getcard(x):
    if x == 1:
        return '2C'
    elif x == 2:
        return '3C'
    elif x == 3:
        return '4C'
    elif x == 4:
        return '5C'
    elif x == 5:
        return '6C'
    elif x == 6:
        return '7C'
    elif x == 7:
        return '8C'
    elif x == 8:
        return '9C'
    elif x == 9:
        return 'TC'
    elif x == 10:
        return 'JC'
    elif x == 11:
        return 'QC'
    elif x == 12:
        return 'KC'
    elif x == 13:
        return 'AC'
    elif x == 14:
        return '2D'
    elif x == 15:
        return '3D'
    elif x == 16:
        return '4D'
    elif x == 17:
        return '5D'
    elif x == 18:
        return '6D'
    elif x == 19:
        return '7D'
    elif x == 20:
        return '8D'
    elif x == 21:
        return '9D'
    elif x == 22:
        return 'TD'
    elif x == 23:
        return 'JD'
    elif x == 24:
        return 'QD'
    elif x == 25:
        return 'KD'
    elif x == 26:
        return 'AD'
    elif x == 27:
        return '2H'
    elif x == 28:
        return '3H'
    elif x == 29:
        return '4H'
    elif x == 30:
        return '5H'
    elif x == 31:
        return '6H'
    elif x == 32:
        return '7H'
    elif x == 33:
        return '8H'
    elif x == 34:
        return '9H'
    elif x == 35:
        return 'TH'
    elif x == 36:
        return 'JH'
    elif x == 37:
        return 'QH'
    elif x == 38:
        return 'KH'
    elif x == 39:
        return 'AH'
    elif x == 40:
        return '2S'
    elif x == 41:
        return '3S'
    elif x == 42:
        return '4S'
    elif x == 43:
        return '5S'
    elif x == 44:
        return '6S'
    elif x == 45:
        return '7S'
    elif x == 46:
        return '8S'
    elif x == 47:
        return '9S'
    elif x == 48:
        return 'TS'
    elif x == 49:
        return 'JS'
    elif x == 50:
        return 'QS'
    elif x == 51:
        return 'KS'
    elif x == 52:
        return 'AS'

    
##########################################################
'''Defines'''
def sortvalue(x):
    sortedhand = []
    for z in range(13):
        for y in range(len(x)):
            currentcard = x[y]
            if z == 0 and currentcard[0] == 'A':
                sortedhand.append(currentcard)
            elif z == 1 and currentcard[0] == 'K':
                sortedhand.append(currentcard)
            elif z == 2 and currentcard[0] == 'Q':
                sortedhand.append(currentcard)
            elif z == 3 and currentcard[0] == 'J':
                sortedhand.append(currentcard)
            elif z == 4 and currentcard[0] == 'T':
                sortedhand.append(currentcard)
            elif z == 5 and currentcard[0] == '9':
                sortedhand.append(currentcard)
            elif z == 6 and currentcard[0] == '8':
                sortedhand.append(currentcard)
            elif z == 7 and currentcard[0] == '7':
                sortedhand.append(currentcard)
            elif z == 8 and currentcard[0] == '6':
                sortedhand.append(currentcard)
            elif z == 9 and currentcard[0] == '5':
                sortedhand.append(currentcard)
            elif z == 10 and currentcard[0] == '4':
                sortedhand.append(currentcard)
            elif z == 11 and currentcard[0] == '3':
                sortedhand.append(currentcard)
            elif z == 12 and currentcard[0] == '2':
                sortedhand.append(currentcard)
    return sortedhand     
###############################################
''' Handle A2345 Case '''
def straight(x):
    cards = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
    numbers = []
    a_nums = [] #assigned numbers
    straight = False
    straighthigh = ''
    for b in range(len(x)):
        number = x[b][0]
        numbers.append(number)
    numbers = sortvalue(numbers)
    for c in range(len(numbers)):
        for d in range(len(cards)):
            if numbers[c] == cards[d] and d not in a_nums:
                a_nums.append(d)
                break
    while len(a_nums) < 7:
        a_nums.append(500)
    if a_nums[0] == a_nums[1] - 1 and a_nums[1] == a_nums[2] - 1 and a_nums[2] == a_nums[3] - 1 and a_nums[3] == a_nums[4] - 1:
        straight = True
        straighthigh = cards[a_nums[0]]
    elif a_nums[1] == a_nums[2] - 1 and a_nums[2] == a_nums[3] - 1 and a_nums[3] == a_nums[4] - 1 and a_nums[4] == a_nums[5] - 1:
        straight = True
        straighthigh = cards[a_nums[1]]
    elif a_nums[2] == a_nums[3] - 1 and a_nums[3] == a_nums[4] - 1 and a_nums[4] == a_nums[5] - 1 and a_nums[5] == a_nums[6] - 1:
        straight = True
        straighthigh = cards[a_nums[2]]
    if straight:
        return 'straight ' + straighthigh

    else:
        return ''      
        
################################################

def quad(x):
    cards = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
    numbers = []
    quad = False
    quadvalue = ''
    highcard = ''
    for b in range(len(x)):
        #card = x[b]
        number = x[b][0]
        numbers.append(number)
    for c in range(len(cards)):
        if numbers.count(cards[c]) == 4:
            quad = True
            quadvalue = cards[c]
            break         
    if quad:
        numbers = sortvalue(numbers)
        for d in range(len(numbers)):
            if numbers[d] != quadvalue:
                highcard = numbers[d]
                break                     
        return 'quad ' + quadvalue + ' ' + highcard
    else:
        return ''
    
#######################################################    

def flush(x):
    clubs = []
    diamonds = []
    hearts = []
    spades = []
    for b in range(len(x)):
        card = x[b]
        suit = card[1]
        if suit == 'C':
            clubs.append(card)
        elif suit == 'D':
            diamonds.append(card)
        elif suit == 'H':
            hearts.append(card)
        elif suit == 'S':
            spades.append(card)
    if len(clubs) >= 5:
        clubs = sortvalue(clubs)
        add = 'flush '+clubs[0][0]+ ' '+clubs[1][0]+ ' '+clubs[2][0]+ ' '+ clubs[3][0]+ ' '+clubs[4][0]
        return add
    elif len(diamonds) >= 5:
        diamonds = sortvalue(diamonds)
        add = 'flush '+diamonds[0][0]+ ' '+diamonds[1][0]+ ' '+diamonds[2][0]+ ' '+ diamonds[3][0]+ ' '+diamonds[4][0]
        return add
    elif len(hearts) >= 5:
        hearts = sortvalue(hearts)
        add = 'flush '+hearts[0][0]+ ' '+hearts[1][0]+ ' '+hearts[2][0]+ ' '+ hearts[3][0]+ ' '+hearts[4][0]
        return add
    elif len(spades) >= 5:
        spades = sortvalue(spades)
        add = 'flush '+spades[0][0]+ ' '+spades[1][0]+ ' '+spades[2][0]+ ' '+ spades[3][0]+ ' '+spades[4][0]
        return add
    else:
        return ''

#######################################################

def fullhouse(x):
    cards = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
    numbers = []
    triple = False
    pair = False
    triplevalue = ''
    pairvalue = ''
    for b in range(len(x)):
        number = x[b][0]
        numbers.append(number)
    for c in range(len(cards)):
        if numbers.count(cards[c]) == 3:
            triple = True
            triplevalue = cards[c]
            cards.remove(triplevalue)
            break
    if triple:
        for d in range(len(cards)):
            if numbers.count(cards[d]) == 2 or numbers.count(cards[d]) == 3:
                pair = True
                pairvalue = cards[d]
                break
    if pair:
        return 'fullhouse '+triplevalue+' '+pairvalue
    else:
        return ''
    
#######################################################
    
def triple(x):
    cards = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
    numbers = []
    triple = False
    triplevalue = ''
    highcard = ''
    highcard2 = ''
    counter = 0 
    for b in range(len(x)):
        number = x[b][0]
        numbers.append(number)
    for c in range(len(cards)):
        if numbers.count(cards[c]) == 3:
            triple = True
            triplevalue = cards[c]
            break
    if triple:
        numbers = sortvalue(numbers)
        for d in range(len(numbers)):
            if numbers[d] != triplevalue:
                if counter == 0:
                    highcard = numbers[d]
                    counter += 1
                elif counter == 1:
                    highcard2 = numbers[d]
                    break
        return 'triple ' + triplevalue + ' ' + highcard + ' ' + highcard2
    else:
        return ''

######################################################

def twopair(x):
    cards = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
    numbers = []
    pair1 = False
    pair2 = False
    pair1value = ''
    pair2value = ''
    highcard = ''
    for b in range(len(x)):
        number = x[b][0]
        numbers.append(number)
    for c in range(len(cards)):
        if numbers.count(cards[c]) == 2:
            pair1 = True
            pair1value = cards[c]
            cards.remove(pair1value)
            break
    if pair1:
        for d in range(len(cards)):
            if numbers.count(cards[d]) == 2:
                pair2 = True
                pair2value = cards[d]
                break
    if pair2:
        numbers = sortvalue(numbers)
        for e in range(len(numbers)):
            if numbers[e] != pair1value and numbers[e] != pair2value:
                highcard = numbers[e]
                break
        return '2pair ' + pair1value + ' ' + pair2value + ' ' + highcard
    else:
        return ''
            
    
#######################################################
    
def pair(x):
    cards = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
    numbers = []
    pair = False
    pairvalue = ''
    highcard = ''
    highcard2 = ''
    highcard3 = ''
    counter = 0
    for b in range(len(x)):
        number = x[b][0]
        numbers.append(number)
    for c in range(len(cards)):
        if numbers.count(cards[c]) == 2:
            pair = True
            pairvalue = cards[c]
            break
    if pair:
        numbers = sortvalue(numbers)
        for d in range(len(numbers)):
            if numbers[d] != pairvalue:
                if counter == 0:
                    highcard = numbers[d]
                    counter += 1
                elif counter == 1:
                    highcard2 = numbers[d]
                    counter +=1
                elif counter == 2:
                    highcard3 = numbers[d]
                    break
        return 'pair ' + pairvalue + ' ' + highcard+ ' ' + highcard2+ ' ' + highcard3
    else:
        return ''

########################################################

def highcard(x):
    numbers = []
    for b in range(len(x)):
        number = x[b][0]
        numbers.append(number)
    numbers = sortvalue(numbers)
    return 'highcard ' + numbers[0] + ' ' + numbers[1]+ ' ' + numbers[2]+ ' ' + numbers[3]+ ' ' + numbers[4]
    

