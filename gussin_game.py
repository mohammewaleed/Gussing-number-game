import random2;

pc_num = random2.randint(1,10)
print(pc_num)
attemsps = 0

while True: 
  player_num = int(input("Enter a number between 1-10: "))
  if 10 >= player_num >= 1:
    attemsps+=1
  else:
    player_num = input("It is invaled,number between 1-10: ")

  if player_num == pc_num:
    print("Your are won in " + str(attemsps) + " try")
    break
  elif player_num > pc_num:
      print("Your number is greater than pc number.")
  else:
    print("Your number is less than pc number.")
