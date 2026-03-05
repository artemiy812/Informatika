list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

middle = len(list_players) // 2  # Находим середину
first_team = list_players[:middle]  # Находим первую команду: от 0 до 2 ("Маша", "Петя", "Саша")
second_team = list_players[middle:]  # Находим вторую команду: от 3 до конца ("Оля", "Кирилл", "Коля")

print(first_team)
print(second_team)