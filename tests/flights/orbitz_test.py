from tests.base_test import BaseTestCase
from tests.pages.index_page import IndexPage
from tests.pages.search_result_page import SearchResultPage


class MulticityTestClass(BaseTestCase):
    def test_multicity_flights(self):
        # use cities names in this test, not airport names. Added custom checks for this.
        # in this test you can use dynamic number of cities (but not less than 2) and children
        # without additional refactoring.
        # Just edit/import values to "cities" list or/and passengers dict

        passengers = {
            'adults': "2",
            'children': {'age': ["2", "4"]}
        }
        cities = ["New York", "Los Angeles", "Dallas"]

        cities_as_looped_pairs = self.cities_loop_as_pairs(cities)
        departures_date = self.get_departure_days(len(cities_as_looped_pairs))
        cities_with_departures = list(zip(cities_as_looped_pairs, departures_date))

        self.open(IndexPage.url)

        self.click(IndexPage.flights_tab)
        self.click(IndexPage.multi_city_button)
        # select how many passengers
        self.select_option_by_value(IndexPage.adults_dropdown, passengers['adults'])
        self.select_option_by_value(IndexPage.children_dropdown, str(len(passengers['children']['age'])))

        # select age for children
        for child, child_age in enumerate(passengers['children']['age'], 1):
            self.select_option_by_value(IndexPage.child_age_selector(str(child)), child_age)

        # click on "+ Add another flight" enough to fill all cities info
        for _ in range(len(cities_with_departures) - 2):
            self.click(IndexPage.add_another_flight_link)

        for idx, (city, departure_date) in enumerate(cities_with_departures, 1):
            # input Flying from
            self.select_all_airports_in_city(
                IndexPage.flying_from_selector_by_index(idx),
                city[0],  # ['New York', 'Los Angeles'][0]
                IndexPage.all_airports_in_city_by_city_name(city[0]))

            # input Flying to
            self.select_all_airports_in_city(
                IndexPage.flying_to_selector_by_index(idx),
                city[1],  # ['New York', 'Los Angeles'][1]
                IndexPage.all_airports_in_city_by_city_name(city[1]))

            # fill Departing date field
            self.add_text(IndexPage.departure_date_selector_by_index(idx), departure_date)

        self.click(IndexPage.search_button)

        # Now we on Search result page
        self.wait_for_element(SearchResultPage.offer_block)
        print("\nSearch results available:", len(self.find_elements(SearchResultPage.offer_block)))
        # assuming that default order is by lowest price: the first item price will be the lowest one
        print("\nLowest Price:", self.get_text(SearchResultPage.first_block_price()))

