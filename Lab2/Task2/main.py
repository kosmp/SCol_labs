from container import ContainerOfUsers


def menu(container: ContainerOfUsers):
    container.switch(str(input("Enter username: ")))

    while True:
        print("You can enter: add, remove, find, grep, list, load, save, switch or exit to run this method.")
        choice = input("Your choice: ")

        if choice == 'add':
            add_data = input("Enter data to add(one or more elements separated by spaces): ").split(' ')
            container.add(*add_data)
        elif choice == 'remove':
            remove_data = input("Enter data to remove(one element): ")
            if remove_data.isdigit():
                remove_data = int(remove_data)
            container.remove(remove_data)
        elif choice == 'find':
            find_data = input("Enter data to find(one or more elements separated by spaces): ").split(' ')
            container.find(*find_data)
        elif choice == 'grep':
            regex = str(input("Enter a regular expression to find: "))
            container.grep(regex)
        elif choice == 'load':
            container.load()
        elif choice == 'save':
            container.save()
        elif choice == 'switch':
            ch = input("Do you want to save data to file? If YES - enter Y: ")
            if ch == 'Y':
                container.save()

            new_username = input("Enter new username: ")
            container.switch(new_username)

            ch = input("Do you want to load data from file? If YES - enter Y: ")
            if ch == 'Y':
                container.load()
        elif choice == 'list':
            container.list()
        elif choice == 'exit':
            ch = input("Do you want to save data to file? If YES - enter Y")
            if ch == 'Y':
                container.save()
            break
        else:
            print("Incorrect input. Try again.")


default_user_set = set([1, 2, 3])
cont = ContainerOfUsers(default_user_set)
menu(cont)
