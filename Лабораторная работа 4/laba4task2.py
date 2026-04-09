import csv #Импортируем csv
import json #Импортируем json
input_csv = "input.csv" #Вводим переменнную
output_json = "output.json" #Вводим переменнную
def convert_csv_to_json() -> None: #объявляем функцию, пометка None означает, что она не возвращает результат через return
    with open(input_csv, "r", encoding="utf-8") as csv_file: #Открываем csv файл для чтения
        reader =  csv.DictReader(csv_file) #создаем "читатель", который воспринимает каждую строку csv как словарь
        rows = list(reader) #превращаем объект-читатель в обычный список, содержащий словари с данными
    with open (output_json, "w", encoding="utf-8") as json_file: #Открывает файл json для записи
        json.dump (rows, json_file, indent=4, ensure_ascii=False) #Преобразуем список data в json и записываем вфайл indent=4 - добавляет отступы по 4 пробела
if __name__== "__main__": #Проверяем:код внутри этого условия выполнится только припрямом запуске файла,а не при егот импорте в другой скрипт
    convert_csv_to_json () #Вызываем функцию, которую описали выше
    with open(output_json) as readable_json: #снова открываем уже созданный json файл,чтобы проверитьт результат
        for line in readable_json: #Запускаем цикл, которая читает файл
            print(line, end="") #Выводим ответ наэкран