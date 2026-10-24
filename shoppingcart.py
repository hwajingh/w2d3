try:
    from IPython.display import clear_output
except ImportError:  # FIX: allow running outside a notebook
    def clear_output():
        pass

# Ask the user 5 bits of input: Do you want to : Show/Add/Delete/clear or Quit?

def shoppingcart():
    emptyset = set() 
    
    while True:
        # FIX: normalise the command once, instead of move.lower() five times.
        move = input("Do you want to : Show/Add/Delete/clear or Quit? ").strip().lower()
        if move == 'show':
            print(f"The shopping list has: ")
            for x in emptyset:
                print(x,  end =" ")
        elif move == "add":
            item = input("what to add? ")
            emptyset.add(item)
        elif move == "delete":
            rm = input("what to remove ")
            # FIX: discard() instead of remove() — removing a missing item
            # used to raise KeyError.
            emptyset.discard(rm)
        elif move == "clear":
            emptyset.clear()
        elif move == 'quit':
            print(f"The list has: ")
            for stuff in emptyset:
                print(stuff,  end =" ")
            break
        else:
            clear_output()
            
shoppingcart()
