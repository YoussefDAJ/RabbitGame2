print("Welcome to place the rabbit\n")
field = [["🥬", "🥬", "🥬"], ["🥬", "🥬", "🥬"], ["🥬", "🥬", "🥬"]]

print(f"{field[0]} \n{field[1]} \n{field[2]}")
print("\nWhere should the rabbit go? 🐇")

position = input("Please choose a row and a column  ")
row = int(position[0])
column = int(position[1])

# field[row][column] = "🐇" #this will give us error in placement

field[row - 1][column - 1] = "🐇"

print("\nSucess  ... \n")
print(f"{field[0]} \n{field[1]} \n{field[2]}")
