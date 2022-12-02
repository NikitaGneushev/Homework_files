cook_book = {}

with open('data.txt', 'rt', encoding='utf-8') as file:
    for l in file:
        cook_name = l.strip()
        dictik = []
        employees_count = file.readline()
        for i in range(int(employees_count)):
            eat = file.readline()
            ingredient_name, quantity, measure = eat.strip().split(' | ')
            dictik.append({'ingredient_name': ingredient_name,
                           'quantity': int(quantity),
                           'measure': measure})
            dep = {cook_name: dictik}
        blank_line = file.readline()
        cook_book.update(dep)
# print(f'cook_book = {cook_book}')
# print(dep)
# print(cook_book)
print(cook_book.values())

def list_of_stores_with_ingredients(dishes, person_count):
    result = {}
    for dish in dishes:
        if dish in cook_book:
            for consist in cook_book[dish]:
                if consist['ingredient_name'] in result:
                    result[consist['ingredient_name']]['quantity'] += consist['quantity'] * person_count
                else:
                    result[consist['ingredient_name']] = {'measure': consist['measure'],
                                                       'quantity': (consist['quantity'] * person_count)}
        else:
            print(f'Блюда "{dish}" нет в книге рецептов')
    print (result)

list_of_stores_with_ingredients(['Омлет', 'Фахитос'], 3)





# def rewrite_file(path1=None, path2=None, path3=None):
#     if path1 or path2 or path3 is None:
#         path1 = '1.txt'
#         path2 = '2.txt'
#         path3 = '3.txt'
#         os.chdir('sorted')
#         outout_file = "rewrite_file.txt"
#         file1_path = os.path.join(os.getcwd(), path1)
#         file2_path = os.path.join(os.getcwd(), path2)
#         file3_path = os.path.join(os.getcwd(), path3)
#         with open(file1_path, 'r', encoding='utf-8') as f1:
#             file1 = f1.readlines()
#         with open(file2_path, 'r', encoding='utf-8') as f2:
#             file2 = f2.readlines()
#         with open(file3_path, 'r', encoding='utf-8') as f3:
#             file3 = f3.readlines()
#         with open(outout_file, 'w', encoding='utf-8') as f_total:
#
#
#
#             if len(file1) < len(file2) and len(file1) < len(file3):
#                 f_total.write(path1 + '\n')
#                 f_total.write(str(len(file1)) + '\n')
#                 f_total.writelines(file1)
#                 f_total.write('\n')
#             elif len(file2) < len(file1) and len(file2) < len(file3):
#                 f_total.write(path2 + '\n')
#                 f_total.write(str(len(file2)) + '\n')
#                 f_total.writelines(file2)
#                 f_total.write('\n')
#             elif len(file3) < len(file1) and len(file3) < len(file2):
#                 f_total.write(path3 + '\n')
#                 f_total.write(str(len(file3)) + '\n')
#                 f_total.writelines(file3)
#                 f_total.write('\n')
#             if len(file2) > len(file1) > len(file3) or len(file2) < len(file1) < len(
#                     file3):
#                 f_total.write(path1 + '\n')
#                 f_total.write(str(len(file1)) + '\n')
#                 f_total.writelines(file1)
#                 f_total.write('\n')
#             elif len(file1) > len(file2) > len(file3) or len(file2) > len(file1) and len(file2) < len(
#                     file3):
#                 f_total.write(path2 + '\n')
#                 f_total.write(str(len(file2)) + '\n')
#                 f_total.writelines(file2)
#                 f_total.write('\n')
#             elif len(file1) > len(file3) > len(file2) or len(file3) > len(file1) and len(file3) < len(
#                     file2):
#                 f_total.write(path3 + '\n')
#                 f_total.write(str(len(file3)) + '\n')
#                 f_total.writelines(file3)
#                 f_total.write('\n')
#             if len(file1) > len(file2) and len(file1) > len(file3):
#                 f_total.write(path1 + '\n')
#                 f_total.write(str(len(file1)) + '\n')
#                 f_total.writelines(file1)
#             elif len(file2) > len(file1) and len(file2) > len(file3):
#                 f_total.write(path2 + '\n')
#                 f_total.write(str(len(file2)) + '\n')
#                 f_total.writelines(file2)
#             elif len(file3) > len(file1) and len(file3) > len(file2):
#                 f_total.write(path3 + '\n')
#                 f_total.write(str(len(file3)) + '\n')
#                 f_total.writelines(file3)
#     else:
#         print('Давай лучше без параметров')
#     return
#
# rewrite_file()

