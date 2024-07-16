import json

class CountryState:
    def __init__(self):
        self.data = {}  

    def add_pair(self, country, capital):
        self.data[country] = capital

    def delete_pair(self, country):
        if country in self.data:
            del self.data[country]
        else:
            print(f"Pair with key '{country}' not found.")

    def search_by_key(self, country):
        if country in self.data:
            return self.data[country]
        else:
            return f"Capital for {country} not found."

    def search_by_value(self, capital):
        for key, value in self.data.items():
            if value == capital:
                return key
        return f"Country with capital '{capital}' not found."

    def edit_value(self, country, new_capital):
        if country in self.data:
            self.data[country] = new_capital
        else:
            print(f"Pair with key '{country}' not found.")

    def save_data(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.data, file)

    def load_data(self, filename):
        with open(filename, 'r') as file:
            self.data = json.load(file)


cs = CountryState()
cs.add_pair("Kazakhstan", "Astana")
cs.add_pair("USA", "Washington D.C.")
print(cs.data)

cs.save_data("countries.json")

cs2 = CountryState()
cs2.load_data("countries.json")
print(cs2.data)