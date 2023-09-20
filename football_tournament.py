football_club_name = input()
number_played_games_for_the_season = int(input())
got_points = 0
win_times = 0
draw_times = 0
lost_times = 0
sum_points = 0
percent_for_win_game = 0
if number_played_games_for_the_season > 0:
    for games in range(number_played_games_for_the_season):
        game_result = input()
        if game_result == "W":
            got_points = 3
            win_times += 1
        elif game_result == "D":
            got_points = 1
            draw_times += 1
        else:
            got_points = 0
            lost_times += 1
        sum_points += got_points
    print(f"{football_club_name} has won {sum_points} points during this season.")
    print("Total stats:")
    print(f"## W: {win_times}")
    print(f"## D: {draw_times}")
    print(f"## L: {lost_times}")
    print(f"Win rate: {win_times/number_played_games_for_the_season*100:.2f}%")
else:
    print(f"{football_club_name} hasn't played any games during this season.")
