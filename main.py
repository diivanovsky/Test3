
# data_to_write = "smth new", "another new shit"
#
# with open("write_file.txt", "rb") as f:
#     data = f.read()
#     print(data.decode("utf-8"))

import json
import csv
with open("classmates.csv", "w") as w_file:
    file_writer = csv.writer(w_file, delimiter=",")
    file_writer.writerow(["Имя", "Класс", "Возраст"])
    file_writer.writerow(["Лиза", "8", "13"])
    file_writer.writerow(["Катя", "7", "12"])
    file_writer.writerow(["Антон", "7", "12"])
    file_writer.writerow(["Сережа", "7", "12"])
with open("employees.csv", "r", encoding="utf-8") as r_file:
    file_reader = csv.reader(r_file, delimiter=',')
    count = 0
    for row in file_reader:
        if count == 0:
            print(f"Файл содержит столбцы: {','.join(row)}")
        else:
            print(f"    {row[0]} - {row[1]} - {row[2]}")
        count += 1
    print(f"Total: {count} lines")
data = {
    "employees":
        [
            {
                "name": "John",
                "salary": 900
            },
            {
                "name": "Rick",
                "salary": 1500
            },
            {
                "name": "Morty",
                "salary": 100
            }
        ]
}
with open("employees.json", "w") as jf:
    json.dump(data, jf, indent=4)


# Task 1
# def count(lst):
#     counts = {}
#     for w in lst:
#             if w in counts:
#                 cnt = counts.get(w, 0)
#                 counts[w] = cnt + 1
#             else:
#                 counts[w] = 1
#     return counts
#
#
# with open("text.txt", "r") as t:
#     text = t.readlines()
#     lines = list(map(lambda x: x.lower().split(), text))
#     w_counts = []
#     # print(lines)
#     for words in lines:
#         w_counts.append(count(words))
#         print(w_counts)
#         for i in w_counts:
#             max_word = max(w_counts, key=w_counts.get)
#             with open('output.txt', 'w') as f:
#                 f.write(f"{max_word} {w_counts[max_word]}")