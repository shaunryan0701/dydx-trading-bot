from func_connections import connect_to_dydx
from func_private import abort_all_open_positions
from func_public import construct_market_prices
from constants import ABORT_ALL_POSITIONS, FIND_COINTEGRATED


if __name__ == "__main__":
    # Connect to client
    try:
        print("Connecting to client")
        client = connect_to_dydx()
    except Exception as e:
        print(e)
        print("Error connecting to client", e)
        exit(1)

    # Abort all open positions
    if ABORT_ALL_POSITIONS:
        try:
            print("Closing all positions")
            close_orders = abort_all_open_positions(client)
        except Exception as e:
            print(e)
            print("Error connecting to client", e)
            exit(1)

    # find cointegrated pairs
    if FIND_COINTEGRATED:
        # construct market prices
        try:
            print("Fetching market prices, please allow 3 minutes")
            df_market_prices = construct_market_prices(client)
        except Exception as e:
            print(e)
            print("Error constructing market prices", e)
            exit(1)        
