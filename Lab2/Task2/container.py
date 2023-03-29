import re


class ContainerOfUsers:
    current_user = "Pavel"

    def __init__(self, user_set):
        self.storage = {self.current_user: user_set}

    def add(self, *args):
        for el in args:
            self.storage.get(self.current_user).add(el)

    def remove(self,  element):
        for i in self.storage.get(self.current_user):
            if i == element:
                self.storage.get(self.current_user).remove(element)

    def find(self, *args):
        user_set = self.storage.get(self.current_user)
        list_of_found = []
        for el in args:
            if el in user_set:
                print(f"Found {el}")
                list_of_found.append(el)

        if len(list_of_found) == 0:
            print("No such elements")
        else:
            return list_of_found

    def grep(self, regex):
        list_of_found = []
        for el in self.storage.get(self.current_user):
            check_el = re.search(regex, str(el))
            if check_el is not None:
                print(f"Found {el}")
                list_of_found.append(el)

        if len(list_of_found) == 0:
            print("No such elements")
        else:
            return list_of_found

    def load(self):
        with open("test.txt", "r") as file:
            for line in file:
                check_line_format = re.match(r'^[\w-]+:(\s[\w\.-]+)+$', line)
                if not check_line_format:
                    print("Incorrect format for some of the file lines. Data has not been loaded. "
                          "Edit data in the file to load.")
                    print("Correct line format: username: el1 el2 el3 el4 and etc.")
                    break
                if self.current_user in line and check_line_format:
                    lst = re.split(r'\s|\n', line[line.find(':') + 2:])
                    lst.remove('')
                    for el in lst:
                        if el.isdigit():
                            el = int(el)
                        self.storage.get(self.current_user).add(el)

    def save(self):
        with open("test.txt", "w") as file:
            file.write(self.current_user + ':')
            for el in self.storage.get(self.current_user):
                file.write(' ' + str(el))

    def switch(self, new_user):
        if len(new_user) == 0:
            return

        self.current_user = new_user

        if self.current_user not in self.storage:
            self.storage[self.current_user] = set()

    def list(self):
        print(self.storage.get(self.current_user))
