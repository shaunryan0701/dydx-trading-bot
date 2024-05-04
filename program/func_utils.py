from datetime import datetime, timedelta

def format_number(curr_number, match_number):
    """
    Give curr_number an example of a number with decimals desired
    Function will return the correctly formatted string
    """
    curr_number_string = f"{curr_number}"
    match_number_string = f"{match_number}"

    if "." in match_number_string:
        match_decimals = len(match_number_string.split(".")[1])
        curr_number_string = f"{curr_number:.{match_decimals}f}"
        curr_number_string = curr_number_string[:]
        return curr_number_string
    else:
        return f"{int(curr_number)}"
    
def format_time(timestammp):
    return timestammp.replace(microsecond=0).isoformat()

def get_ISO_times():
    # get timestamps
    date_start_0 = datetime.now()
    date_start_1 = date_start_0 - timedelta(hours=100)
    date_start_2 = date_start_1 - timedelta(hours=100)
    date_start_3 = date_start_2 - timedelta(hours=100)
    date_start_4 = date_start_3 - timedelta(hours=100)

    # formt datetimes
    times_dict = {
        "range_1": {
            "from_iso": format_time(date_start_1),
            "to_iso": format_time(date_start_0)
        },
        "range_2": {
            "from_iso": format_time(date_start_2),
            "to_iso": format_time(date_start_1)
        },
        "range_3": {
            "from_iso": format_time(date_start_3),
            "to_iso": format_time(date_start_2)
        },
        "range_4": {
            "from_iso": format_time(date_start_4),
            "to_iso": format_time(date_start_3)
        }
    }

    # return results
    return times_dict
