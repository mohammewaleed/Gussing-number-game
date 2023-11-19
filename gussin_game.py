import random2;
while True:
  pc_num = random2.randint(1,10)
  print(pc_num)
  attemsps = 0

  while True: 
    player_num = int(input("Pick a number between 1-10: "))
    if 10 >= player_num >= 1:
      attemsps+=1
    else:
      player_num = input("It is invaled,number between 1-10: ")
      continue
    if player_num == pc_num:
      print("Your are won in " + str(attemsps) + " try")
      break
    elif player_num > pc_num:
        print("Your number is greater than pc number.")
    else:
      print("Your number is less than pc number.")
  play_again = input("Do you want to play again?").lower()
  if play_again != "yes":
    print("Thanks, we want to see you again.")
    break