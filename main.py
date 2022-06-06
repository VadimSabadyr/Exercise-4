class Beverage:

    prices = {"Strawberries": 1.5, "Banana": 0.5, "Mango": 2.5,
              "Blueberries": 1, "Raspberries": 1, "Apple": 1.75,
              "Pineapple": 3.5}
    def __init__(self, ingredients, c = 0.00, cout = 0):
        self.ingredients = ingredients
        self.c = c
        self.cout = cout


    def get_cost(self):
        for i in self.ingredients:
            for k, v in self.prices.items():
                if i == k:
                    self.c += v
        x = self.c
        return f"${self.c:.2f}"

    def get_price(self):
        return f"${self.c * 2.5:.2f}"


    def get_name(self):
        x = []
        self.ingredients = [name.replace("berries", "berry") for name in self.ingredients]
        name = self.ingredients.sort()
        for i in self.ingredients:
            x.append(i)
            self.cout += 1
        st = " ".join([str(item) for item in x])
        if self.cout == 1:
            return f"{st} Smoothie"
        elif self.cout > 1:
            return (f"{st} Fusion")
