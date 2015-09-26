import os


def clear_screen():
    os.system('clear')


def print_title():
    print('Welcome to Mailroom Madness')


def print_welcome():
    print_title()
    print ('Thank you for using the donor database.')
    print()
    print ('This program will allow you to: ')
    print ('\t * Input a new donor.')
    print ('\t * Input a donation from a donor.')
    print ('\t * Print a thank you letter to the donor.')
    print ('\t * Get a report on donations.')
    print ()
    print ('At any point in this program you can type:')
    help_menu()


def help_menu():
    print("M = Main menu \t x = eXit")
    print()


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
    print("Choose from the following:")
    print('T - Send a (T)hank You')
    print('R - Create a (R)eport')
    print('quit - Quit the Program')
    user_input = input('>')
    user_input = validate_initial_prompt(user_input)
    return user_input


def validate_initial_prompt(user_input):
    """ Reads input and changes user info to specified type

    If user input does not meet specifications
    then user is sent back to initial prompt"""

    user_input = user_input.lower()
    exit = ['exit', 'x', 'quit', 'ex', 'q', 'e']
    letter = ['t', 'thank', 'thank you', 'l', 'letter', 's', 'send']
    report = ['r', 'report', 'c', 'create']
    if (user_input in exit):
        return 'x'
    elif (user_input in letter):
        return 't'
    elif (user_input in report):
        return 'r'
    else:
        return initial_prompt()


def enter_name():
    """ Will prompt user to enter donor's name.

    Inputs would be:
    1) Full Name
    2) List
    2) Return to main menu.

    returns full name or command to list all donors.
    """

    clear_screen()
    print_title()
    print('Please enter a name or chose from the following:')
    print('list - Print a list of previous donors')
    print('quit - Return to main menu')
    name = input(">")
    name = validate_name(name)
    return name


def validate_name(input_name):
    temp_name = input_name.lower()

    exit = ['exit', 'x', 'ex', 'e']
    main = ['q', 'quit', 'm', 'main', 'menu']
    report = ['l', 'list', 'report']
    if (temp_name in exit):
        return 'x'
    elif(temp_name in main):
        return 'm'
    elif(temp_name in report):
        return 'l'
    else:
        return input_name


def is_current_donor(donor_name, all_donors):
    """Compares name to names of people who have given in the past.

    Returns True if the name is in the database.
    Returns False if the name is not in the database.

    """
    donor = False
    for names in all_donors:
        if(donor_name == names):
            donor = True

    return donor


def get_donor_number(donor_name, donors):
    """Compares name to names of people who have given in the past.

    Returns donor number if a donor record already exists.
    Creates a new number for new donors.

    """
    is_new = True

    for i in range(len(donors)):
        if(donor_name == donors[i].name):
            is_new = False
            break

    if (is_new):
        create_donor(donor_name, donors)
        return (len(donors) - 1)
    else:
        return i


def create_donor(donor_name, donors):
    """ Adds a new donor to the list of donors.

    Donor object created.
    Donation history set to empty."""
    new_donor = Donor(donor_name)
    donors.append(new_donor)


def list_donors(donors):
    """ Lists all donors.

    Will sort donors some logical way."""
    for i in range(len(donors)):
        print(donors[i].name, donors[i].donation_amount)


def input_donation():
    """ Asks user to input a donation amount.

    Returns donation amount in the form of a floating point amount."""

    print()
    print("Please enter donation amount or 'quit':")
    donation = input('>')
    donation = verify_donation(donation)
    return donation


def verify_donation(donation):
    """ Verifies that a correct donation amount has been entered.

    Returns true if it is a valid amount.

    Returns False if it is:
        - has alpha charicters.
        - is negative.
        - has more than 2 decimal places."""

    main = ['q', 'quit', 'm', 'main', 'menu']
    if (donation.lower() in main):
        return 'quit'

    elif (not(is_float(donation))):
        return input_donation()

    else:
        donation = float(donation)
        if (donation <= 0):
            return input_donation()

        elif (not(is_currency(donation))):
            return input_donation()
        else:
            return donation


def calculate_total_donation(donor_object):
    """ Calculates the total amount of all donations for a given donor."""


def calculte_avg_donation(donor_object):
    """ Calculates the average amount of donations from a given donor.

    Will round to the nearest cent."""


def generate_report():
    """ Generates a report that lists all donors by donation amount.

    Prints their name, total donations, average donations."""


def is_float(x):
    try:
        float(x)
        return True
    except ValueError:
        return False


def is_currency(x):
    if (((x * 1000) % 10) > 0):
        temp = False
    else:
        temp = True
    return temp


class Donor(object):
    def __init__(self, name):
        self.name = name
        self.donation_amount = []
        self.parse_name()

    def add_donation_amount(self, donation_amount):
        self.donation_amount.append(donation_amount)

    def parse_name(self):
        self.fname = self.name.split(' ')[0]

    def thank_you(self):
        """ Prints a nice thank you letter for the inputted donor.

        Will include a friendly personalized greeting
        to the donot by spicing the given name.

        """

        last_donation = self.donation_amount[len(self.donation_amount) - 1]
        last_donation = str('%0.2f' % last_donation)

        letter = """Dear {},
Thank you so much for your kind donation of ${}.
We here at the Ministry for Silly Walks greatly appreciate it.
Your money will go towards creating newer sillier walks.

Thanks again,
John CLeese
Director, CEO M.S.W.

""".format(self.fname, last_donation)

        print(letter)


def main():
    not_done = True
    is_first_time = False  # Originally had a more verbose intro.
    donors = []

    while not_done:
        clear_screen()
        if (is_first_time):
            print_welcome()
            is_first_time = False
        else:
            print_title()

        initial_input = initial_prompt()
        if(initial_input == 'x'):
            not_done = False
            continue
        elif(initial_input == 't'):
            donor_name = enter_name()
            if (donor_name == 'x'):
                not_done = False
                continue
            if (donor_name == 'm'):
                continue
            donation_amount = input_donation()
            if (donation_amount == 'quit'):
                continue

            don_numb = get_donor_number(donor_name, donors)

            donors[don_numb].add_donation_amount(donation_amount)

            donors[don_numb].thank_you()

            input()


main()
