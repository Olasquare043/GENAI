import user as User
class Farmer(User):
    def __init__(self,name,phone,location,farm_size,major_crop):
        # calling the parent constructor for common attributes
        super().__init__(name,phone,location)
        # extra attributes
        self.farm_size=farm_size
        self.major_crop=major_crop

# function Farmer Registration
    def registration(self):
        try:
            with open("farmers.txt", "a") as file:
                file.write(f"{self.name},{self.phone},{self.location},{self.farm_size},{self.major_crop}\n")
        except Exception as e:
            print(e)

# function to load farmers record to list
    def get_farmers(self):
        farmers = []
        try:
            with open("farmers.txt", "r") as file:
                for line in file:
                    name, phone, location, farm_size, major_crop = line.strip().split(",")
                    farmers.append({
                        "name": name,
                        "phone": phone,
                        "location": location,
                        "farm_size": farm_size,
                        "major_crop": major_crop
                    })
        except Exception as e:
            print(e)
        return farmers

# Display information
    def display_info(self):
        super().display_info()
        print(f"Farm Size: {self.farm_size}")
        print(f"Major Crop: {self.major_crop}")