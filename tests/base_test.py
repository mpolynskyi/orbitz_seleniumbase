from seleniumbase import BaseCase
from datetime import date, timedelta
from random import randrange


class BaseTestCase(BaseCase):
    def select_all_airports_in_city(self, flying_input_locator: str, city_name: str, city_locator: str):
        self.click(flying_input_locator)
        self.add_text(flying_input_locator, city_name)
        self.click(city_locator)

    def get_departure_days(self, number_of_dates):
        dates = []
        last_date = None
        for _ in range(number_of_dates):
            delta = randrange(2, 16)
            if not dates:
                last_date = date.today() + timedelta(days=delta)
                dates.append(last_date)
            else:
                last_date = last_date + timedelta(days=delta)
                dates.append(last_date)

        return [str_dates.strftime("%m/%d/%Y") for str_dates in dates]

    def cities_loop_as_pairs(self, city_list):
        """
        >>cities_loop_as_pairs(["New York", "Los Angeles", "Dallas"])
        [['New York', 'Los Angeles'], ['Los Angeles', 'Dallas'], ['Dallas', 'New York']]
        """
        res = []
        for item in city_list[1:]:
            res.append(item)
            res.append(item)
        res = [city_list[0]] + res + [city_list[0]]
        pairs = [[res[i], res[i + 1]] for i in range(len(res) - 1)[::2]]
        return pairs
