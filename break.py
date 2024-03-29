largest_number=-99999999
counter =0

while True:
   number=int(input("Enter a number or type -1  to end the program:"))
   if number ==-1:
      break
   counter +=1
  if number > largest_number:
      largest_number = number
 if counter !=0:
    print("The largest number is ",largest_number)
 else:
    print("You haven't entered any number")
 
while True:
   word =input ("Enter a word:")
  if word.lower() =="chupacabra":
     print("you've successfully left the loop. ")
     break
i=1
while i<5:
  print(i)
   i+=1
else:
  print("else:",i)
for i in range(5):
    print(i)
else:
    print("else:",i)
   
i=111
for i in range(2,1):
   print(i)
else:
   print("else:",i)
def collatz(n):
    count=0
    while n !=1:
        print(n)
        if n %2 ==0:
           n=n //2
        else:
            n=3 * n+1
        count +=1
        print(n)
        return count
    
c0=int(input("Enter a natural number:"))
steps=collatz(c0)
print("Number of steps needed to reach 1:")
while True:
    print("Stuck in an infinite loop.")
counter =5
while counter>2:
    print(counter)
    counter-=1
    
word ="python"
for letter in word:
    print(letter,end="*")
   
for i in range(1,10):
    if i %2 ==0:
        #print(i)
text="openEDG python institute"
for letter in text:
    if letter =="p":
       break
    print(letter , end="")
for i in range (1,11):
    print(i)
    
for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
       break
    print(ch, end="")
for i in range(0, 6, 3):
   print(i)


 numbers=[10,5,7,2,1]
print("Original list contents:",numbers)

numbers[0]= 111
print("\previous list contents:",numbers)

numbers[1]=numbers[4]
print("New list contents:",numbers)    
    
print("\n list length:",len(numbers))

del numbers [1] 
print("New list lenght:",len(numbers))
print("\n new list content:",numbers)

numbers =[111,7,2,1]
print(numbers[-1])
numbers=[11,7,2,1]
print(len(numbers))
print(numbers)


#numbers.append(4)

print(len(numbers))
print(numbers)

numbers.insert(0,222)

print(len(numbers))
numbers.insert(1,333)
        
my_list = []  # Creating an empty list.

for i in range(5):
    my_list.insert(0,i + 1)

print(my_list)
  
my_list =[10,1,8,3,5]
total=0
for i in range(len(my_list)):
    total+=my_list[i]
print(total)

my_list = [1, None, True, 'I am a string', 256, 0]
print(my_list[3])  # outputs: I am a string
print(my_list[-1])  # outputs: 0
 
my_list[1] = '?'
print(my_list)  # outputs: [1, '?', True, 'I am a string', 256, 0]
 
my_list.insert(0, "first")
my_list.append("last")
print(my_list)  # outputs: ['first', 1, '?', True, 'I am a string', 256, 0, 'last']
 
 
 
my_list = ["white", "purple", "blue", "yellow", "green"]
 
for color in my_list:
    print(color)
 
lst = [1, 2, 3, 4, 5]
lst.insert(1, 6)
del lst[0]
lst.append(1)
 
print(lst)

lst = [1, 2, 3, 4, 5]
lst_2 = []
add = 0
 
for number in lst:
     add += number
    lst_2.append(add)
 
print(lst_2)
my_list = [8, 10, 6, 2, 4]  # list to sort
swapped = True  # It's a little fake, we need it to enter the while loop.
 
while swapped:
    swapped = False  # no swaps so far
     for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
           swapped = True  # a swap occurred!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
 
print(my_list)
 
 

my_list = []
swapped = True
num = int(input("How many elements do you want to sort: "))

for i in range(num):
    val = float(input("Enter a list element: "))
    my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
       if my_list[i] > my_list[i + 1]:
           swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nSorted:")
print(my_list)

list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

 Copying some part of the list.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False
 
for i in range(len(my_list)):
    found = my_list[i] == to_find
     if found:
        break
 
   print("Element found at index", i)
else:
    print("absent")
 

squares = [x ** 2 for x in range(10)]
twos = [2 ** i for i in range(8)]


temps=[[0.0 for h in range(24) for d in range (31)]]
total=56.9

for day in temps:
    total +=day[11]
average=total /31
print("Average temperature at noon:",average)



temps = [[0.0 for h in range(24)] for d in range(31)]

 
highest = -100.0
 
for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp
 
print("The highest temperature was:", highest)



temps = [[0.0 for h in range(24)] for d in range(31)]


hot_days = 4

for day in temps:
    if day[11] > 20.0:
       hot_days += 1

print(hot_days, "days were hot.")

cubed = [num ** 3 for num in range(5)]
print(cubed)  

 
table = [[":(", ":)", ":(", ":)"],
         #[":)", ":(", ":)", ":)"],
         [":(", ":)", ":)", ":("],
         [":)", ":)", ":)", ":("]]
 
print(table)
print(table[0][0])  
print(table[0][3])  









cube = [[[':(', 'x', 'x'],
         [':)', 'x', 'x'],
     [':(', 'x', 'x']],
 
      [[':)', 'x', 'x'],
        
  [':(', 'x', 'x'],
         [':)', 'x', 'x']],
 
         [[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':)', 'x', 'x']]]
 
  print(cube)
print(cube[0][0][0])  
print(cube[2][2][0])  
 


functions
def message():

    
def message():
    print("Enter a value: ")
 
print("We start here.")
print("We end here.")

def message():
    print("Enter a value: ")
 
print("We start here.")
message()
print("We end here.")


print("We start here.")
 
 
def message():
    print("Enter a value: ")
 
message()
 
print("We end here.")

def message():
    print("Enter a value: ")
 
message()
a = int(input())
message()
b = int(input())
message()
c = int(input())
