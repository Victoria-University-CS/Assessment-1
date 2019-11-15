def get_init_input(instruction, options):
    init_prompt = instruction + "({})".format(', '.join(options))
    result = input(init_prompt+ ": ").lower()
    while result not in options:
        result = input(init_prompt+ ": ").lower()

    return result

class Property:
    def __init__(self, square_feets='', num_bedrooms='', num_bathrooms='', **kwargs):
        self.square_feets = square_feets
        self.num_bathrooms = num_bathrooms
        self.num_bedrooms = num_bedrooms
    
    def display(self):
        print(f"PROPERTY DETAILS\n{'='*20}")
        print(f'Square Feets: {self.square_feets}')
        print(f'Bathrooms: {self.num_bathrooms}')
        print(f'Bedrooms: {self.num_bedrooms} \n')

    def promp_init():
        return dict(
                square_feets = input("Enter the Square Feets: "),
                num_bathrooms=input("Number of Bathrooms: "),
                num_bedrooms = input("Number of Bedrooms: ")
        )
    promp_init = staticmethod(promp_init)


class House(Property):
    valid_garage = ("attached", "detached", "none")
    valid_fenced = ("yes", "no")
    def __init__(self, num_stories='', garage='', fenced='', **kwargs ):
        super().__init__(**kwargs)
        self.num_stories = num_stories
        self.garage = garage
        self.fenced = fenced

    def display(self):
        super().display()
        print(f"HOUSE DETAILS\n{'='*20}")
        print(f'num_stories: {self.num_stories}')
        print(f'garage: {self.garage}')
        print(f'fenced: {self.fenced}')

    def promp_init():
        parent_init = Property.promp_init()

        num_stories = input("Number of Stories: ")
        garage = get_init_input('Garage Specification: ', House.valid_garage)
        fenced = get_init_input('Is the House Fenced?: ', House.valid_fenced)

        parent_init.update({
            "num_stories":num_stories,
            "garage":garage,
            "fenced":fenced
        })
        return parent_init

    promp_init = staticmethod(promp_init)

class Apartment(Property):
    valid_balconies = ("yes", "no", "solarium")
    valid_laundries = ("coin", "ensuite", "none")
    def __init__(self, balcony='', laundry='', **kwargs ):
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        super().display()
        print(f"APARTMENT DETAILS\n{'='*20}")
        print(f'Laundry: {self.laundry}')
        print(f'Balconies: {self.balcony}')

    def promp_init():
        parent_init = Property.promp_init()
        
        balcony = get_init_input('Is there a balcony?: ', Apartment.valid_balconies)
        laundry = get_init_input('Laundry Available: ', Apartment.valid_laundries)

        parent_init.update({
            "balcony":balcony,
            "laundry":laundry
        })
        return parent_init

    promp_init = staticmethod(promp_init)

class Purchase:
    def __init__(self, price='', taxes='', **kwargs):
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        super().display()
        print(f"PURCHASE DETAILS\n{'='*20}")
        print(f'Selling Price: {self.price}')
        print(f'Tax Involed: {self.taxes}')

    def promp_init():
        return dict(
                price = input("Selling Price: "),
                taxes=input("Total Tax: ")
        )
    promp_init = staticmethod(promp_init)

class Rental:
    def __init__(self, furnished='', utilities='', rent='', **kwargs):
        super().__init__(**kwargs)
        self.furnished = furnished
        self.utilities = utilities
        self.rent = rent

    def display(self):
        super().display()
        print(f"RENT DETAILS\n{'='*20}")
        print(f'Furnishing: {self.furnished}')
        print(f'Available Utilities: {self.utilities}')
        print(f'Monthly Rent: {self.rent}')

    def promp_init():
        return dict(
                furnished = get_init_input("Is the House Furnished: ", ("yes", "no")),
                utilities=input("Utilities Available: "),
                rent=input("Monthly rent: ")
        )
    promp_init = staticmethod(promp_init)

class HouseRental(Rental, House):
    def promp_init():
        init = House.promp_init()
        init.update(Rental.promp_init())
        return init
    promp_init = staticmethod(promp_init)
    

class HousePurchase(Purchase, House):
    def promp_init():
        init = House.promp_init()
        init.update(Purchase.promp_init())
        return init
    promp_init = staticmethod(promp_init)

class ApartmentRental(Rental, Apartment):
    def promp_init():
        init = Apartment.promp_init()
        init.update(Rental.promp_init())
        return init
    promp_init = staticmethod(promp_init)

class ApartmentPurchase(Purchase, Apartment):
    def promp_init():
        init = Apartment.promp_init()
        init.update(Purchase.promp_init())
        return init 
    promp_init = staticmethod(promp_init)


class Agent:
    def __init__(self):
        self.property_list = []

    agent_choice = {
        ("house", "rental"):HouseRental,
        ("house", "purchase"):HousePurchase,
        ("apartment", "rental"):ApartmentRental,
        ("apartment", "purchase"):ApartmentPurchase
    }

    def add_property(self):
        property_type = get_init_input('Which Property? ', ("house", "apartment"))
        purchase_type = get_init_input('Purchase Type? ', ("rental", "purchase"))

        propertyClass = self.agent_choice[(property_type, purchase_type)]
        prompts =  propertyClass.promp_init()
        # print(prompts)

        self.property_list.append(propertyClass(**prompts))

    def display_property(self):
        for property in self.property_list:
            property.display()



agent = Agent()
agent.add_property()
agent.display_property()