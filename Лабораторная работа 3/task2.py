def find_common_participants(group1, group2, sep=','):
    participants_group1 = set(group1.split(sep))
    participants_group2 = set(group2.split(sep))
    common_participants = list(participants_group1.intersection(participants_group2))
    return sorted(common_participants)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

find = find_common_participants(participants_first_group, participants_second_group)
print(find)