#функция часть кода которую можно призвать многокрано
#Встроенная функция(3)
#abs(модуль числа работает только с int)
#pow(поднимает в степень)
#print("принимает множество данных)
#input(принимает один аргумент(описание))
#len
#list(списки)
#tuple(преобразовывает в кортежи)
#int
#string
#type
#dir(сколько методов имеет тип данных)
#map(),filter(),raduce():(принимает более двух аргументов первый это функция)
#def add(x):
#    return x+7
#lists = [3, 5, 8, 12]
#add_to = list(map(add(), lists))
#print(add_to)
#def fact(a):
 #   if a<0:
  #      a=abs(a)
   # x=1
    #for i in range(1, a +1):
     #   x*=i
    #  return x
#lists = [-3, 5, -8, 2]
#lists_new = list(map(fact, lists))
#print(lists_new)

#def test(x):
   # if x<=3:
       # return x
#numbers = [1, 19, 13, 3, ]
#result= filter(test, numbers)
#print(list(result))

#palindrom
#polindrom=['anna','civic','китнаморенеромантик', 'dan', 'kaneki']

#def is_palindrom(strin):
   # new_str =strin[::-1]
  #  if strin.lower()==new_str.lower():
 #       return strin
#new_polindrom= list(filter(is_palindrom, polindrom))
#print(new_polindrom)


#from functools import reduce
#def proiz(a, b):
#    return a*b
#num=[4, 2, 2, 3]
#numb=reduce(proiz,num)
#print(numb)
#from functools import reduce
#lists= reduce(map(range(1,101))**2 )
#print(lists)


# Напишите код банкомата, который принимает цифру, выдает деньги с номиналом 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 3, 1.
