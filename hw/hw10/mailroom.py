def initial_prompt():
    """ Request data from the user.

    Inputs are either:
    1) Send Thank you
    2) Create Report
    3) Quit

    calls validate_initial_prompt to verify results
    if not verified will ask user to Inputs

    returns value

    """


def validate_initial_prompt(text):
    """ Validates user input at the initial prompt.

    returns True if data is in correct form
    returns False if it is in an unknown input."""


def enter_name():
    """ Will prompt user to enter donor's name.

    Inputs would be:
    1) Full Name
    2) List
    2) Return to main menu.

    returns full name or command to list all donors.
    """


def check_prior_donations(donor_name):
    """Compares name to names of people who have given in the past.

    Returns True if the name is in the database.
    Returns False if the name is not in the database.

    """


def create_donor(donor_name):
    """ Adds a new donor to the list of donors.

    Donor object created.
    Donation history set to empty."""


def list_donors():
    """ Lists all donors.

    Will sort donors some logical way."""


def input_donation():
    """ Asks user to input a donation amount.

    Returns donation amount in the form of a floating point amount."""


def verify_donation():
    """ Verifies that a correct donation amount has been entered.

    Returns true if it is a valid amount.

    Returns False if it is:
        - has alpha charicters.
        - is negative.
        - has more than 2 decimal places."""


def print_thankyou(donor_object):
    """ Prints a nice thank you letter for the inputted donor.

    Will include a friendly personalized greeting
    to the donot by spicing the given name.

    """


def calculate_total_donation(donor_object):
    """ Calculates the total amount of all donations for a given donor."""


def calculte_avg_donation(donor_object):
    """ Calculates the average amount of donations from a given donor.

    Will round to the nearest cent."""


def generate_report():
    """ Generates a report that lists all donors by donation amount.

    Prints their name, total donations, average donations."""
