#Напишите программу, которая по данному числу N от 1 до 9 выводит на экран N пингвинов.
# Изображение одного пингвина имеет размер 5×9 символов, между двумя соседними пингвинами также имеется пустой (из пробелов) столбец.
# Разрешается вывести пустой столбец после последнего пингвина.
# Для упрощения рисования скопируйте пингвина из примера в среду разработки.

n = int(input('Number of the penguins from 1 to 9: ', ))

print(
'     _~_     ' * n,
'    (o o)    ' * n,
'   /  V  \   ' * n,
'  /(  _  )\  ' * n,
'    ^^ ^^    ' * n, sep='\n' )


