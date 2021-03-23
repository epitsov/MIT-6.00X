# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 13:45:23 2021

@author: epits
"""
from ps6.py import Message
import string
class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self,text)
        
    def build_decrypter(self,shift):
        d = dict.fromkeys(string.ascii_letters, 0)
        for ch in d:
            if not ch.isupper(): 
                if ord(ch)-shift<97:
                    left=shift-(ord(ch)-97)
                    new=122-left
                    d[ch]=chr(new)    
                else:
                    d[ch]=chr(ord(ch)-shift)
            else:
                if ord(ch)-shift<65:
                    left= shift-(ord(ch)-65)
                    new=90-left
                    d[ch]=chr(new)    
                else:
                    d[ch]=chr(ord(ch)-shift)
        return d
    def apply_decrypter(self,shift):
        d=self.build_decrypter(shift)
        newWord=''
        for i in self.message_text:
            try:
                new_ch=d[i]
                newWord=newWord+new_ch
            except:
                newWord=newWord+i
        return newWord
            
    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        max_counter=0
        best_suggestion=0
        for i in range(26):
            counter=0
            ecryption=self.apply_decrypter(i)
            for w in ecryption:
                if w in self.valid_words:
                    counter=counter+1
            if counter>max_counter:
                best_suggestion=i
                final=ecryption.split(' ')
            
        return final
                    
