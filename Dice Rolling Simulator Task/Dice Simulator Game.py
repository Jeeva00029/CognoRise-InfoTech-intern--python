"""
Dice Simulators
two players to play a game with
5 rounds. finally announce a winner in a battle.
"""
import random
print("||======DICE SIMULATOR GAME======||")
player_1_score=0
player_2_score=0
player_1=input("Player 1->Enter your Name:")
player_2=input("Player 2->Enter your Name:")
round=int(input("How many rounds you need:"))
for i in range(1,round+1):
    print("**** Round",i,"****")
    player_1_roll=input("click enter {}-->".format(player_1))
    player_1_roll=random.randint(1,6)
    print("{} Dice rolled:".format(player_1),player_1_roll)
    print()
    player_2_roll = input("click enter {}-->".format(player_2))
    player_2_roll = random.randint(1, 6)
    print("{} Dice rolled:".format(player_2),player_2_roll)
    print()
    if(player_1_roll>player_2_roll):
        print("{} wins the round".format(player_1),i)
        player_1_score+=1
    elif(player_1_roll<player_2_roll):
        print("{} wins the round".format(player_2),i)
        player_2_score+=1
    else:
        print("Round",i,"Match Draw")
    print()
if(player_1_score>player_2_score):
    print("||*=*=*=*=*=* {} Wins the Battle *=*=*=*=||".format(player_1))
    print("Congrats {}".format(player_1.upper()))
elif(player_1_score<player_2_score):
    print("||*=*=*=*=*=* {} Wins the Battle *=*=*=*=||".format(player_2))
    print("Congrats {}".format(player_2.upper()))
else:
    print("Match Draw"
          "Play Again.....")
print()
print("(*******^^^THANK YOU^^^******)")