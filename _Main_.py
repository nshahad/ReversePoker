import pygame
import ctypes
import time
import random
from Handtest import * 


user32 = ctypes.windll.user32
screen_width = user32.GetSystemMetrics(0)
screen_height = user32.GetSystemMetrics(1)

pygame.init()
gameDisplay = pygame.display.set_mode((screen_width,screen_height),pygame.FULLSCREEN)
pygame.display.set_caption('ProjectP')
clock = pygame.time.Clock()


black = (0,0,0)
white = (255,255,255)

''' Fonts '''
pygame.font.init()
font1 = pygame.font.SysFont('Impact',40)
font2 = pygame.font.SysFont('Comic Sans MS',40)


start_button_sizex = int(0.25*screen_width)
start_button_sizey = int(0.2*screen_height)
start_button_locx = int(0.375*screen_width)
start_button_locy = int(0.4*screen_height)
start_button = pygame.image.load('start_button.png')
start_button = pygame.transform.scale(start_button, (start_button_sizex,start_button_sizey))
def fstart_button(start_button_locx,start_button_locy):
    gameDisplay.blit(start_button,(start_button_locx,start_button_locy))

htp_sizex = int(0.1*screen_width)
htp_sizey = int(0.1*screen_width)
htp_locx = int(0.8*screen_width)
htp_locy = int(0.8*screen_height)
htp = pygame.image.load('settings.png')
htp = pygame.transform.scale(htp, (htp_sizex,htp_sizey))
def fhtp(htp_locx,htp_locy):
    gameDisplay.blit(htp,(htp_locx,htp_locy))

title_sizex = int(0.7*screen_width)
title_sizey = int(0.25*screen_height)
title_locx = int(0.15*screen_width)
title_locy = int(0.1*screen_height)
title = pygame.image.load('Title.png')
title = pygame.transform.scale(title, (title_sizex,title_sizey))
def ftitle(title_locx,title_locy):
    gameDisplay.blit(title,(title_locx,title_locy))




nextcard_sizex = int(0.15 * screen_width)
nextcard_sizey = int(0.1 * screen_height)
nextcard_locx = int(0.85 * screen_width)
nextcard_locy = int(0.9 * screen_height)
nextcard = pygame.image.load('Next.png')
nextcard = pygame.transform.scale(nextcard, (nextcard_sizex, nextcard_sizey))
def fnextcard(nextcard_locx,nextcard_locy):
    gameDisplay.blit(nextcard,(nextcard_locx,nextcard_locy))


selectcard_sizex = int(0.15 * screen_width)
selectcard_sizey = int(0.1 * screen_height)
selectcard_locx = int(0)
selectcard_locy = int(0.9 * screen_height)
selectcard = pygame.image.load('Stay.png')
selectcard = pygame.transform.scale(selectcard, (selectcard_sizex, selectcard_sizey))
def fselectcard(selectcard_locx,selectcard_locy):
    gameDisplay.blit(selectcard, (selectcard_locx,selectcard_locy))

##################################################################################
''' Load Cards '''

card_sizex = int(0.15*screen_width)
card_sizey = int(0.2904* screen_height)
card1 = pygame.image.load('2_of_clubs.png')
card1 = pygame.transform.scale(card1, (card_sizex, card_sizey))
card2 = pygame.image.load('3_of_clubs.png')
card2 = pygame.transform.scale(card2, (card_sizex, card_sizey))
card3 = pygame.image.load('4_of_clubs.png')
card3 = pygame.transform.scale(card3, (card_sizex, card_sizey))
card4 = pygame.image.load('5_of_clubs.png')
card4 = pygame.transform.scale(card4, (card_sizex, card_sizey))
card5 = pygame.image.load('6_of_clubs.png')
card5 = pygame.transform.scale(card5, (card_sizex, card_sizey))
card6 = pygame.image.load('7_of_clubs.png')
card6 = pygame.transform.scale(card6, (card_sizex, card_sizey))
card7 = pygame.image.load('8_of_clubs.png')
card7 = pygame.transform.scale(card7, (card_sizex, card_sizey))
card8 = pygame.image.load('9_of_clubs.png')
card8 = pygame.transform.scale(card8, (card_sizex, card_sizey))
card9 = pygame.image.load('10_of_clubs.png')
card9 = pygame.transform.scale(card9, (card_sizex, card_sizey))
card10 = pygame.image.load('jack_of_clubs2.png')
card10 = pygame.transform.scale(card10, (card_sizex, card_sizey))
card11 = pygame.image.load('queen_of_clubs2.png')
card11 = pygame.transform.scale(card11, (card_sizex, card_sizey))
card12 = pygame.image.load('king_of_clubs2.png')
card12 = pygame.transform.scale(card12, (card_sizex, card_sizey))
card13 = pygame.image.load('ace_of_clubs.png')
card13 = pygame.transform.scale(card13, (card_sizex, card_sizey))
card14 = pygame.image.load('2_of_diamonds.png')
card14 = pygame.transform.scale(card14, (card_sizex, card_sizey))
card15 = pygame.image.load('3_of_diamonds.png')
card15 = pygame.transform.scale(card15, (card_sizex, card_sizey))
card16 = pygame.image.load('4_of_diamonds.png')
card16 = pygame.transform.scale(card16, (card_sizex, card_sizey))
card17 = pygame.image.load('5_of_diamonds.png')
card17 = pygame.transform.scale(card17, (card_sizex, card_sizey))
card18 = pygame.image.load('6_of_diamonds.png')
card18 = pygame.transform.scale(card18, (card_sizex, card_sizey))
card19 = pygame.image.load('7_of_diamonds.png')
card19 = pygame.transform.scale(card19, (card_sizex, card_sizey))
card20 = pygame.image.load('8_of_diamonds.png')
card20 = pygame.transform.scale(card20, (card_sizex, card_sizey))
card21 = pygame.image.load('9_of_diamonds.png')
card21 = pygame.transform.scale(card21, (card_sizex, card_sizey))
card22 = pygame.image.load('10_of_diamonds.png')
card22 = pygame.transform.scale(card22, (card_sizex, card_sizey))
card23 = pygame.image.load('jack_of_diamonds2.png')
card23 = pygame.transform.scale(card23, (card_sizex, card_sizey))
card24 = pygame.image.load('queen_of_diamonds2.png')
card24 = pygame.transform.scale(card24, (card_sizex, card_sizey))
card25 = pygame.image.load('king_of_diamonds2.png')
card25 = pygame.transform.scale(card25, (card_sizex, card_sizey))
card26 = pygame.image.load('ace_of_diamonds.png')
card26 = pygame.transform.scale(card26, (card_sizex, card_sizey))
card27 = pygame.image.load('2_of_hearts.png')
card27 = pygame.transform.scale(card27, (card_sizex, card_sizey))
card28 = pygame.image.load('3_of_hearts.png')
card28 = pygame.transform.scale(card28, (card_sizex, card_sizey))
card29 = pygame.image.load('4_of_hearts.png')
card29 = pygame.transform.scale(card29, (card_sizex, card_sizey))
card30 = pygame.image.load('5_of_hearts.png')
card30 = pygame.transform.scale(card30, (card_sizex, card_sizey))
card31 = pygame.image.load('6_of_hearts.png')
card31 = pygame.transform.scale(card31, (card_sizex, card_sizey))
card32 = pygame.image.load('7_of_hearts.png')
card32 = pygame.transform.scale(card32, (card_sizex, card_sizey))
card33 = pygame.image.load('8_of_hearts.png')
card33 = pygame.transform.scale(card33, (card_sizex, card_sizey))
card34 = pygame.image.load('9_of_hearts.png')
card34 = pygame.transform.scale(card34, (card_sizex, card_sizey))
card35 = pygame.image.load('10_of_hearts.png')
card35 = pygame.transform.scale(card35, (card_sizex, card_sizey))
card36 = pygame.image.load('jack_of_hearts2.png')
card36 = pygame.transform.scale(card36, (card_sizex, card_sizey))
card37 = pygame.image.load('queen_of_hearts2.png')
card37 = pygame.transform.scale(card37, (card_sizex, card_sizey))
card38 = pygame.image.load('king_of_hearts2.png')
card38 = pygame.transform.scale(card38, (card_sizex, card_sizey))
card39 = pygame.image.load('ace_of_hearts.png')
card39 = pygame.transform.scale(card39, (card_sizex, card_sizey))
card40 = pygame.image.load('2_of_spades.png')
card40 = pygame.transform.scale(card40, (card_sizex, card_sizey))
card41 = pygame.image.load('3_of_spades.png')
card41 = pygame.transform.scale(card41, (card_sizex, card_sizey))
card42 = pygame.image.load('4_of_spades.png')
card42 = pygame.transform.scale(card42, (card_sizex, card_sizey))
card43 = pygame.image.load('5_of_spades.png')
card43 = pygame.transform.scale(card43, (card_sizex, card_sizey))
card44 = pygame.image.load('6_of_spades.png')
card44 = pygame.transform.scale(card44, (card_sizex, card_sizey))
card45 = pygame.image.load('7_of_spades.png')
card45 = pygame.transform.scale(card45, (card_sizex, card_sizey))
card46 = pygame.image.load('8_of_spades.png')
card46 = pygame.transform.scale(card46, (card_sizex, card_sizey))
card47 = pygame.image.load('9_of_spades.png')
card47 = pygame.transform.scale(card47, (card_sizex, card_sizey))
card48 = pygame.image.load('10_of_spades.png')
card48 = pygame.transform.scale(card48, (card_sizex, card_sizey))
card49 = pygame.image.load('jack_of_spades2.png')
card49 = pygame.transform.scale(card49, (card_sizex, card_sizey))
card50 = pygame.image.load('queen_of_spades2.png')
card50 = pygame.transform.scale(card50, (card_sizex, card_sizey))
card51 = pygame.image.load('king_of_spades2.png')
card51 = pygame.transform.scale(card51, (card_sizex, card_sizey))
card52 = pygame.image.load('ace_of_spades2.png')
card52 = pygame.transform.scale(card52, (card_sizex, card_sizey))
           

def fprintcard(parameter1,parameter2,parameter3):
    if parameter1 == '2C':
        gameDisplay.blit(card1,(parameter2,parameter3))
    elif parameter1 == '3C':
        gameDisplay.blit(card2,(parameter2,parameter3))
    elif parameter1 == '4C':
        gameDisplay.blit(card3,(parameter2,parameter3))
    elif parameter1 == '5C':
        gameDisplay.blit(card4,(parameter2,parameter3))
    elif parameter1 == '6C':
        gameDisplay.blit(card5,(parameter2,parameter3))
    elif parameter1 == '7C':
        gameDisplay.blit(card6,(parameter2,parameter3))
    elif parameter1 == '8C':
        gameDisplay.blit(card7,(parameter2,parameter3))
    elif parameter1 == '9C':
        gameDisplay.blit(card8,(parameter2,parameter3))
    elif parameter1 == 'TC':
        gameDisplay.blit(card9,(parameter2,parameter3))
    elif parameter1 == 'JC':
        gameDisplay.blit(card10,(parameter2,parameter3))
    elif parameter1 == 'QC':
        gameDisplay.blit(card11,(parameter2,parameter3))
    elif parameter1 == 'KC':
        gameDisplay.blit(card12,(parameter2,parameter3))
    elif parameter1 == 'AC':
        gameDisplay.blit(card13,(parameter2,parameter3))
    elif parameter1 == '2D':
        gameDisplay.blit(card14,(parameter2,parameter3))
    elif parameter1 == '3D':
        gameDisplay.blit(card15,(parameter2,parameter3))
    elif parameter1 == '4D':
        gameDisplay.blit(card16,(parameter2,parameter3))
    elif parameter1 == '5D':
        gameDisplay.blit(card17,(parameter2,parameter3))
    elif parameter1 == '6D':
        gameDisplay.blit(card18,(parameter2,parameter3))
    elif parameter1 == '7D':
        gameDisplay.blit(card19,(parameter2,parameter3))
    elif parameter1 == '8D':
        gameDisplay.blit(card20,(parameter2,parameter3))
    elif parameter1 == '9D':
        gameDisplay.blit(card21,(parameter2,parameter3))
    elif parameter1 == 'TD':
        gameDisplay.blit(card22,(parameter2,parameter3))
    elif parameter1 == 'JD':
        gameDisplay.blit(card23,(parameter2,parameter3))
    elif parameter1 == 'QD':
        gameDisplay.blit(card24,(parameter2,parameter3))
    elif parameter1 == 'KD':
        gameDisplay.blit(card25,(parameter2,parameter3))
    elif parameter1 == 'AD':
        gameDisplay.blit(card26,(parameter2,parameter3))
    elif parameter1 == '2H':
        gameDisplay.blit(card27,(parameter2,parameter3))
    elif parameter1 == '3H':
        gameDisplay.blit(card28,(parameter2,parameter3))
    elif parameter1 == '4H':
        gameDisplay.blit(card29,(parameter2,parameter3))
    elif parameter1 == '5H':
        gameDisplay.blit(card30,(parameter2,parameter3))
    elif parameter1 == '6H':
        gameDisplay.blit(card31,(parameter2,parameter3))
    elif parameter1 == '7H':
        gameDisplay.blit(card32,(parameter2,parameter3))
    elif parameter1 == '8H':
        gameDisplay.blit(card33,(parameter2,parameter3))
    elif parameter1 == '9H':
        gameDisplay.blit(card34,(parameter2,parameter3))
    elif parameter1 == 'TH':
        gameDisplay.blit(card35,(parameter2,parameter3))
    elif parameter1 == 'JH':
        gameDisplay.blit(card36,(parameter2,parameter3))
    elif parameter1 == 'QH':
        gameDisplay.blit(card37,(parameter2,parameter3))
    elif parameter1 == 'KH':
        gameDisplay.blit(card38,(parameter2,parameter3))
    elif parameter1 == 'AH':
        gameDisplay.blit(card39,(parameter2,parameter3))
    elif parameter1 == '2S':
        gameDisplay.blit(card40,(parameter2,parameter3))
    elif parameter1 == '3S':
        gameDisplay.blit(card41,(parameter2,parameter3))
    elif parameter1 == '4S':
        gameDisplay.blit(card42,(parameter2,parameter3))
    elif parameter1 == '5S':
        gameDisplay.blit(card43,(parameter2,parameter3))
    elif parameter1 == '6S':
        gameDisplay.blit(card44,(parameter2,parameter3))
    elif parameter1 == '7S':
        gameDisplay.blit(card45,(parameter2,parameter3))
    elif parameter1 == '8S':
        gameDisplay.blit(card46,(parameter2,parameter3))
    elif parameter1 == '9S':
        gameDisplay.blit(card47,(parameter2,parameter3))
    elif parameter1 == 'TS':
        gameDisplay.blit(card48,(parameter2,parameter3))
    elif parameter1 == 'JS':
        gameDisplay.blit(card49,(parameter2,parameter3))
    elif parameter1 == 'QS':
        gameDisplay.blit(card50,(parameter2,parameter3))
    elif parameter1 == 'KS':
        gameDisplay.blit(card51,(parameter2,parameter3))
    elif parameter1 == 'AS':
        gameDisplay.blit(card52,(parameter2,parameter3))





####################################################################################

apprun = True
homepage = True #1 - home
screen1 = False #2 - play
screen2 = False #3  - htp
screen3 = False #4 - hand order
screen_selector = 1
streak = 0
while apprun:
    ''' Saving High Score '''
    file = open("ProjectP.txt","r")
    highscore_text = file.readline()
    file.close()
    if int(streak) > int(highscore_text):
        file = open("ProjectP.txt","w")
        file.write(str(streak))
        file.close()
    ##################################################################  
    
    if screen_selector == 1:
        while homepage:
            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        homepage = False
                        apprun = False
                        break

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if pos[0] > start_button_locx and pos[0] < start_button_locx + start_button_sizex:
                        if pos[1] > start_button_locy and pos[1] < start_button_locy + start_button_sizey:
                            homepage = False
                            screen1 = True
                            screen_selector = 2

                    if pos[0] > htp_locx and pos[0] < htp_locx + htp_sizex:
                        if pos[1] > htp_locy and pos[1] < htp_locy + htp_sizey:
                            homepage = False
                            screen2 = True
                            screen_selector = 3

            gameDisplay.fill(white)
            gameDisplay.fill((14,25,114))
            ftitle(title_locx,title_locy)
            fstart_button(start_button_locx,start_button_locy)
            fhtp(htp_locx,htp_locy) ########
            pygame.display.update()
            clock.tick(60)
            
    elif screen_selector == 2:
        ''' Drawing Hands'''
        scores = []

        allcards = []
        while len(allcards) < 15:
            x = random.randint(1,52)
            cardcheck = getcard(x)
            if cardcheck not in allcards:
                allcards.append(cardcheck)
        commonhand = allcards[0:5]
        playerhand1 = allcards[5:7]
        playerhand2 = allcards[7:9]
        playerhand3 = allcards[9:11]
        playerhand4 = allcards[11:13]
        playerhand5 = allcards[13:15]
        print (commonhand)
        print (playerhand1)
        print (playerhand2)
        print (playerhand3)
        print (playerhand4)
        print (playerhand5)


                
        ########################################################
        ''' Scoring Hands ''' 
        for a in range(5):
            currenthand = []
            if a == 0:
                for c in range(5):
                    currenthand.append(commonhand[c])
                currenthand.append(playerhand1[0])
                currenthand.append(playerhand1[1])
                add = quad(currenthand)
                if add == '':
                    add = fullhouse(currenthand)
                    if add == '':
                        add = flush(currenthand)
                        if add == '':
                            add = straight(currenthand)
                            if add == '':
                                add = triple(currenthand)
                                if add == '':
                                    add = twopair(currenthand)
                                    if add == '':
                                        add = pair(currenthand)
                                        if add == '':
                                            add = highcard(currenthand)
                add = add + ' 1'
                scores.append(add)
                
            elif a == 1:
                for c in range(5):
                    currenthand.append(commonhand[c])
                currenthand.append(playerhand2[0])
                currenthand.append(playerhand2[1])
                add = quad(currenthand)
                if add == '':
                    add = fullhouse(currenthand)
                    if add == '':
                        add = flush(currenthand)
                        if add == '':
                            add = straight(currenthand)
                            if add == '':
                                add = triple(currenthand)
                                if add == '':
                                    add = twopair(currenthand)
                                    if add == '':
                                        add = pair(currenthand)
                                        if add == '':
                                            add = highcard(currenthand)
                add = add + ' 2'
                scores.append(add)
            elif a == 2:
                for c in range(5):
                    currenthand.append(commonhand[c])
                currenthand.append(playerhand3[0])
                currenthand.append(playerhand3[1])
                add = quad(currenthand)
                if add == '':
                    add = fullhouse(currenthand)
                    if add == '':
                        add = flush(currenthand)
                        if add == '':
                            add = straight(currenthand)
                            if add == '':
                                add = triple(currenthand)
                                if add == '':
                                    add = twopair(currenthand)
                                    if add == '':
                                        add = pair(currenthand)
                                        if add == '':
                                            add = highcard(currenthand)
                add = add + ' 3'
                scores.append(add)
            elif a == 3:
                for c in range(5):
                    currenthand.append(commonhand[c])
                currenthand.append(playerhand4[0])
                currenthand.append(playerhand4[1])
                add = quad(currenthand)
                if add == '':
                    add = fullhouse(currenthand)
                    if add == '':
                        add = flush(currenthand)
                        if add == '':
                            add = straight(currenthand)
                            if add == '':
                                add = triple(currenthand)
                                if add == '':
                                    add = twopair(currenthand)
                                    if add == '':
                                        add = pair(currenthand)
                                        if add == '':
                                            add = highcard(currenthand)
                add = add + ' 4'
                scores.append(add)
            elif a == 4:
                for c in range(5):
                    currenthand.append(commonhand[c])
                currenthand.append(playerhand5[0])
                currenthand.append(playerhand5[1])
                add = quad(currenthand)
                if add == '':
                    add = fullhouse(currenthand)
                    if add == '':
                        add = flush(currenthand)
                        if add == '':
                            add = straight(currenthand)
                            if add == '':
                                add = triple(currenthand)
                                if add == '':
                                    add = twopair(currenthand)
                                    if add == '':
                                        add = pair(currenthand)
                                        if add == '':
                                            add = highcard(currenthand)
                add = add + ' 5'
                scores.append(add)
                
        print (scores)

        #####################################################################
        ''' Finding Winning Hands '''
        winninghands = []
        scores2 = []
        for x in range(len(scores)):
            current = scores[x].split()
            scores2.append(current)


        handcheck1 = []
        handranks = ['quad','fullhouse','flush','straight','triple','2pair','pair','highcard']
        for x in range(len(handranks)):
            for y in range(len(scores2)):
                if scores2[y][0] == handranks[x]:
                    handcheck1.append(scores2[y])
            if len(handcheck1) > 0:
                break



        cards = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
        ''' Each handcheck is the next element in the hand that is being compared Ex: triple value then highcard1 then highcard2 '''
        handcheck2 = [] 
        handcheck3 = []
        handcheck4 = []
        handcheck5 = []
        handcheck6 = []
        if handcheck1[0][0] == 'quad':
            if len(handcheck1) == 1:
                winninghands.append(handcheck1[0][-1])
            else:
                for x in range(len(cards)):
                    for y in range(len(handcheck1)):
                        if handcheck1[y][1] == cards[x]:
                            handcheck2.append(handcheck1[y])
                    if len(handcheck2) > 0:
                        break
                if len(handcheck2) == 1:
                    winninghands.append(handcheck2[0][-1])
                else:
                    for x in range(len(cards)):
                        for y in range(len(handcheck2)):
                            if handcheck2[y][2] == cards[x]:
                                handcheck3.append(handcheck2[y])
                        if len(handcheck3) > 0:
                            break
                    for z in range(len(handcheck3)):
                        winninghands.append(handcheck3[z][-1])            
                    

        elif handcheck1[0][0] == 'fullhouse':
            if len(handcheck1) == 1:
                winninghands.append(handcheck1[0][-1])
            else:
                for x in range(len(cards)):
                    for y in range(len(handcheck1)):
                        if handcheck1[y][1] == cards[x]:
                            handcheck2.append(handcheck1[y])
                    if len(handcheck2) > 0:
                        break
                if len(handcheck2) == 1:
                    winninghands.append(handcheck2[0][-1])
                else:
                    for x in range(len(cards)):
                        for y in range(len(handcheck2)):
                            if handcheck2[y][2] == cards[x]:
                                handcheck3.append(handcheck2[y])
                        if len(handcheck3) > 0:
                            break
                    for z in range(len(handcheck3)):
                        winninghands.append(handcheck3[z][-1])              
                            

        elif handcheck1[0][0] == 'flush':
            if len(handcheck1) == 1:
                winninghands.append(handcheck1[0][-1])
            else:
                for x in range(len(cards)):
                    for y in range(len(handcheck1)):
                        if handcheck1[y][1] == cards[x]:
                            handcheck2.append(handcheck1[y])
                    if len(handcheck2) > 0:
                        break
                if len(handcheck2) == 1:
                    winninghands.append(handcheck2[0][-1])
                else:
                    for x in range(len(cards)):
                        for y in range(len(handcheck2)):
                            if handcheck2[y][2] == cards[x]:
                                handcheck3.append(handcheck2[y])
                        if len(handcheck3) > 0:
                            break
                    if len(handcheck3) == 1:
                        winninghands.append(handcheck3[0][-1])
                    else:
                        for x in range(len(cards)):
                            for y in range(len(handcheck3)):
                                if handcheck3[y][3] == cards[x]:
                                    handcheck4.append(handcheck3[y])
                            if len(handcheck4) > 0:
                                break
                        if len(handcheck4) == 1:
                            winninghands.append(handcheck4[0][-1])
                        else:
                            for x in range(len(cards)):
                                for y in range(len(handcheck4)):
                                    if handcheck4[y][4] == cards[x]:
                                        handcheck5.append(handcheck4[y])
                                if len(handcheck5) > 0:
                                    break
                            if len(handcheck5) == 1:
                                winninghands.append(handcheck5[0][-1])
                            else:
                                for x in range(len(cards)):
                                    for y in range(len(handcheck5)):
                                        if handcheck5[y][5] == cards[x]:
                                            handcheck6.append(handcheck5[y])
                                    if len(handcheck6) > 0:
                                        break                  
                                for z in range(len(handcheck6)):
                                    winninghands.append(handcheck6[z][-1])
                                    

        elif handcheck1[0][0] == 'straight':
            if len(handcheck1) == 1:
                winninghands.append(handcheck1[0][-1])
            else:
                for x in range(len(cards)):
                    for y in range(len(handcheck1)):
                        if handcheck1[y][1] == cards[x]:
                            handcheck2.append(handcheck1[y])
                    if len(handcheck2) > 0:
                        break
                for z in range(len(handcheck2)):
                    winninghands.append(handcheck2[z][-1])
                    

        elif handcheck1[0][0] == 'triple':
            if len(handcheck1) == 1:
                winninghands.append(handcheck1[0][-1])
            else:
                for x in range(len(cards)):
                    for y in range(len(handcheck1)):
                        if handcheck1[y][1] == cards[x]:
                            handcheck2.append(handcheck1[y])
                    if len(handcheck2) > 0:
                        break
                if len(handcheck2) == 1:
                    winninghands.append(handcheck2[0][-1])
                else:
                    for x in range(len(cards)):
                        for y in range(len(handcheck2)):
                            if handcheck2[y][2] == cards[x]:
                                handcheck3.append(handcheck2[y])
                        if len(handcheck3) > 0:
                            break
                    if len(handcheck3) == 1:
                        winninghands.append(handcheck3[0][-1])
                    else:
                        for x in range(len(cards)):
                            for y in range(len(handcheck3)):
                                if handcheck3[y][3] == cards[x]:
                                    handcheck4.append(handcheck3[y])
                            if len(handcheck4) > 0:
                                break                       
                        for z in range(len(handcheck4)):
                            winninghands.append(handcheck4[z][-1]) 
                

        elif handcheck1[0][0] == '2pair':
            if len(handcheck1) == 1:
                winninghands.append(handcheck1[0][-1])
            else:
                for x in range(len(cards)):
                    for y in range(len(handcheck1)):
                        if handcheck1[y][1] == cards[x]:
                            handcheck2.append(handcheck1[y])
                    if len(handcheck2) > 0:
                        break
                if len(handcheck2) == 1:
                    winninghands.append(handcheck2[0][-1])
                else:
                    for x in range(len(cards)):
                        for y in range(len(handcheck2)):
                            if handcheck2[y][2] == cards[x]:
                                handcheck3.append(handcheck2[y])
                        if len(handcheck3) > 0:
                            break
                    if len(handcheck3) == 1:
                        winninghands.append(handcheck3[0][-1])
                    else:
                        for x in range(len(cards)):
                            for y in range(len(handcheck3)):
                                if handcheck3[y][3] == cards[x]:
                                    handcheck4.append(handcheck3[y])
                            if len(handcheck4) > 0:
                                break                       
                        for z in range(len(handcheck4)):
                            winninghands.append(handcheck4[z][-1])
                            

        elif handcheck1[0][0] == 'pair':
            if len(handcheck1) == 1:
                winninghands.append(handcheck1[0][-1])
            else:
                for x in range(len(cards)):
                    for y in range(len(handcheck1)):
                        if handcheck1[y][1] == cards[x]:
                            handcheck2.append(handcheck1[y])
                    if len(handcheck2) > 0:
                        break
                if len(handcheck2) == 1:
                    winninghands.append(handcheck2[0][-1])
                else:
                    for x in range(len(cards)):
                        for y in range(len(handcheck2)):
                            if handcheck2[y][2] == cards[x]:
                                handcheck3.append(handcheck2[y])
                        if len(handcheck3) > 0:
                            break
                    if len(handcheck3) == 1:
                        winninghands.append(handcheck3[0][-1])
                    else:
                        for x in range(len(cards)):
                            for y in range(len(handcheck3)):
                                if handcheck3[y][3] == cards[x]:
                                    handcheck4.append(handcheck3[y])
                            if len(handcheck4) > 0:
                                break
                        if len(handcheck4) == 1:
                            winninghands.append(handcheck4[0][-1])
                        else:
                            for x in range(len(cards)):
                                for y in range(len(handcheck4)):
                                    if handcheck4[y][4] == cards[x]:
                                        handcheck5.append(handcheck4[y])
                                if len(handcheck5) > 0:
                                    break                  
                            for z in range(len(handcheck5)):
                                winninghands.append(handcheck5[z][-1])

                            
        elif handcheck1[0][0] == 'highcard':
            if len(handcheck1) == 1:
                winninghands.append(handcheck1[0][-1])
            else:
                for x in range(len(cards)):
                    for y in range(len(handcheck1)):
                        if handcheck1[y][1] == cards[x]:
                            handcheck2.append(handcheck1[y])
                    if len(handcheck2) > 0:
                        break
                if len(handcheck2) == 1:
                    winninghands.append(handcheck2[0][-1])
                else:
                    for x in range(len(cards)):
                        for y in range(len(handcheck2)):
                            if handcheck2[y][2] == cards[x]:
                                handcheck3.append(handcheck2[y])
                        if len(handcheck3) > 0:
                            break
                    if len(handcheck3) == 1:
                        winninghands.append(handcheck3[0][-1])
                    else:
                        for x in range(len(cards)):
                            for y in range(len(handcheck3)):
                                if handcheck3[y][3] == cards[x]:
                                    handcheck4.append(handcheck3[y])
                            if len(handcheck4) > 0:
                                break
                        if len(handcheck4) == 1:
                            winninghands.append(handcheck4[0][-1])
                        else:
                            for x in range(len(cards)):
                                for y in range(len(handcheck4)):
                                    if handcheck4[y][4] == cards[x]:
                                        handcheck5.append(handcheck4[y])
                                if len(handcheck5) > 0:
                                    break
                            if len(handcheck5) == 1:
                                winninghands.append(handcheck5[0][-1])
                            else:
                                for x in range(len(cards)):
                                    for y in range(len(handcheck5)):
                                        if handcheck5[y][5] == cards[x]:
                                            handcheck6.append(handcheck5[y])
                                    if len(handcheck6) > 0:
                                        break                  
                                for z in range(len(handcheck6)):
                                    winninghands.append(handcheck6[z][-1])
                
        print (winninghands)
        #############################################################
        current_round = 1 #0.191666
        round1 = True
        round2 = False
        round3 = False
        round4 = False
        round5 = False
        card1_locx = 0.041666*screen_width
        card1_locy = 0.1*screen_height
        card2_locx = 0.233332*screen_width
        card2_locy = 0.1*screen_height
        card3_locx = 0.424998*screen_width
        card3_locy = 0.1*screen_height
        card4_locx = 0.616664*screen_width
        card4_locy = 0.1*screen_height
        card5_locx = 0.80833*screen_width
        card5_locy = 0.1*screen_height
        card6_locx = 0.041666*screen_width
        card6_locy = 0.5*screen_height
        card7_locx = 0.071666*screen_width
        card7_locy = 0.5*screen_height
        card8_locx = 0.233332*screen_width
        card8_locy = 0.5*screen_height
        card9_locx = 0.263332*screen_width
        card9_locy = 0.5*screen_height
        card10_locx = 0.424998*screen_width
        card10_locy = 0.5*screen_height
        card11_locx = 0.454998*screen_width
        card11_locy = 0.5*screen_height
        card12_locx = 0.616664*screen_width
        card12_locy = 0.5*screen_height
        card13_locx = 0.646664*screen_width
        card13_locy = 0.5*screen_height
        card14_locx = 0.80833*screen_width
        card14_locy = 0.5*screen_height
        card15_locx = 0.83833*screen_width
        card15_locy = 0.5*screen_height
        userchoice = '0'
        selected = False
        selected2 = True
        
                    
        
        while screen1:
            gameDisplay.fill(white)
            gameDisplay.fill((14,25,114))
            
            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()

                    ''' Next Card Button (Prints next card) '''
                    if pos[0] > nextcard_locx and pos[0] < nextcard_locx + nextcard_sizex:
                        if pos[1] > nextcard_locy and pos[1] < nextcard_locy + nextcard_sizey:
                            current_round += 1
                            if current_round == 2:
                                round2 = True
                            elif current_round == 3:
                                round3 = True
                            elif current_round == 4:
                                round4 = True
                            elif current_round == 5:
                                round5 = True
                            if selected:
                                current_round = 6

                    ''' Selected Card Button (prints all cards and selects current card) '''    
                    if pos[0] > selectcard_locx and pos[0] < selectcard_locx + selectcard_sizex:
                        if pos[1] > selectcard_locy and pos[1] < selectcard_locy + selectcard_sizey:
                            userchoice = str(current_round)
                            selected = True

            ####################################################################################################
            ''' Printing ''' 
            fnextcard(nextcard_locx,nextcard_locy)
            fselectcard(selectcard_locx,selectcard_locy)
                        
            if  round1 or selected :
                fprintcard(allcards[0],card1_locx,card1_locy)
                fprintcard(allcards[1],card2_locx,card2_locy)
                fprintcard(allcards[2],card3_locx,card3_locy)
                fprintcard(allcards[3],card4_locx,card4_locy)
                fprintcard(allcards[4],card5_locx,card5_locy)
                fprintcard(allcards[5],card6_locx,card6_locy)
                fprintcard(allcards[6],card7_locx,card7_locy)
            if  round2 or selected :
                fprintcard(allcards[7],card8_locx,card8_locy)
                fprintcard(allcards[8],card9_locx,card9_locy)
            if  round3 or selected:
                fprintcard(allcards[9],card10_locx,card10_locy)
                fprintcard(allcards[10],card11_locx,card11_locy)
            if  round4 or selected:
                fprintcard(allcards[11],card12_locx,card12_locy)
                fprintcard(allcards[12],card13_locx,card13_locy)
            if  round5 or selected:
                fprintcard(allcards[13],card14_locx,card14_locy)
                fprintcard(allcards[14],card15_locx,card15_locy)
            if current_round == 6:
                screen1 = False
                homepage = True
                screen_selector = 1

            ## Save Score on Text File ## 
            file = open("ProjectP.txt","r")
            highscore_text = file.readline()
            file.close()
            
            textsurface = font1.render('Streak: '+str(streak), False, white)
            textsurface2 = font1.render('Highscore: '+str(highscore_text), False, white)
            gameDisplay.blit(textsurface, (int(0.3*screen_width),int(0.9*screen_height)))
            gameDisplay.blit(textsurface2, (int(0.6*screen_width),int(0.9*screen_height)))


            winlose = ''
            if selected and selected2:
                for x in range(len(winninghands)):
                    if userchoice == winninghands[x]:
                        winlose = 'You Win'
                        selected2 = False
                        streak += 1
                    
                if winlose == '':
                    winlose = 'You Lose'
                    selected2 = False
                    streak = 0
                print (winlose)                            
            
            pygame.display.update()
            clock.tick(60)
            
    elif screen_selector == 3:
        while screen2:
            for event in pygame.event.get():
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if pos[0] > start_button_locx and pos[0] < start_button_locx + start_button_sizex:
                        if pos[1] > start_button_locy and pos[1] < start_button_locy + start_button_sizey:
                            homepage = True
                            screen2 = False
                            screen_selector = 1

            #gameDisplay.fill((40,190,160))
            gameDisplay.fill(white)
            gameDisplay.fill((14,25,114))
            fstart_button(start_button_locx,start_button_locy)
            pygame.display.update()
            clock.tick(60)

    elif screen_selector == 4:
        while screen3:
            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if pos[0] > close_button_locx and pos[0] < close_button_locx + close_button_sizex:
                        if pos[1] > close_button_locy and pos[1] < close_button_locy + close_button_sizey:
                            screen2 = True
                            screen3 = False
                            screen_selector = 3

            fprintcard('AS',100,100)
            fprintcard('KS',200,100)
            fprintcard('QS',300,100)
            fprintcard('JS',400,100)
            fprintcard('TS',500,100)

            fprintcard('9S',100,200)
            fprintcard('9H',200,200)
            fprintcard('9D',300,200)
            fprintcard('9C',400,200)
            fprintcard('AS',500,200)

            

            gameDisplay.fill(white)
            


''' Color button when hovering over '''
