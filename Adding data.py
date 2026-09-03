from csv import writer

for y in range(0, 10):
    home_team = input("Home team: ")
    away_team = input("Away team: ")
    home_goal = int(input("Home goal: "))
    away_goal = int(input("Away goal: "))
    result = input("Result: ")
    new_row = ['NA', 'NA', home_team, away_team, home_goal, away_goal, result, 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA']

    with open('results.csv', 'a', newline='') as f:
        writer_obj = writer(f)
        writer_obj.writerow(new_row)