def calculate_lot(confidence):

    if confidence >= 97:
        return 3

    elif confidence >= 90:
        return 2

    else:
        return 1


def expiry_time(confidence):

    if confidence >= 97:
        return "1 Minute"

    elif confidence >= 90:
        return "2 Minutes"

    else:
        return "5 Minutes"
