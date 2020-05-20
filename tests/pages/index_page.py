class IndexPage:

    url = "https://www.orbitz.com/"

    flights_tab = "#tab-flight-tab-hp"
    multi_city_button = "#flight-type-multi-dest-label-hp-flight"

    flying_city_autocomplete_results = "ul#typeaheadDataPlain > div.display-group-results > li.results-item"
    first_city_airport_from_results = "(//ul[@id='typeaheadDataPlain']//cdt/div[contains(text(), 'City')])[1]"

    departing_input = "#flight-departing-single-hp-flight"

    adults_dropdown = "#flight-adults-hp-flight"
    children_dropdown = "#flight-children-hp-flight"

    add_another_flight_link = "#add-flight-leg-hp-flight"

    search_button = "//button[@type='submit']/span[contains(text(), 'Search')]"


    @staticmethod
    def all_airports_in_city_by_city_name(city_name: str):
        return f"//ul[@id='typeaheadDataPlain']//strong[contains(text(), '{city_name}')]/../../cdt/div[contains(text(), 'City')]"

    @staticmethod
    def child_age_selector(child: str):
        return f"#flight-age-select-{child}-hp-flight"

    @staticmethod
    def departure_date_selector_by_index(index: int):
        if index == 1:
            return "input#flight-departing-single-hp-flight"
        else:
            return f"input#flight-{index}-departing-hp-flight"

    @staticmethod
    def flying_from_selector_by_index(index: int):
        if index == 1:
            return "input#flight-origin-hp-flight"
        else:
            return f"input#flight-{index}-origin-hp-flight"

    @staticmethod
    def flying_to_selector_by_index(index: int):
        if index == 1:
            return "input#flight-destination-hp-flight"
        else:
            return f"input#flight-{index}-destination-hp-flight"
