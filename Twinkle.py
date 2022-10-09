from time import sleep
from playsound import playsound
from threading import Thread

import platform
import time
import os

if platform.system() == 'Linux':
    a = 'clear'
else:
    a = 'cls'

msl = 0.8


def moon():
    print("       _..._     ")
    print("     .:::::::.   ")
    print("    :::::::::::  NEW  MOON")
    print("    :::::::::::  ")
    print("    `:::::::::'  ")
    print("      `':::''    ")

    sleep(msl)
    os.system(a)

    print("\t       _..._     ")
    print("\t     .::::. `.   ")
    print("\t    :::::::.  :  WAXING CRESCENT MOON")
    print("\t    ::::::::  :  ")
    print("\t    `::::::' .'  ")
    print("\t      `'::'-'    ")
    sleep(msl)
    os.system(a)

    print("\t\t       _..._     ")
    print("\t\t     .::::  `.   ")
    print("\t\t    ::::::    :  FIRST QUARTER MOON")
    print("\t\t    ::::::    :  ")
    print("\t\t    `:::::   .'  ")
    print("\t\t      `'::.-'    ")

    sleep(msl)
    os.system(a)

    print("\t\t\t       _..._     ")
    print("\t\t\t     .::'   `.   ")
    print("\t\t\t    :::       :  WAXING GIBBOUS MOON")
    print("\t\t\t    :::       :  ")
    print("\t\t\t    `::.     .'  ")
    print("\t\t\t      `':..-'    ")

    sleep(msl)
    os.system(a)

    print("\t\t\t\t       _..._     ")
    print("\t\t\t\t     .'     `.   ")
    print("\t\t\t\t    :         :  FULL MOON")
    print("\t\t\t\t    :         :  ")
    print("\t\t\t\t    `.       .'  ")
    print("\t\t\t\t      `-...-'    ")

    sleep(msl)
    os.system(a)

    print("\t\t\t\t\t       _..._     ")
    print("\t\t\t\t\t     .'   `::.   ")
    print("\t\t\t\t\t    :       :::  WANING GIBBOUS MOON")
    print("\t\t\t\t\t    :       :::  ")
    print("\t\t\t\t\t    `.     .::'  ")
    print("\t\t\t\t\t      `-..:''    ")

    sleep(msl)
    os.system(a)

    print("\t\t\t\t\t\t       _..._     ")
    print("\t\t\t\t\t\t     .'  ::::.   ")
    print("\t\t\t\t\t\t    :    ::::::  LAST QUARTER MOON")
    print("\t\t\t\t\t\t    :    ::::::  ")
    print("\t\t\t\t\t\t    `.   :::::'  ")
    print("\t\t\t\t\t\t      `-.::''    ")

    sleep(msl)
    os.system(a)

    print("\t\t\t\t\t\t\t       _..._     ")
    print("\t\t\t\t\t\t\t     .' .::::.   ")
    print("\t\t\t\t\t\t\t    :  ::::::::  WANING CRESCENT MOON")
    print("\t\t\t\t\t\t\t    :  ::::::::  ")
    print("\t\t\t\t\t\t\t    `. '::::::'  ")
    print("\t\t\t\t\t\t\t      `-.::''    ")

    sleep(msl)
    os.system(a)

    print("\t\t\t\t\t\t\t\t       _..._     ")
    print("\t\t\t\t\t\t\t\t     .:::::::.   ")
    print("\t\t\t\t\t\t\t\t    :::::::::::  NEW  MOON")
    print("\t\t\t\t\t\t\t\t    :::::::::::  ")
    print("\t\t\t\t\t\t\t\t    `:::::::::'  ")
    print("\t\t\t\t\t\t\t\t      `':::''    ")
    sleep(msl)
    os.system(a)


def earth():
    print(" \n\n\tOUR EARTH\n                       ")
    print("\t         _____               ")
    print("\t     ,-:` \;',`'-,           ")
    print("\t   .'-;_,;  ':-;_,'.         ")
    print("\t  /;   '/    ,  _`.-\        ")
    print("\t | '`. (`     /` ` \`|       ")
    print("\t |:.  `\`-.   \_   / |       ")
    print("\t |     (   `,  .`\ ;'|       ")
    print("\t  \     | .'     `-'/        ")
    print("\t   `.   ;/        .'         ")
    print("\t      `'-._____.             ")

    sleep(0.5)
    os.system(a)

    print(" \n\n\tOUR EARTH\n                       ")
    print("\t              _____          ")
    print("\t           .-'.  ':'-.       ")
    print("\t         .''::: .:    '.     ")
    print("\t        /   :::::'      \    ")
    print("\t       ;.    ':' `       ;   ")
    print("\t       |       '..       |   ")
    print("\t       ; '      ::::.    ;   ")
    print("\t        \       '::::   /    ")
    print("\t         '.      :::  .'     ")
    print("\t           '-.___'_.-'       ")
    sleep(0.5)
    os.system(a)


def sat():
    print("\n\n\t  SATURN   \n                 ")
    print("\t           ,MMM8&&&.          ")
    print("\t      _...MMMMM88&&&&..._     ")
    print("\t   .::'''MMMMM88&&&&&&'''::.  ")
    print("\t  ::     MMMMM88&&&&&&     :: ")
    print("\t  '::....MMMMM88&&&&&&....::' ")
    print("\t     `''''MMMMM88&&&&''''`    ")
    print("\t           'MMM8&&&'          ")
    print("\t                              ")

    sleep(0.5)
    os.system(a)

    print("\n\n\t  SATURN\n                  ")
    print("\t                       .::. ")
    print("\t                    .:'  .: ")
    print("\t          ,MMM8&&&.:'   .:' ")
    print("\t         MMMMM88&&&&  .:'   ")
    print("\t        MMMMM88&&&&&&:'     ")
    print("\t        MMMMM88&&&&&&       ")
    print("\t      .:MMMMM88&&&&&&       ")
    print("\t    .:'  MMMMM88&&&&        ")
    print("\t  .:'   .:'MMM8&&&'         ")
    print("\t  :'  .:'                   ")
    print("\t  '::'                      ")

    sleep(0.5)
    os.system(a)


def lyrics():
    moon()
    # sleep(8)
    print("\n\n\tTwinkle, twinkle, little star,")
    sleep(4)
    print("\nHow I wonder what you are!")
    sleep(3)
    print("\n\tUp above the world so high,")
    sleep(4)
    print("\nLike a diamond in the sky.")
    sleep(4)
    print("\n\tTwinkle, twinkle, little star,")
    sleep(4)
    print("\nHow I wonder what you are!")
    sleep(3)
    #****
    os.system(a)
    sat()
    sat()

    sleep(3)
    print("\n\n\tWhen the blazing sun is gone,")
    sleep(4)
    print("\nWhen he nothing shines upon,")
    sleep(3)
    print("\n\tThen you show your little light,")
    sleep(4)
    print("\nTwinkle, twinkle, all the night.")
    sleep(4)
    print("\n\tTwinkle, twinkle, little star,")
    sleep(4)
    print("\nHow I wonder what you are!")
    sleep(3)

    #****
    os.system(a)
    earth()
    earth()

    sleep(2)
    print("\n\n\tThen the traveller in the dark,")
    sleep(4)
    print("\nThanks you for your tiny spark,")
    sleep(3)
    print("\n\tHe could not see which way to go,")
    sleep(4)
    print("\nIf you did not twinkle so.")
    sleep(4)
    print("\n\tTwinkle, twinkle, little star,")
    sleep(4)
    print("\nHow I wonder what you are!")
    sleep(3)

    #****
    os.system(a)
    sat()
    sat()

    sleep(2)
    print("\n\n\tIn the dark blue sky you keep,")
    sleep(4)
    print("\nAnd often through my curtains peep,")
    sleep(3)
    print("\n\tFor you never shut your eye,")
    sleep(4)
    print("\nTill the sun is in the sky.")
    sleep(4)
    print("\n\tTwinkle, twinkle, little star,")
    sleep(4)
    print("\nHow I wonder what you are!")
    sleep(3)

    #****
    os.system(a)
    earth()
    earth()

    sleep(2)
    print("\n\n\tAs your bright and tiny spark,")
    sleep(4)
    print("\nLights the traveller in the dark,—")
    sleep(3)
    print("\n\tThough I know not what you are,")
    sleep(4)
    print("\nTwinkle, twinkle, little star.")
    sleep(4)
    print("\n\tTwinkle, twinkle, little star,")
    sleep(4)
    print("\nHow I wonder what you are!")
    sleep(3)
    print("\n\tHow I wonder what you are!")
    sleep(3)
    os.system(a)
    print("\n\n\t\t*****************************")
    print("\t\t*                           *")
    print("\t\t*  ThankYou For Lisining :) *")
    print("\t\t*                           *")
    print("\t\t*****************************")


def snd():
    # t1 = Thread(target=playsound('twl1.mp3'))
    t1 = Thread(target=playsound('./msc/twl1.mp3'))


t1 = Thread(target=snd)
t1.start()
t2 = Thread(target=lyrics)
t2.start()
