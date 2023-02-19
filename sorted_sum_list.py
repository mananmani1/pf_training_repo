def list_of_numbers():
    while True: 
            final_list =[]
            lenth_of_list = input('How much elements in your list?\t \n')
            if lenth_of_list.isdigit():
                for i in range(0,int(lenth_of_list)):
                    while True:
                        try:                          
                            num = int(input(f"Your element at {i} index:\t"))
                            final_list.append(num)
                            final_list.sort()
                            break                     
                        except ValueError: 
                             print('invalid input ! Please input integer value')
                        continue
            else:
                print('invalid input ! Please input Positive integer value')   
                continue
            break
    print('Your Sorted List: ',final_list)
            
                
    while True:
        try:
    
            new_input = input('would you like add another values?yes/no\t \n').lower()
            if new_input == 'no':
                print('Your Final Sorted List: ',final_list)     
                print('\nThanks for using our services(PF-Ltd.)')
                break
            elif new_input == 'yes':
                while True:
                    try:
                        num_2 = int(input('Please enter your new value:\t \n'))
                        final_list.append(num_2)
                        final_list.sort()
                        print(final_list)
                        
                        break
                    except ValueError: 
                        print('invalid input ! Please input integer value')
                    
            else:
                print("Please type 'yes' or 'no' ")
        except ValueError:
            print('invalid')
            
list_of_numbers()
    


