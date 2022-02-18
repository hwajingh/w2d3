from IPython.display import clear_output

# Ask the user 5 bits of input: Do you want to : Show/Add/Delete/clear or Quit?

def shoppingcart():
    emptyset = set() 
    
    while True:
        move = input("Do you want to : Show/Add/Delete/clear or Quit? ")
        if move.lower() == 'show':
            print(f"The shopping list has: ")
            for x in emptyset:
                print(x,  end =" ")
        elif move.lower() == "add":
            item = input("what to add? ")
            emptyset.add(item)
        elif move.lower()== "delete":
            rm = input("what to remove ")
            emptyset.remove(rm)
        elif move.lower()=="clear":
            emptyset.clear()
        elif move.lower() == 'quit':
            print(f"The list has: ")
            for stuff in emptyset:
                print(stuff,  end =" ")
            break
        else:
            clear_output()
            
shoppingcart()
