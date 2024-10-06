import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
actions = [rock , paper , scissors]
user_wins = 0
computer_wins = 0
draws = 0
total_games = 2  # We start with at least 2 games
games_played = 0


#user choice
while games_played < total_games :
  user_choice = int(input("what do you choose? type 0 for rock , 1 for paper , 2 for scissors\n"))
  if user_choice >= 3 or user_choice < 0:
        print("You typed an invalid number, you lose!")
        continue 
  
  print("your choice:")  
  print(actions[user_choice])


  #computer choice
  computer_choice = random.randint(0,2)
  print("computer choice:")           
  print(actions[computer_choice])


  #game rules
  if user_choice == 0 and computer_choice == 2:
    print("You win!")
    user_wins += 1
  elif computer_choice == 0 and user_choice == 2:                 
    print("You lose")
    computer_wins += 1
  elif computer_choice > user_choice:
    print("You lose")
    computer_wins += 1
  elif user_choice > computer_choice:
    print("You win!")
    user_wins += 1
  elif computer_choice == user_choice:
    print("It's a draw")
    draws += 1

  games_played += 1

  #check if user has won 2 games

  if user_wins == 2 :
    print("You won 2 games, the match is over!")
    break


  # Check if computer has won 2 games
  if computer_wins == 2:
    print("The computer won 2 games, the match is over!")
    break

  # Add an extra game if 1 win and 1 draw
  if draws == 1 and (user_wins == 1 or computer_wins == 1) and games_played == 2:
     print("One game was a draw and one was a win. One more game will be played.")
     total_games += 1


   # If user and computer have won 1 game, add a tiebreaker

  if user_wins == 1 and computer_wins == 1 and games_played == 2:
     print("It's a tie! One more game will be played as a tiebreaker.")
     total_games += 1

#final result
if user_wins > computer_wins :
    print(f"Final result: You won the match with {user_wins} wins!")

elif computer_wins > user_wins:
    print(f"Final result: The computer won the match with {computer_wins} wins!")

else:
    print("The match ended in a draw!")

