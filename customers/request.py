CUSTOMERS = [
    {
        "id": 1,
        "name": "Hannah Hall",
        "address": "7002 Chestnut Ct",
        "animalId": 1,
        "email": "hannah@kennels.com"
    },
    {
        "id": 2,
        "name": "Jennifer French",
        "address": "100 Home",
        "animalId": 2,
        "email": "jennifer@kennels.com"
    },
    {
        "id": 3,
        "name": "Becky Vanderbeck",
        "address": "1000 Places St",
        "animalId": 3,
        "email": "becky@kennels.com"
    },
    {
        "id": 4,
        "name": "Vicki Picky",
        "address": "Somewhere Lane",
        "animalId": 4,
        "email": "vicki@kennels.com"
    }
]


def get_all_customers():
    """returning the customer dictonaries
    """
    return CUSTOMERS

# Function with a single parameter


def get_single_customer(id):
    """loop over customer dictonaries
    """
    # Variable to hold the found customer, if it exists
    requested_customer = None

    # Iterate the customers list above. Very similar to the
    # for..of loops you used in JavaScript.
    for customer in CUSTOMERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer

def create_customer(customer):
    """creating new customer
    """
    max_id = CUSTOMERS[-1]["id"]
    new_id = max_id + 1

    customer["id"] = new_id

    CUSTOMERS.append(customer)

    return customer