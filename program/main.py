from func_connections import connect_to_dydx

if __name__ == "__main__":
    # Connect to client
    try:
        client = connect_to_dydx()
    except Exception as e:
        print(e)
        print("Error connecting to client", e)
        exit(1)