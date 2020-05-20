class SearchResultPage:
    offer_block = "//ul[@id='flightModuleList']/li[@data-test-id='offer-listing']"

    @staticmethod
    def first_block_price():
        offer_block = SearchResultPage.offer_block
        return f"({offer_block}//span[@data-test-id='listing-price-dollars'])[1]"
