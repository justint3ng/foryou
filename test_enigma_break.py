# -*- coding: utf-8 -*-
"""
Create and test an Enigma machine encryption and decoding machine

This code is based on the implementation of the Enigma machine in Python 
called pyEnigma by Christophe Goessen (initial author) and Cédric Bonhomme
https://github.com/cedricbonhomme/pyEnigma

Created on Tue Feb  5 12:17:02 2019

@author: uqscha22
"""
import string
import enigma
import rotor

letters = string.ascii_letters #contains 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
capitalLetters = letters[-26:]
#print(capitalLetters)

ShakesHorribleMessage = "Xm xti ca idjmq Ecokta Rkhoxuu! Kdiu gm xex oft uz yjwenv qik parwc hs emrvm sfzu qnwfg. Gvgt vz vih rlt ly cnvpym xtq sgfvk jp jatrl irzru oubjo odp uso nsty jm gfp lkwrx pliv ojfo rl rylm isn aueuom! Gdwm Qopjmw!"
crib = "Hail Shakes!"
crib_substring = ""
print(crib_substring)

##Break the code via brute force search
#INSERT CODE HERE
#counter
num_tries = 0

#search all possible rotor starting positions
for rotor1 in capitalLetters:               #search for rotor1 starting position
    for rotor2 in capitalLetters:           #search for rotor2 starting position
        for rotor3 in capitalLetters:       #search for rotor3 starting position
            num_tries += 1                  #increment the counter by 1

            #generate possible starting positions
            start_pos = rotor1 + rotor2 + rotor3

            #initiate the engine
            decryption_engine = enigma.Enigma(rotor.ROTOR_Reflector_A, rotor.ROTOR_I,
                                rotor.ROTOR_II, rotor.ROTOR_III, key=start_pos,
                                plugs="AA BB CC DD EE")

            #attempt to decrypt the text
            decrypted_message = decryption_engine.encipher(ShakesHorribleMessage)

            #check if the decrypted version is the same as the crib text
            if decrypted_message.endswith(crib):
                print("rotor starting positions:")
                print(start_pos)
                break
        else:
            continue
        break
    else:
        continue
    break

#Print the Decoded message
#INSERT CODE HERE
print("final decrypted message:")
print(decrypted_message)
#print the number of tries it took
print(num_tries)

