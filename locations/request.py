LOCATIONS = [
    {
        "id": 1,
        "name": "Nashville North",
        "address": "8422 Johnson Pike"
    },
    {
        "id": 2,
        "name": "Nashville South",
        "address": "209 Emory Drive"
    },
    {
        "name": "East Nashville",
        "address": "111 Eastland Dr",
        "id": 3
    },
    {
        "name": "Franklin",
        "address": "111 Hillsboro",
        "id": 4
    }
]


def get_all_locations():
    """returning the location dictonaries
    """
    return LOCATIONS

# Function with a single parameter


def get_single_location(id):
    """loop over location dictonaries
    """
    # Variable to hold the found location, if it exists
    requested_location = None

    # Iterate the locations list above. Very similar to the
    # for..of loops you used in JavaScript.
    for location in LOCATIONS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if location["id"] == id:
            requested_location = location

    return requested_location

def create_location(location):
    """creating new location
    """
    max_id = LOCATIONS[-1]["id"]
    new_id = max_id + 1

    location["id"] = new_id

    LOCATIONS.append(location)

    return location