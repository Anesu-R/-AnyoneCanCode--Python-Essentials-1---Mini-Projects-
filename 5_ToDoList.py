#Bug fix - figure out how to break while loop

Decision1 = input("Would you like to add an item to your to-do list? Y/N ")
Additional1 = Decision1 == "Y" or "y"

if Additional1:
    while True:

        new_item = input("Great, what would you like to add? ")

        with open('todo.txt', 'r') as todo_file:
            todo = todo_file.read()

        todo = todo + new_item + '\n'
        with open("todo.txt", "w+") as todo_file:
            todo_file.write(todo)

        Decision2 = input("Would you like to add another item? Y/N")
        if Decision2 == "Y":
            new_item = input("Great, what would you like to add? ")

            with open('todo.txt', 'r') as todo_file:
                todo = todo_file.read()

            todo = todo + new_item + '\n'
            with open("todo.txt", "w+") as todo_file:
                todo_file.write(todo)

            Decision2 = input("Would you like to add another item? Y/N")
        else:
            break

elif Decision1 == "N":
    print("Awesome, you sound up-to-date with everything!")

else:
    print("Oops, that looks like an incorrect entry")







