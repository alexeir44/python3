#1.Задайте рандомно список из чисел размером N, где N число с клавиатуры. 
  # Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:
#   [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


#def sum_odd_index(lst):
    #s = 0
    #for i in range(len(lst)):
        #if i % 2 != 0:
            #s += lst[i]
    #print(f"Сумма равна: {s}")

#lst = [2, 3, 5, 9, 3]
#sum_odd_index(lst)
#lst = list(map(int, input("Введите числа через пробел:\n").split()))
#sum_odd_index(lst)


#2.Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
#	[2, 3, 4, 5, 6] => [12, 15, 16];
#	[2, 3, 5, 6] => [12, 15]



#my_list = [2, 3, 4, 5, 6]
#result_list = []
#for i in range((len(my_list)+1)//2):
 #    result_list.append(my_list[i]*my_list[len(my_list)-1-i])
#print(result_list)


#3.Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
#   [1.1, 1.2, 3.1, 5, 10.01] => 0.19


#lst = list(map(float, input("Введите числа через пробел:\n").split()))
#new_lst = [round(i%1,2) for i in lst if i%1 != 0]
#print(max(new_lst) - min(new_lst)) 


#4.Напишите программу, которая будет преобразовывать десятичное число в двоичное.

#*Пример:*

#45 -> 101101
#3 -> 11
#2 -> 10

#s = ""
#n = int(input("Введите число для преобразовывания десятичного числа в двоичное:\n"))
#while n != 0:
 #   s = str(n%2) + s
  #  n //=2
#print(s)

#5. Задайте число - размер списка. Составьте список чисел Фибоначчи, 
 #  в том числе для отрицательных индексов.

  #*Пример:*

 #- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]


 
def Fibonacci(n):
    if n in [1, 2]:                       
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

def NegaFibonacci(n):
    if n == 1:                       
        return 1
    elif n == 2:                       
        return -1
    else:
        num1, num2 = 1, -1
        for i in range(2, n):
            num1, num2 = num2, num1 - num2
        return num2

list = [0]
userNumber = int(input('Enter any number: '))
for e in range(1, userNumber + 1):
    list.append(Fibonacci(e))
    list.insert(0, NegaFibonacci(e))
print(list)