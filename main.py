class Beverage:
    prices = {"Strawberries": 1.5, "Banana": 0.5, "Mango": 2.5,
              "Blueberries": 1, "Raspberries": 1, "Apple": 1.75,
              "Pineapple": 3.5}
    cout = 0

    def __init__(self, ingredients):
        self.ingredients = ingredients

    def get_cost(self):
        for i in self.ingredients:
            for k, v in self.prices.items():
                if i == k:
                    self.cout += v
        return f"${self.cout:.2f}"

    def get_price(self):
        return f"${self.cout * 2.5:.2f}"

    def get_name(self):
        cout = 0
        x = []
        ingred = [name.replace("berries", "berry") for name in self.ingredients]
        ingred.sort()
        for i in ingred:
            x.append(i)
            cout += 1
        st = " ".join([str(item) for item in x])
        if cout == 1:
            return f"{st} Smoothie"
        elif cout > 1:
            return f"{st} Fusion"
