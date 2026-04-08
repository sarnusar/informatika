# TODO Напишите функцию find_common_participants

def find_common_participants(group1, group2, delimiter=','): #
  set1 = set(group1.split(delimiter)) #строка group1 разбивается на список имен,который затем превращается в множество
  set2 = set(group2.split(delimiter)) #строка group2 разбивается на список имен,который затем превращается в множество
  common = sorted(list(set1.intersection(set2))) #находим элементы,которые есть сразу в обоих множествах
  return common #функция должна возвращать список
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
result = find_common_participants(participants_first_group, participants_second_group, delimiter="|") #вызов функции,в которую передаются созданные строки
print(result) #вывод результата на экран