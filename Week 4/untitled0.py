# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 11:16:43 2021

@author: epits
"""
    
        while not bool(hand):
            arr=''
            for i in hand:
                arr+=((hand[i]*i)+' ')
            print('Current Hand: '+arr)
            inp= input('Enter word, or a "." to indicate that you are finished: ')
            if inp=='.':
                break
            else:
                if not isValidWord(inp, hand, wordList):
                    print('Invalid word, please try again.\n')
                else:
                    for i in inp:
                        hand[i]-=1
                        if hand[i]==0:
                            del(hand[i])
                        score=getWordScore(word, len(hand))
                        currentScore+=score
                        print('"%s" earned %d points. Total: %d points',inp,score,currentScore)