print("Today's date?")
date = input()
print("Breakfast calorie?")
breakfast = int(input())
print("Lunch calorie?")
lunch = int(input())
print("Dinner calorie?")
dinner = int(input())
print("Snack calorie?")
snack = int(input())
total_calorie = breakfast + lunch + dinner + snack
print(f'Calorie content for {date}: {total_calorie}')