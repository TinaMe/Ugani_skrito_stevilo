# -*- coding: utf-8 -*-

secret = 12

guess = int(raw_input("Ugani skrito število (med 1 in 20): "))

if guess == secret:
    print "Čestitamo! Uganil si skrito število!"

else:
    print "Žal si uganil napačno število. Poskusi še enkrat!"


