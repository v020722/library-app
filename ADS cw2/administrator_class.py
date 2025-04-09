class Administrator:
    def __init__(self, username, password, first_name, last_name):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

    def display_details(self):
        print("Administrator Details:")
        print("Username:", self.username)
        print("First Name:", self.first_name)
        print("Last Name:", self.last_name)

    def authenticate(self, username, password):
        return self.username == username and self.password == password

