class Base:
    def __init__(self):  # initialize the countries container
        self.countries = []  # list that contains lists of astronaut ids for every country
        self.country_sizes = {}  # keeping this piece of data separate, to get rid of counting operation at the end
        self.last_country_id = 0  # id's needed for country_sizes dict to populate properly

    """
        number of possible combinations
    """

    def get_number_of_possible_combinations(self):  # O(n^2)
        combos = 0
        number_of_countries = len(self.country_sizes)
        for i in range(0, number_of_countries - 1):
            for j in range(i + 1, number_of_countries):
                combos += self.country_sizes[i] * self.country_sizes[j]
        return combos

    """
        find the country for new astronaut if his pair belongs to one.
        If not - create the new country list
    """

    def insert_countryman(self, pair: list):  # O(n^2)
        for country_id, astronauts in enumerate(self.countries):
            for a in astronauts:
                if a == pair[0]:
                    astronauts.append(pair[1])
                    self.country_sizes[country_id] += 1
                    return
                if a == pair[1]:
                    astronauts.append(pair[0])
                    self.country_sizes[country_id] += 1
                    return

        self.countries.append(pair)
        self.country_sizes[self.last_country_id] = 2
        self.last_country_id += 1
