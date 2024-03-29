# My line of code

line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
if position == 'A1': 
  line1[0] = 'X'
if position == 'A2':
  line2[0] = 'X'
if position == 'A3':
  line3[0] = 'X'
if position == 'B1': 
  line1[1] = 'X'
if position == 'B2':
  line2[1] = 'X'
if position == 'B3':
  line3[1] = 'X'
if position == 'C1': 
  line1[2] = 'X'
if position == 'C2':
  line2[2] = 'X'
if position == 'C3':
  line3[2] = 'X'


# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")

# input B3 then answer will be 
#⬜️,⬜️,⬜️
#⬜️,⬜,⬜️
#⬜️,X,⬜️

# other way of coding with nested list
line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# Your code below
letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter)
number_index = int(position[1]) - 1
map[number_index][letter_index] = "X"

print(f"{line1}\n{line2}\n{line3}")
