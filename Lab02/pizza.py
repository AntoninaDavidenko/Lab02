class Pizza:
    def __init__(self, ingredients, name):
        self.ingredients = ingredients
        self.name = name

    def __str__(self):
        return f"Pizza of the day is {self.name}! Ingredients: %s" % str(self.ingredients)

    @classmethod
    def monday(cls):
        return cls(['cheese', 'tomatoes'], 'Margherita')

    @classmethod
    def tuesday(cls):
        return cls(['cheese', 'tomatoes', 'ham', 'mushrooms'], 'Prosciutto')

    @classmethod
    def wednesday(cls):
        return cls(['tomatoes', 'olive', 'onion', 'mushrooms', 'green pepper'], 'Vegetarian')

    @classmethod
    def thursday(cls):
        return cls(['cheese', 'pineapple', 'ham', ], 'Hawaiian')

    @classmethod
    def friday(cls):
        return cls(['cheese', 'pepperoni'], 'Pepperoni')

    @classmethod
    def saturday(cls):
        return cls(['pepperoni', 'sausage', 'ham', 'beef', 'bacon', 'cheese'], 'Meatzza')

    @classmethod
    def sunday(cls):
        return cls(['chicken', 'red onion', 'cheese', 'BBQ sauce'], 'BBQ Chicken')

    def add(self, ingredients):
        self.ingredients.extend([ingredients])
        print("New ingredients added: ", self.ingredients)


print(Pizza.monday())
Pizza.monday().add('cheese')
