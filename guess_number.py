from getpass import getpass as input
cout_p_1 = 0
cout_p_2 = 0
print("Rules of Game:")
print()

print("Enter 'R' or 'r' for Rock")
print("Enter 'P' or 'p' for Paper")
print("Enter 'S' or 's' for Sesser")
print()

print("A person who wins first three time wil be the winner of the game")
print()

while(True):
  player_1 = input("Player1 turn(R,P,S): ")
  if(player_1 != 'R' and player_1 != 'r' and player_1 != 'P' and player_1 != 'p' and player_1 != 'S' and player_1 != 's'):
    print("Sorry You Entered Wrong input!")
    continue

  player_2 = input("Player2 turn(R,P,S): ")
  if(player_2 != 'R' and player_2 != 'r' and player_2 != 'P' and player_2 != 'p' and player_2 != 'S' and player_2 != 's'):
    print("Sorry You Entered Wrong input!")
    continue

  print()
  if(player_1 == player_2):
    print("Player1 selected ",player_1)
    print("Player2 selected ",player_2)
    print("Game Tie")
    print()
    continue

  elif(player_1 == 'R' or player_1 == 'r'):
    if(player_2 == 'S' or player_2 == 's'):
      print("Player1 selected ",player_1)
      print("Player2 selected ",player_2)
      print("Rock smashes scissors!")
      print("player_1 Win")
      print()
      cout_p_1 += 1
      
      
    else:
      print("Player1 selected ",player_1)
      print("Player2 selected ",player_2)
      print("Paper covers rock!")
      print("player_2 Win")
      print()
      cout_p_2 += 1
    
  elif(player_1 == 'P' or player_1 == 'p'):
    if(player_2 == 'R' or player_2 == 'r'):
      print("Player1 selected ",player_1)
      print("Player2 selected ",player_2)
      print("Paper covers rock!")
      print("player_1 Win")
      print()
      cout_p_1 += 1
      
      
    else:
      print("Player1 selected ",player_1)
      print("Player2 selected ",player_2)
      print("Scissors cuts paper!")
      print("player_2 Win")
      print()
      cout_p_2 += 1
      
    
  elif(player_1 == 'S' or player_1 == 's'):
    if(player_2 == 'R' or player_2 == 'r'):
      print("Player1 selected ",player_1)
      print("Player2 selected ",player_2)
      print("Rock smashes scissors!")
      print("player_2 Win")
      print()
      cout_p_2 += 1
      
      
    else:
      print("Player1 selected ",player_1)
      print("Player2 selected ",player_2)
      print("Scissors cuts paper!")
      print("player_1 Win")
      print()
      cout_p_1 += 1
      
  if(cout_p_1 == 3):
      print("Player1 Win")
      break
  elif(cout_p_2 == 3):
      print("Player2 Win")
      break