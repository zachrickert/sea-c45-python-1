import os


def clear_screen():
    os.system('clear')


def print_title():
    print('Welcome to Mailroom Madness')


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
    # print_title()
    print('Please enter a name or chose from the following:')
    print('list - Print a list of previous donors')
    print('quit - Return to main menu')
    name = input(">")
    name = validate_name(name)
    return name


def validate_name(input_name):
    temp_name = input_name.lower()

    exit = ['exit', 'x', 'ex', 'e']
    main = ['q', 'quit', 'm', 'main', 'menu']  # quit returns to main menu.
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
        create_donor(donor_name, donors, len(donors) - 1)
        return (len(donors) - 1)
    else:
        return i


def create_donor(donor_name, donors, id_numb):
    """ Adds a new donor to the list of donors.

    Donor object created.
    Donation history set to empty."""
    new_donor = Donor(donor_name, id_numb)
    donors.append(new_donor)


def list_donors(donors):
    """ Lists all donors.
    by namesome logical way."""

    sort_donors(donors, 'name')
    report(donors)


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


def calculate_donations(donors):
    """Finds the total and average amount of all donations for all donors."""

    for i in range(len(donors)):
        donors[i].calc_total_and_avg()


def generate_report(donors):
    """ Generates a report that lists all donors by donation amount.

    Prints their name, total donations, average donations."""

    sort_donors(donors, 'total')
    report(donors)


def report(donors):
    print('Name \t\t| Total \t\t| # \t| Average ')
    print('_____________________________________________________________')
    for i in range(len(donors)):
        total = format_currency(donors[i].total)
        average = format_currency(donors[i].average)

        line = "{}\t|{}\t\t|{}\t|{}".format(donors[i].name, total,
                                            donors[i].numb_of_donations,
                                            average)
        print(line)


def is_float(x):
    try:
        float(x)
        return True
    except ValueError:
        return False


def is_currency(x):
    """Checks to see if there is only two decimal places."""
    if (((x * 1000) % 10) > 0):
        temp = False
    else:
        temp = True
    return temp


def format_currency(numb):
    return '$' + str('%0.2f' % numb)


def wait_for_input():
    exit = ['exit', 'x', 'ex', 'e', 'q', 'quit']
    print()
    x = input('Press Enter to Continue...')
    if (x in exit):
        return True
    else:
        return False


def sort_donors(donors, sort_by):
    if (sort_by == 'total'):
        donors.sort(key=lambda x: x.total, reverse=True)
    elif (sort_by == 'id_numb'):
        donors.sort(key=lambda x: x.donor_id_numb, reverse=False)
    else:  # default to name
        donors.sort(key=lambda x: x.name, reverse=False)


class Donor(object):
    def __init__(self, name, numb):
        self.name = name
        self.donor_id_numb = numb
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
        last_donation = format_currency(last_donation)

        letter = """Dear {},
Thank you so much for your kind donation of {}.
We here at the Ministry for Silly Walks greatly appreciate it.
Your money will go towards creating newer sillier walks.

Thanks again,
John Cleese
Director, CEO M.S.W.
""".format(self.name, last_donation)

        print(letter)

    def calc_total_and_avg(self):
        self.total = 0
        for i in range(len(self.donation_amount)):
            self.total = self.total + self.donation_amount[i]

        self.numb_of_donations = i + 1
        self.average = self.total / self.numb_of_donations


if __name__ == '__main__':
    done = False
    donors = []

    while (not done):
        clear_screen()
        print_title()

        initial_input = initial_prompt()
        if(initial_input == 'x'):
            done = True
            continue
        elif(initial_input == 't'):
            list_names = True

            # Will loop back to the name prompt if they ask to see the list
            while (list_names):
                donor_name = enter_name()
                if (donor_name == 'l'):
                    calculate_donations(donors)
                    list_donors(donors)
                    done = wait_for_input()
                else:
                    list_names = False
                    # Anything besides l will conmtinue

            if (donor_name == 'x'):
                done = True
                continue
            if (donor_name == 'm'):
                continue

            donation_amount = input_donation()
            if (donation_amount == 'quit'):
                continue

            don_numb = get_donor_number(donor_name, donors)

            donors[don_numb].add_donation_amount(donation_amount)
            donors[don_numb].thank_you()
            done = wait_for_input()

        elif(initial_input == 'r'):
            calculate_donations(donors)
            generate_report(donors)
            done = wait_for_input()
