import project_tests


def date_top_industries(prices, sector, date, top_n):
    """
    Get the set of the top industries for the date

    Parameters
    ----------
    prices : DataFrame
        Prices for each ticker and date
    sector : Series
        Sector name for each ticker
    date : Date
        Date to get the top performers
    top_n : int
        Number of top performers to get

    Returns
    -------
    top_industries : set
        Top industries for the date
    """
    # TODO: Implement Function
    print(prices.index)
    # print(prices)
    # print(prices.loc[date].nlargest(top_n).index)
    # print(sector.loc[prices.loc[date].nlargest(top_n).index])
    return set(sector.loc[prices.loc[date].nlargest(top_n).index])


project_tests.test_date_top_industries(date_top_industries)
