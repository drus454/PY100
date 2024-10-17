users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

number_of_visits = {
    "Общее количество": 0,
    "Уникальные посещения": 0,
}
number_of_visits["Общее количество"] = len(users)
number_of_visits["Уникальные посещения"] = len(set(users))
print(number_of_visits)
