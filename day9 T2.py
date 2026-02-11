class Mobile:
    
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    # Equality method
    def __eq__(self, other):
        if isinstance(other, Mobile):
            return self.brand == other.brand and self.model == other.model
        return False


# Creating 3 objects
mobile1 = Mobile("Samsung", "Galaxy S23", 80000)
mobile2 = Mobile("Samsung", "Galaxy S23", 75000)
mobile3 = Mobile("Apple", "iPhone 15", 90000)

# Comparing objects using ==
print("mobile1 == mobile2:", mobile1 == mobile2)
print("mobile1 == mobile3:", mobile1 == mobile3)
