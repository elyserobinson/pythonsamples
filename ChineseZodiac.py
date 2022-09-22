# A program to find out the Chinese zodiac sign for a given year. The Chinese zodiac sign is based on a 12-year cycle, and each year in this cycle is represented by an animal— monkey, rooster, dog, pig, rat, ox, tiger, rabbit, dragon, snake, horse, and sheep.

# A program that prompts the user to specify a year, and then it displays the animal for that year.

year = eval(input("Enter a year: "))
zodiacYear = year % 12
if zodiacYear == 0:
  print("monkey")
elif zodiacYear == 1:
  print("rooster")
elif zodiacYear == 2:
  print("dog")
elif zodiacYear == 3:
  print("pig")
elif zodiacYear == 4:
  print("rat")
elif zodiacYear == 5:
  print("ox")
elif zodiacYear == 6:
  print("tiger")
elif zodiacYear == 7:
  print("rabbit")
elif zodiacYear == 8:
  print("dragon")
elif zodiacYear == 9:
  print("snake")
elif zodiacYear == 10:
  print("horse")
else:
  print("sheep")
