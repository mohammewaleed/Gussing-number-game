import random2

pc_num = random2.randint(1, 10)
print(pc_num)
attempts = 0

while True:
    try:
        player_num = int(input("Enter a number between 1-10: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        continue  # Restart the loop for invalid input

    if 1 <= player_num <= 10:
        attempts += 1

        if player_num == pc_num:
            print(f"Congratulations! You won in {attempts} tries.")
            break  # Exit the loop when the player wins
        elif player_num > pc_num:
            print("Your number is greater than the pc number.")
        else:
            print("Your number is less than the pc number.")
    else:
        print("Invalid input. Please enter a number between 1-10.")
