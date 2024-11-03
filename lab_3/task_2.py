# TODO Напишите функцию find_common_participants
def find_common_participants(first, second, spl=','):
    result = []
    for participant1 in first.split(spl):
        for participant2 in second.split(spl):
            if participant2 == participant1:
                result.append(participant1)
    result.sort()
    return result

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
find_common_participants(participants_first_group, participants_second_group, '|')