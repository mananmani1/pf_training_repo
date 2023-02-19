import queue

def lifo_queue():
    q = queue.LifoQueue()

    while True:
        command = input("Please type a command (add/remove/update/clear/close) for your Queue(pile): ")
        
        #Add the item in lifo queue 
        if command == "add":
            while True:          
                length_of_q = input('How much elements do you want in your queue?\t \n')
                if length_of_q.isdigit():
                        for i in range(0,int(length_of_q)):
                                    item = input(f"Enter your item {i+1} to put in Queue: ")
                                    q.put(item)
                                    print(f"Current queue: {q.queue}")
                                    continue
                
                else:
                    print('invalid length formate ! Please enter integer value')
                    continue
                break
                
        #remove single item from lifo queue 
        elif command == "remove":
            try:
                item = q.get_nowait()
                print(f"{item} has been removed from the queue.")
            except queue.Empty:
                print("The queue is already empty.")
                
        #update the item in the lifo queue          
        elif command == "update":
            if q.qsize() == 0: 
                print("The queue is empty.")
            else:
                old_item = input("Enter the item to update: ")
                
                # Get a list of all items in the queue
                queue_list = q.queue
                
                try:
                    # Find the index of the old item in the queue by subtracting index of old item (create the copy on the fly)
                    # from the length of queue list and then subtract 1 because index start from zero unlike length
                    
                    index = len(queue_list) - queue_list[::-1].index(old_item) -1        
                    new_item = input("Enter the new value for the item going to updated: ")
                    queue_list[index] = new_item
                    q = queue.LifoQueue()
                    
                    for item in queue_list:
                        q.put(item)
                    print(f"{old_item} has been updated to {new_item}.")
                    
                except ValueError:
                    print(f"{old_item} is not in the queue.")
                    continue
        
        #remove all the itmes from lifo queue at once
        elif command == 'clear':
            if q.qsize() == 0: 
                print("The queue is already empty.")
            else:
                q = queue.LifoQueue()
                print("The queue has been cleared.")
                
        #close the lifo queue with final que items with termination message      
        elif command == "close":
            print(f'Your Final Queue: {q.queue}')
            print('Thanks for uisng our Services(PF Ltd.)')
            break
            
        else:
            print("Invalid command. Please enter 'add', 'remove','update', 'clear' or 'close' commands.")

        print(f"\nFinal queue: {q.queue}")

lifo_queue()