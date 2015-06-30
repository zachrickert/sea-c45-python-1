from subprocess import Popen, PIPE, STDOUT, TimeoutExpired


def process(input):
    p = Popen(['python3', './mailroom.py'],
              stdout=PIPE,
              stdin=PIPE,
              stderr=STDOUT)

    try:
        mailroom_stdout = p.communicate(
            input=input, timeout=3)[0]
        output = mailroom_stdout.decode().lower()

        return output

    except TimeoutExpired:
        raise AssertionError("Quit unsuccessful")


def test_quit():
    output = process(b'quit')
    assert("send a (t)hank you" in output)
    assert("create a (r)eport" in output)


def test_thank_you_quit():
    output = process(b'T\nlist\nquit')
    # prompts for a name
    assert("enter a name" in output)


def test_name_quit():
    output = process(b'T\nbill gates\nquit')
    assert("donation amount" in output)


def test_name_donate():
    output = process(b'T\nbill gates\n200\nquit')

    # name and amount in thank you
    assert("bill gates" in output)
    assert("200" in output)

    # successfully returns to main menu
    assert("send a (t)hank you" in output)
    assert("create a (r)eport" in output)


def test_name_report():
    output = process(b'T\nbill gates\n200\nR\nquit')

    # new donor in report
    assert("bill gates" in output)
    assert("200" in output)
