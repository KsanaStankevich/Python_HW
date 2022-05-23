# Напишите программу, удаляющую из текста все слова, содержащие "абв".

my_str = 'Напиабвшите прогабврамму, удабваляющую из тексабвта все слова, содержащие"абв"'
my_str = my_str.split(' ')
result = ' '.join(list(filter(lambda word: word.find('абв') == -1, my_str)))
print(result)