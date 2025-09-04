class User:
    def __init__ (self, name,phone,location):
        self.name=name
        self.phone= phone
        self.location=location
        
    # function to display user details
    def display_info(self):
        print(f'Name: {self.name}')
        print(f'Phone: {self.phone}')
        print(f'Location: {self.location}')
