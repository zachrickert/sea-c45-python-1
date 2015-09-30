import os


TITLE = '''
Welcome to Mailroom Madness
'''

MAIN_MENU = '''
Choose from the following:
T - Send a (T)hank You
R - Create a (R)eport
quit - Quit the Program
'''

THANKYOU_MENU = '''
Please enter a name or chose from the following:
list - Print a list of previous donors
quit - Return to main menu
'''

REPORT_HEADER = '''
Report Manager
'''

LIST_HEADER = '''
List Manager
'''

DONATION_AMOUNT = '''
Please enter donation amount or 'quit':
'''

WAIT_TEXT = '''
Press Enter to Continue...
'''

DEFAULT_LETTER = '''
Dear {name},
Thank you so much for your kind donation of {amount}.
We here at the Ministry for Silly Walks greatly appreciate it.
Your money will go towards creating newer sillier walks.

Thanks again,
John Cleese
Director, CEO M.S.W.
'''


def clear_screen():
    os.system('clear')


def prompt(menu):
    if (menu != 'quit'):
        if (menu != 'wait'):
            clear_screen()
            print(TITLE)
        print(menus[menu])
        if (menu == 'list' or menu == 'report'):
            reply = None
        else:
            reply = input('>')
        validate = validator[menu]
        reply = validate(reply)
        return reply


def main_validator(user_input):
    """ Reads input and changes user info to specified type

    If user input does not meet specifications
    then user is sent back to initial prompt"""

    user_input = user_input.lower()
    quit = ['exit', 'x', 'quit', 'ex', 'q', 'e']
    letter = ['t', 'thank', 'thank you', 'l', 'letter', 'send']
    report = ['r', 'report', 'c', 'create']

    if (user_input in quit):
        return 'quit'
    elif (user_input in letter):
        return 'thankyou'
    elif (user_input in report):
        return 'report'
    else:
        return prompt('main')


def name_validator(user_input):
    temp_name = user_input.lower()

    exit = ['exit', 'x', 'ex', 'e']
    main = ['q', 'quit', 'm', 'main', 'menu']  # quit returns to main menu.
    report = ['l', 'list', 'report']
    if (temp_name in exit):
        return 'x'
    elif(temp_name in main):
        return 'main'
    elif(temp_name in report):
        return 'list'
    else:
        create_donor(temp_name.title())
        return('donate')


def wait_validator(user_input):
    exit = ['exit', 'x', 'ex', 'e', 'quit', 'q']

    if user_input in exit:
        return 'quit'

    return 'main'


def report_validator(user_input):
    for i in range(len(donors)):
        donors[i].calc_total_and_avg()
    sort_donors('total')
    report()
    return 'wait'


def list_validator(user_input):
    sort_donors('name')
    report()
    return 'wait'


def report():
    line = "{:^30} | {:^10} | {:^3} | {:^10}"
    line = line.format('Name', 'Total', '#', 'Average')
    print(line)
    print('______________________________________________________________')
    for i in range(len(donors)):
        donors[i].calc_total_and_avg()
        total = format_currency(donors[i].total)
        average = format_currency(donors[i].average)

        line = "{:<30} | {:>10} | {:>3} | {:>10}"
        line = line.format(donors[i].name, total,
                           donors[i].numb_of_donations, average)
        print(line)


def donation_validator(user_input):
    """ Verifies that a correct donation amount has been entered.

    Returns true if it is a valid amount.

    Returns False if it is:
        - has alpha charicters.
        - is negative.
        - has more than 2 decimal places."""

    main = ['q', 'quit', 'm', 'main', 'menu']
    if (user_input.lower() in main):
        return 'main'

    elif (not(is_float(user_input))):
        return 'donate'

    else:
        donation = float(user_input)
        if (donation <= 0):
            return 'donate'

        elif (not(is_currency(donation))):
            return 'donate'
        else:
            donors[-1].add_donation_amount(donation)
            donors[-1].thank_you()
            return 'wait'


def create_donor(donor_name):
    """ Adds a new donor to the list of donors.

    Donor object created.
    Donation history set to empty."""
    new_donor = Donor(donor_name)
    donors.append(new_donor)


def import_donors():
    try:
        f = open('donor.txt', 'r')
        finish_import = True

    except IOError:
        print('donor.txt not found. No data importted.')
        finish_import = False

    if finish_import:
        don_numb = 0
        for line in f:
            values = line.split(",")
            create_donor(values[0])
            for i in range(1, len(values) - 1):
                donors[don_numb].add_donation_amount(float(values[i]))
            don_numb = don_numb + 1

        print('donor.txt found and importted')
        f.close()


def save_donors():
    f = open('donor.txt', 'w')
    for i in range(len(donors)):
        line = donors[i].name + ', '
        for donation in donors[i].donation_amount:
            line = line + str(donation) + ', '
        line.rstrip(' ')
        line.rstrip(',')
        line = line + '\n'
        f.write(line)
    f.close()


def sort_donors(sort_by):
    if (sort_by == 'total'):
        donors.sort(key=lambda x: x.total, reverse=True)
    elif (sort_by == 'id_numb'):
        donors.sort(key=lambda x: x.donor_id_numb, reverse=False)
    else:  # default to name
        donors.sort(key=lambda x: x.name, reverse=False)


class Donor(object):
    def __init__(self, name):
        self.name = name
        self.donation_amount = []

    def add_donation_amount(self, donation_amount):
        self.donation_amount.append(donation_amount)

    def thank_you(self):
        """ Prints a nice thank you letter for the inputted donor.

        Will include a friendly personalized greeting
        to the donot by spicing the given name.

        """

        try:
            f = open("letter_template.txt", 'r')
            letter = ""
            for line in f:
                if(not(line[0] == '#')):
                    letter = letter + line

            f.close()

        except IOError:
            letter = DEFAULT_LETTER

        last_donation = self.donation_amount[- 1]
        last_donation = format_currency(last_donation)

        print(letter.format(name=self.name, amount=last_donation))

    def calc_total_and_avg(self):
        self.total = sum(self.donation_amount)
        self.numb_of_donations = len(self.donation_amount)
        self.average = self.total / self.numb_of_donations


def format_currency(numb):
    return '$' + str('%0.2f' % numb)


menus = {'main': MAIN_MENU, 'thankyou': THANKYOU_MENU, 'report': REPORT_HEADER,
         'list': LIST_HEADER, 'donate': DONATION_AMOUNT, 'wait': WAIT_TEXT}
validator = {'main': main_validator, 'thankyou': name_validator,
             'report': report_validator, 'list': list_validator,
             'donate': donation_validator, 'wait': wait_validator}
donors = []


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


def repl():
    done = False

    current_menu = 'main'
    while not done:
        user_input = prompt(current_menu)
        if user_input == 'quit':
            done = True
            break

        current_menu = user_input


if __name__ == '__main__':
    import_donors()
    repl()
