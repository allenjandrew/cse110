print('\nWelcome to the Oregon Trail. Let\'s get started!')

import sys
def you_died():
    sys.exit('\nYou died! Better luck next time.\n')

input('\nYou\'ve got a long journey ahead. Press ENTER to begin.')

print('\nYou\'re packing for the journey. You\'ve loaded up the wagon with')
print('food, supplies, tools, clothes, and a bit of cash. Hopefully it\'ll')
print('enough for you, your wife, and your 6 children. You take a look and')
print('realize that the wagon\'s full - you can only take one more item.')
item = input('Do you want to pack a RIFLE, a pet LAMB, or a family HEIRLOOM?\n').lower()
print('')

if item == 'rifle':
    print('You can\'t go anywhere without your trusty rifle. She may be a bit')
    print('rusty, but she\'ll get the job done.')
elif item == 'lamb':
    print('Daisy bleats happily as you pick her up and place her gently in the')
    print('wagon. She\'ll keep your daughters company, and on the off chance you')
    print('should run out of rations, Heaven forbid, Daisy will provide.')
elif item == 'heirloom':
    print('This old chair was crafted by your great-grandfather. Your fond memories')
    print('of him come flooding back as you place the chair in the back of the wagon.')
else:
    print('You place it in the wagon. It may prove useful someday.')

input('\nReady to go? Let\'s hit the trail. Press ENTER to continue.')

print('\nYou make it to Winter Quarters, but find out that you\'re a day late. The')
print('wagon company left just two days ago. The next company doesn\'t start out')
print('until late summer. You can choose to LEAVE now and try to catch up to the')
print('wagon company, or you can WAIT and leave with the next company, but risk')
decision = input('traveling through cold weather. What will you do?\n').lower()
print('')

if decision == 'wait':
    print('You decide to wait for the next wagon. You end up waiting longer than expected.')
    print('The wagon company leaves in late September. You and your wife decide it\'s all or')
    print('nothing at this point, and you go with them. After two months of slow progress and')
    print('the deaths of two daughters from dysentery, a heavy snowstorm hits the company. You')
    print('don\'t make it through alive. You only hope your wife can survive the horrible winter.')
    you_died()

print('\nYou decide to leave the settlement now, hoping to catch up to the company')
print('before it gets too far away. You make good time on the trail, but after two weeks')
print('you still haven\'t caught up to it. You may have made a wrong turn. One night,')
print('you suddenly hear whoops in the distance. Indians are coming to raid your wagon!')
if item == 'rifle':
    indians_response = input('Would you like to FIGHT back or COMPLY with their demands?\n').lower()
    print('')
    if indians_response == 'fight':
        print('You shoot at the Indians and one of them falls. Adrenaline rising, you')
        print('stand up to get a better shot. You feel a jolt of pain in your chest and')
        print('realize you\'ve been hit. The last thing you hear is your wife\'s scream.')
        you_died()
else:
    indians_response = input('Would you like to HIDE or COMPLY with their demands?\n').lower()
    print('')
    if indians_response == 'hide':
        print('You hide the wagon in a clump of trees and tell everyone to be quiet.')
        if item == 'lamb':
            print('Suddenly, Daisy bursts out with terrified bleating. You quickly try to silence')
            print('her, but it\'s too late! The Indians have found you! They\'re on a killing spree,')
            print('and you\'ve become their next victims. They kill you and take your belongings.')
            you_died()
        else:
            print('You pray for a miracle and wait breathlessly. The Indians run right by your hiding')
            print('spot without seeing you. After a few minutes, you breathe a sigh of relief.')
if indians_response == 'comply':
    print('It\'s probably for the best to just let the Indians take what they want and')
    print('leave. They take the cash, the clothes, and a bit of food, then continue off')
    print('into the night. Hopefully you won\'t come accross them again.')

print('\nA couple months later, you reach the mountains. You\'re getting close! However,')
print('your food supply is getting low. You can probably last a little while longer if')
print('you ration what\'s left, but could it take you all the way to Utah? Alternatively,')
if item == 'rifle':
    print('you could take your rifle and see if you can hunt some game. The mountains are')
    print('full of deer and squirrels, but you also face the risk of coming across a bear.')
    option_2 = ', HUNT for game,'
elif item == 'lamb':
    print('you have Daisy... she would make a nice meal. You\'ve been getting fed up with')
    print('her incessant bleating and whimpering, and a bit of mutton would hit the spot.')
    option_2 = ', EAT Daisy,'
elif item == 'heirloom' and indians_response == 'hide':
    print('you crossed paths with a trader a while back who said there is a settlement')
    print('nearby. You could try to find it, and use your cash to buy more food.')
    option_2 = ', look for the SETTLEMENT,'
else:
    print('you could try to forage for food, though the prospects of finding any are slim.')
    option_2 = ''
hunger = input(f'Would you like to RATION your food{option_2} or try to FORAGE?\n').lower()

if hunger == 'ration':
    print('\nYou decide to ration your remaining food. Miraculously, there\'s just enough')
    print('to get you through the next couple months of traveling. Every so often you find')
    print('a dead animal or a lone berry bush as well. You thank the Lord for His blessings.')
elif hunger == 'forage':
    print('\nUnfortunately, food is hard to come by around here. Your foraging efforts were')
    print('in vain. You return to the wagon even more hungry and exhausted than before.')
    print('A few days later, you begin to feel your vision narrowing. You try to hop down')
    print('from the wagon, but you fall underneath the wheel, and your leg breaks. You only')
    print('last one more night.')
    you_died()
elif hunger == 'hunt':
    print('\nYou head out into some nearby woods looking for game. Before sundown, you\'ve')
    print('bagged a deer and a couple rabbits. You return to the wagon, where your family')
    print('is overjoyed to see the catch. Over the best dinner you\'ve had in three months,')
    print('you give thanks to the Lord and sing praises for His many bounteous blessings.')
elif hunger == 'eat':
    print('Sadly, the time has come. While the children are out gathering firewood, you')
    print('take Daisy out behind the wagon and slit her throat. You had grown mighty fond')
    print('of her. With tears in her eyes, your wife prepares supper. You normally love')
    print('the taste of fresh mutton, but tonight the stew seems to have lost its flavor.')
elif hunger == 'settlement':
    print('Miraculously, you find the settlement and are welcomed by the locals. Your leftover')
    print('cash is just enough to buy you food and supplies to last you the rest of your journey.')
else:
    print('\nNice try, but it doesn\'t work. You wander aimlessly accross the plains, hoping now only')
    print('to survive. Your mind goes crazy, and... well... have you ever heard of the Donner Party?')
    you_died()

print('The next morning, you continue on your way. The final stretch throught the Rockies is')
print('strenuous, but working with your sons, you\'re able to pull the wagon through the rough')
print('spots. Finally, you reach the other side and enter the great Salt Lake valley. You drop')
print('to your knees with joy as your children jump excitedly and your wife hugs you tightly.')

print('\nCongratulations! You\'ve completed the game! Thanks for playing!\n')