from container import ContainerOfUsers
from container import is_float


def menu(container: ContainerOfUsers):
    container.switch(str(input("Enter username: ")))

    while True:
        print("You can enter: add, remove, find, grep, list, load, save, switch or exit to run this method.")
        choice = input("Your choice: ")

        if choice == 'add':
            add_data = input("Enter data to add(one or more elements separated by spaces): ").split(' ')
            if len(add_data) == 0:
                continue
            i = 0
            while i < len(add_data):
                if add_data[i].isdigit():
                    add_data[i] = int(add_data[i])
                elif is_float(add_data[i]):
                    add_data[i] = float(add_data[i])
                elif len(add_data[i]) >= 2 and (add_data[i][0] == '\'' or add_data[i][0] == '\"') and\
                        (add_data[i][-1] == '\'' or add_data[i][-1] == '\"'):
                    add_data[i] = add_data[i][1:len(add_data[i]) - 1]
                i += 1
            container.add(*add_data)
        elif choice == 'remove':
            remove_data = input("Enter data to remove(one element): ")
            if remove_data.isdigit():
                container.remove(int(remove_data))
            elif is_float(remove_data):
                container.remove(float(remove_data))
            elif len(remove_data) >= 2 and (remove_data[0] == '\'' or remove_data[0] == '\"') and\
                    (remove_data[-1] == '\'' or remove_data[-1] == '\"'):
                container.remove(remove_data[1:len(remove_data) - 1])
        elif choice == 'find':
            find_data = input("Enter data to find(one or more elements separated by spaces): ").split(' ')
            i = 0
            while i < len(find_data):
                if find_data[i].isdigit():
                    find_data[i] = int(find_data[i])
                elif is_float(find_data[i]):
                    find_data[i] = float(find_data[i])
                elif len(find_data[i]) >= 2 and (find_data[i][0] == '\'' or find_data[i][0] == '\"') and\
                        (find_data[i][-1] == '\'' or find_data[i][-1] == '\"'):
                    find_data[i] = find_data[i][1:len(find_data[i]) - 1]
                i += 1
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
            ch = input("Do you want to save data to file? If YES - enter Y: ")
            if ch == 'Y':
                container.save()
            break
        else:
            print("Incorrect input. Try again.")


default_user_set = set([1, 2, 3])
cont = ContainerOfUsers(default_user_set)
menu(cont)
