import user as User
class Buyer(User):
    def __init__(self,name,phone,location,organization_name):
        # calling the parent constructor for common attributes
        super().__init__(name,phone,location)
        # extra attributes
        self.organization_name=organization_name

# function buyer Registration
    def registration(self):
        try:
            with open("buyers.txt", "a") as file:
                file.write(f"{self.name},{self.phone},{self.location},{self.organization_name}\n")
        except Exception as e:
            print(e)

# function to load buyer record to list
    def get_buyers(self):
        farmers = []
        try:
            with open("buyers.txt", "r") as file:
                for line in file:
                    name, phone, location, organization_name = line.strip().split(",")
                    farmers.append({
                        "name": name,
                        "phone": phone,
                        "location": location,
                        "organization_name": organization_name,
                    })
        except Exception as e:
            print(e)
        return farmers

# Display information
    def display_info(self):
        super().display_info()
        print(f"Farm Size: {self.organization_name}")