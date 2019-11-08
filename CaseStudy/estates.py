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
    pass



class HousePurchase(Purchase, House):
    pass

class ApartmentRental(Rental, Apartment):
    pass



class ApartmentPurchase(Purchase, Apartment):
    pass



class Agent:
    pass

