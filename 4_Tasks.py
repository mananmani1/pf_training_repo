
# def add_to_list(lst):
#     key = input(f"Enter a key: ")
#     value = input("Enter a value: ")
#     for pair in lst:
#         if pair[0] == key:
#             return "Sorry, that key is already filled. Please choose another key."
#     lst.append((key, value))
#     return "Value added successfully!"


# my_list = []
# while True:
#     result = add_to_list(my_list)
#     print(result)
#     if len(my_list) >= 10:
#         break

# # Display only the values in the final list from the tuple of keys and values as values has index 1
# print("Values in the final list:")
# values_list = [pair[1] for pair in my_list]
# print(values_list)



# Task 1

value = []

def add_list():
    key = []
    length=0
    
    while(length<10):
        key_value=input(f'Enter your key {length+1}:\t')
        values=input(f'Enter your value {length+1}:\t')
        if key_value in key:
            print('This key is already filled please choose another key')
            continue
        
        else:
            value.append(values)
            key.append(key_value)
            length+=1
        
    print  ("Your Final List of values:\n\n",value) 


add_list()




# **Task 2**



#get the first of of previous list of values
value_list_length = len(value)
middle_index = value_list_length//2

first_half_list = value[:middle_index]
main_list = []
def q_list():
    #if u want input from user
    # length=0
    # while(length<5):
    #     values=input(f'Enter your value {length+1} out of 5:\t')
    #     main_list.append(values)
    #     length+=1

    print  ("Now You got List as Queue:\n",first_half_list)
    while True:
        another_value = input('will you add another value in your Queue(yes/no):\t').lower()
        if another_value == 'yes':
                new_value=input(f'Enter your value in Queue:\t')
                first_half_list.append(new_value)
                first_half_list.pop(0)
                print("Your Final List as Queue:\n",first_half_list[::-1])
                

        elif another_value =='no':
                print  ("\nYour Final List as Queue:\n",first_half_list[::-1])
                break

q_list()
               
#Task 3
def random_list():
    print  ("\nYou got now simple List :\n",first_half_list)
    while True:
        another_value = input('would you add new value in list(yes/no):\t').lower()
        if another_value == 'yes':
            new_value=input(f'Enter your new value:\t')
            if new_value in first_half_list:
                print('This value is already exist,please try another value')
                continue

            else:
                first_half_list.append(new_value)
                print("Your Final List :\n",first_half_list)


        elif another_value =='no':
                print  ("\nYour Simple Final List :\n",first_half_list)
                break
    


random_list()
    


# **Task 4**


import random
def table_form(a, b):
    print('___ Our Table ___')
    for i in range(a):
        for j in range(b):
            r= random.randint(15,30)
            print(r,end=" ")
        print("")

if __name__ == "__main__":
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of  columns: "))

table_form(rows,cols)

    







