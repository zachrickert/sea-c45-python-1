**************************
Session One: Introductions
**************************

| In which you are introduced to this class, your instructors, your environment
| and your new best friend, Python.

.. image:: /_static/python.png
    :align: center
    :width: 38%

.. rst-class:: credit

`xkcd.com/353`_


.. _xkcd.com/353: http://xkcd.com/353

Introductions
=============

.. rst-class:: center large

Now let's back up and meet each other.

Your instructor
---------------

.. rst-class:: center large

| Paul Pham
| @paulpham on Slack
| (paul at codefellows dot com)

Seattleite for 8 years.
UW alum.
Taught at The Evergreen State College in Olympia.
I like startups and using technology to improve people's lives,
especially through education.

Your TAs
---------------

.. rst-class:: center large

| Grace Hatamyar
| @ghatamyar

| Crystal Stellwagen
| @liraeldianne


How This Fits into CodeFellows
----------------------------

Prerequisites

* Foundations I: Web Dev with HTML, CSS, Javascript
* Unix & Git for Everyone

This Class

* Foundations II: Python

Where to Go From Here

* Python 401 next year
(the new Development Accelerator)

Outline of this Class
---------------------

* Session 1: Dev Environment, Python Syntax
* Session 2: Functions, Modules, Booleans
* Session 3: Sequences, Iteration and String Formatting
* Session 4: Dictionaries, Sets, Exceptions, and Files
* Session 5: Arguments, Comprehensions, Lambdas and Functional Programming
* Session 6: Intro to Object Oriented Programming
* Session 7: Testing, More OO
* Session 8: Optional Topics (Generators, Iterators, Decorators, and Context Managers)

Based on a curriculum designed by

| Cris Ewing and Chris Barker
| (cris at crisewing dot com)

Puzzle Given
---------------

Every session, you'll be given a puzzle in the form of
a Python program to write.
By the end of class, you'll know everything you need to solve the puzzle.

Today's puzzle:

Write a Python program that prints "Hello, World!" if you call it with
no arguments, otherwise prints the correct translation of
"Hello, World!" in whatever language is given as the first argument
to the program.

[demo]

Class Meetings
-------------

* Twice a week for 4 weeks
* 8 total class sessions
* Mondays and Wednesdays, 7-9pm
* The "Easy"

Office Hours
-------------

* 6pm before class, in the Easy
* Instructor + all TAs will be here
* Also by appointment with any TA

Homework
-------------

* 2-4 homework tasks per class session.
* Overall, about 20 homework tasks.
* Worth 5-10 points each.

Rubric:

* 0 points not turned in
* 1 points crashes, major syntax errors.
* 2 points crashes, minor syntax errors.
* 3 points runs, major logical errors
* 4 points runs, with minor logical or style errors
* 5 points, compiles and runs perfectly with good style.

Grading Policy
-------------

In order to pass the class:

* Attend at least 6 out of 8 classes.
* Score 85% of the points in the class total.
* You can resubmit to get more points.
* Late homework will be accepted up to 1 week after the class has ended (July 15)

Intense, Fast-paced
---------------

* Homework is assigned every class, due by the next class.
* You can't afford to miss more than one or two classes.
* It's easy to fall behind on the homework.
* Like learning a foreign language by moving to another country for four weeks.

Who are you?
-------------

.. rst-class:: center large

  Time for Python classmate speed-dating.


Course Materials Online
=======================

Where to Find Your Stuff

GitHub
------

There are two repositories in GitHub you will want to bookmark:

Student Homework Repository:
  https://github.com/codefellows/sea-c45-python

  Fork this repository to your own github account and do homework there.

Course Materials Repository:
  https://github.com/ppham/codefellows_f2_python

  Contains lecture material sources, supplemental materials and homework
  assignments

  A rendered HTML copy of all these class materials may be found online at
  http://codefellows.github.io/sea-c45-python

Canvas
------

We will be using Canvas to track your homework submission.  Grades will be
entered here as well:

https://canvas.instructure.com/courses/961767


Elsewhere
---------

Class email list:
  Code Fellows provides an email list for us. We will use this list for
  announcements. Please make sure that you are receiving the messages sent to
  this list:

  sea-c45@codefellows.com

Class `Slack <https://codefellows.slack.com>`_ Channel:
  The student repository README contains a link to the class chatroom. You can
  sign into the `Codefellow Slack team <https://codefellows.slack.com>` website
  or you can download the desktop client for your OS.

  Once you're signed in, join the `#sea-c45-python` channel.

  This is the official communication medium for the class, and where announcements will be made.


Introduction to Python
==========================

.. rst-class:: center large

Python Programming

How I Learned Python, and Why I'm Glad I Did
----------------------------

All my friends were talking about it.

I had a new project to do, and complete freedom to choose the technology.

Python is now a standard tool for numerical and scientific computation.
(e.g. Machine Learning)

Current and future dream job:
Industrial Light & Magic is hiring Python coders, presumably to work on the
new Star Wars movies.

What is Python?
---------------

.. rst-class:: build

* Dynamic
* Object oriented
* Byte-compiled
* Interpreted


.. nextslide::

.. rst-class:: center large

But what does that mean?


Python Features
---------------

Features:

.. rst-class:: build

* Unlike C, C++, C\#, Java ... More like Ruby, Lisp, Perl, Javascript
  ...

* **Dynamic** -- no type declarations

  * Programs are shorter
  * Programs are more flexible
  * Less code means fewer bugs

* **Interpreted** -- no separate compile, build steps - programming process is
  simpler


What's a Dynamic language
-------------------------

**Dynamic typing**.

* Type checking and dispatch happen at run-time

.. code-block:: ipython

    In [1]: x = a + b

.. rst-class:: build

* What is ``a``?
* What is ``b``?
* What does it mean to add them?
* ``a`` and ``b`` can change at any time before this process

.. nextslide::

**Strong typing**.

.. code-block:: ipython

    In [1]: a = 5

    In [2]: type(a)
    Out[2]: int

    In [3]: b = '5'

    In [4]: type(b)
    Out[4]: str

.. rst-class:: build

* **everything** has a type.
* the *type* of a thing determines what it can do.

Duck Typing
-----------

.. rst-class:: center large

"If it looks like a duck, and quacks like a duck -- it's probably a duck"


.. nextslide::

.. rst-class:: center large

If an object behaves as expected at run-time, it's the right type.


Python Versions
---------------

Python 2.x

.. rst-class:: build

* "Classic" Python
* Evolved from original

Python 3.x ("py3k")

.. rst-class:: build

* Updated version
* Removed the "warts"
* Allowed to break code


.. nextslide::

This class uses Python 3.x (3.4 is the latest as of this writing)
but we will point out the minor differences with Python 2.7, which
you will see in the wild.

.. rst-class:: build

* Adoption of Python 3 is growing fast

  * A few key packages still not supported (https://python3wos.appspot.com/)
  * Most code in the wild is still 2.x

* You *can* learn to write Python that is forward compatible from 2.x to 3.x
* We will be teaching from that perspective.
* If you find yourself needing to work with Python 2 and 3, there are ways to
  write compatible code:

  * https://wiki.python.org/moin/PortingPythonToPy3k
  * http://python3porting.com (particulary the chapters on modern idioms and
    supporting Python 2 and 3)
  * http://python-future.org/compatible_idioms.html

Other Reasons Why Python is Awesome
-----------------------------------

Keep your eye on the prize!

* Built-in data types like lists, dictionaries, tuples that access simply by typing the right grouping symbols! `[] {} ()`
* Its father, Guido van Rossum, still hearts it, actively guides its development,
and tweets about how awesome it is.
* It is named after Monty Python, but it also enables a lot of snake puns.
* Short, succinct metaphors and a can-do attitude
* Easy to experiment and play with. Open the interpreter, start messing around.

Your computer is your own laboratory or viewport into exploring a virtual world.

Introduction to Your Environment
================================

.. rst-class:: Left
.. container::

    There are three basic elements to your environment when working with Python:

    .. rst-class:: build

    * Your Command Line
    * Your Interpreter
    * Your Editor


Your Command Line (cli)
-----------------------

Having some facility on the command line is important

We won't cover this in class, so if you are not comfortable, please bone up at
home.

I suggest running through the **cli** tutorial at "learn code the hard way":

`http://cli.learncodethehardway.org/book`_

.. _http://cli.learncodethehardway.org/book: http://cli.learncodethehardway.org/book

You can also read the materials from the Code Fellows Unix & Git workshop:

`http://github.com/codefellows/sea-w29`_

.. _http://cewing.github.io/cf-uge: http://cewing.github.io/cf-uge


.. nextslide:: Command Line Enhancements

There are a few things you can do to help make your command line a better place
to work.

Part of your homework this week will be to do these things.

More on this later.


Your Interpreter
----------------

Python comes with a built-in interpreter.

You see it when you type ``python`` at the command line:

.. code-block:: pycon

    $ python3
    Python 3.4.3 (default, Jun  1 2015, 09:58:35)
    [GCC 4.2.1 Compatible Apple LLVM 5.0 (clang-500.0.68)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

That last thing you see, ``>>>`` is the "Python prompt".

This is where you type code.


.. nextslide:: Python in the Interpreter

Try it out:

.. code-block:: pycon

    >>> print(u"hello world!")
    hello world!
    >>> 4 + 5
    9
    >>> 2 ** 8 - 1
    255
    >>> print(u"one string" + u" plus another")
    one string plus another
    >>>


.. nextslide:: Tools in the Interpreter

When you are in an interpreter, there are a number of tools available to you.

There is a help system:

.. code-block:: pycon

    >>> help(str)
    Help on class str in module __builtin__:

    class str(basestring)
     |  str(object='') -> string
     |
     |  Return a nice string representation of the object.
     |  If the argument is a string, the return value is the same object.
     ...

You can type ``q`` to exit the help viewer.

.. nextslide:: Tools in the Interpreter

You can also use the ``dir`` builtin to find out about the attributes of a
given object:

.. code-block:: pycon

    >>> bob = u"this is a string"
    >>> dir(bob)
    ['__add__', '__class__', '__contains__', '__delattr__',
     '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
     '__getitem__', '__getnewargs__', '__getslice__', '__gt__',
     ...
     'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines',
     'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper',
     'zfill']
    >>> help(bob.rpartition)

This allows you quite a bit of latitude in exploring what Python is.


.. nextslide:: Advanced Interpreters

In addition to the built-in interpreter, there are several more advanced
interpreters available to you.

We'll be using one in this course called ``iPython``

More on this soon.


Your Editor
-----------

Typing code in an interpreter is great for exploring.

But for anything "real", you'll want to save the work you are doing in a more permanent
fashion.

This is where an Editor fits in.

.. nextslide:: Text Editors Only

Any good text editor will do.

.. rst-class:: build
.. container::

    MS Word is **not** a text editor.

    Nor is *TextEdit* on a Mac.

    ``Notepad`` is a text editor -- but a crappy one.

    You need a real "programmers text editor"

    A text editor saves only what it shows you, with no special formatting
    characters hidden behind the scenes.

.. nextslide:: Minimum Requirements


At a minimum, your editor should have:

.. rst-class:: build

* Syntax Colorization
* Automatic Indentation

In addition, great features to add include:

.. rst-class:: build

* Tab completion
* Code linting
* Jump-to-definition
* Interactive follow-along for debugging

.. rst-class:: build
.. container::

    Have an editor that does all this? Feel free to use it.

    If not, I suggest ``Sublime Text`` (2 or 3):

    http://www.sublimetext.com/


Setting Up Your Environment
===========================

.. rst-class:: centered large

Shared setup means reduced complications.


Our Class Environment
---------------------

We are going to work from a common environment in this class.

We will take the time here in class to get this going.

This helps to ensure that you will be able to work.


Step 1: Python 3.4
------------------

.. rst-class:: large

You have this already, right?

.. code-block:: bash

    $ python
    Python 3.4.3 (default, Jun  1 2015, 09:58:35)
    [GCC 4.2.1 Compatible Apple LLVM 5.0 (clang-500.0.68)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> ^D
    $

If not:

* `For the mac  <./supplements/python_for_mac.html>`_
* `For linux  <./supplements/python_for_linux.html>`_
* `For windows  <./supplements/python_for_windows.html>`_

Step 2: Pip
-----------

Python comes with quite a bit ("batteries included").

Sometimes you need a bit more.

Pip allows you to install Python packages to expand your system.

pip comes preinstalled with Python 3.4.

You can check to see if you have it installed by typing:

.. code-block:: bash

    $ pip --version
    pip 7.0.3 from /usr/local/lib/python3.4/site-packages (python 3.4)

(or go to: http://pip.readthedocs.org/en/latest/installing.html)

.. nextslide:: Using Pip

Once you've installed pip, you use it to install Python packages by name:

.. code-block:: bash

    $ pip install foobar
    ...

To find packages (and their proper names), you can search the python package
index (PyPI):

https://pypi.python.org/pypi



Step 3: Optional -- Virtualenv
-------------------------------

Python packages come in many versions.

Often you need one version for one project, and a different one for another.

`Virtualenv`_ allows you to create isolated environments.

You can then install potentially conflicting software safely.

For this class, this is no big deal, but as you start to work on "real"
projects, it can be a key tool.

.. _Virtualenv: http://www.virtualenv.org/

If you want to install it, here are some notes:

`Intro to VirtualEnv <./supplements/virtualenv.html>`_


Step 4: Fork Class Repository
------------------------------

`GitHub <www.github.com>`_ is an industry-standard system for collaboration on
software projects -- particularly open source ones.

We will use it this class to manage submitting and reviewing your work, etc.

**Wait!** Don't have a gitHub account? Set one up now.

Next, you'll make a copy of the class repository using ``git``.

The canonical copy is in the CodeFellows organization on GitHub:

https://github.com/codefellows/sea-c45-python

Open that URL, and click on the *Fork* button at the top right corner.

This will make a copy of this repository in *your* github account.

.. nextslide:: Clone Your Fork

From here, you'll want to make a clone of your copy on your local machine.

At your command line, run the following commands:

.. code-block:: bash

    $ cd your_working_directory_for_the_class
    $ git clone https://github.com/<yourname>/sea-c45-python.git

(you can copy and paste that link from the gitHub page)

If you have an SSH key set up for gitHub, you'll want to do this instead:

.. code-block:: bash

    git@github.com:<yourname>/sea-c45-python.git

**Remember**, <yourname> should be replaced by your github account name.

Brief Aside
-----------

Remember our puzzle?
Let's go into our recently cloned class repo and see some starter code.

.. code-block:: bash

    cd examples/session01
    python hello.py

Now back to show!

Step 5: Install Requirements
----------------------------

As this is an intro class, we are going to use almost entirely features of standand library. But there are a couple things you may want:

**iPython**

.. code-block:: bash

  $pip install ipython

If you are using SublimeText, you may want:

.. code-block:: bash

  $ pip install PdbSublimeTextSupport

Introduction to iPython
=======================

iPython Overview
------------------

You have now installed `iPython`_.

iPython is an advanced Python interpreter that offers enhancements.

You can read more about it in the `official documentation`_.

Specifically, you'll want to pay attention to the information about

`Using iPython for Interactive Work`_.

.. _iPython: http://ipython.org
.. _official documentation: http://ipython.org/ipython-doc/stable/index.html
.. _Using iPython for Interactive Work: http://ipython.org/ipython-doc/stable/interactive/index.html

.. ifslides::

    Let's see a quick demo of what it can do for you.


The very basics of iPython
--------------------------

iPython can do a lot for you, but for starters, here are the key pieces you'll
want to know:

Start it up

.. code-block:: bash

    $ipython

    $ ipython
    Python 2.7.6 (v2.7.6:3a1db0d2747e, Nov 10 2013, 00:42:54)
    Type "copyright", "credits" or "license" for more information.

    IPython 2.0.0 -- An enhanced Interactive Python.
    ?         -> Introduction and overview of IPython's features.
    %quickref -> Quick reference.
    help      -> Python's own help system.
    object?   -> Details about 'object', use 'object??' for extra details.


.. ifslides::

    (live demo)


.. nextslide:: iPython basics

This is the stuff I use every day:

* command line recall:

  - hit the "up arrow" key
  - if you have typed a bit, it will find the last command that starts the same way.

* basic shell commands:

  - ``ls``, ``cd``, ``pwd``

* any shell command:

  - ``! the_shell_command``

* pasting from the clipboard:

  - ``%paste`` (this keeps whitespace cleaner for you)


.. nextslide:: iPython basics (cont)

* getting help:

  - ``something?``

* tab completion:

  - ``something.<tab>``

* running a python file:

  - ``run the_name_of_the_file.py``


That's it -- you can get a lot done with those.

How to run a python file
--------------------------

A file with python code in it is a 'module' or 'script'

(more on the distiction later on...)

It should be named with the ``.py`` extension: ``some_name.py``

To run it, you have a couple options:

1) call python on the command line, and pass in your module name

.. code-block:: bash

  $ python the_name_of_the_script.py

2) run ``iPython``, and run it from within iPython with the ``run`` command

.. code-block:: ipython

  In [1]: run the_file.py

.. ifslides::

    .. rst-class:: centered

        [demo]



Basic Python Syntax
===================

.. rst-class:: center mlarge

| Expressions, Statements,
| Values, Types, and Symbols


Code structure
--------------

Each line is a piece of code.

Comments:

.. code-block:: ipython

    In [3]: # everything after a '#' is a comment

Expressions:

.. code-block:: ipython

    In [4]: # evaluating an expression results in a value

    In [5]: 3 + 4
    Out[5]: 7

.. nextslide::

Statements:

.. code-block:: ipython

    In [6]: # statements do not return a value, may contain an expression

    In [7]: print(u"this")
    this

    In [8]: line_count = 42

    In [9]:


Printing
--------

In Python 2.x, printing is a statement. In Python 3, it was changed to a
function.

.. rst-class:: build
.. container::

    You can get the Python 3 behavior in Python 2.6+ using the ``__future__``
    module.

    .. code-block:: python

        from __future__ import print_function

    For purposes of writing cross-compatible code, this is a good idea.  Please
    use this idiom in your code.

.. nextslide::

It's kind of obvious, but handy when playing with code:

.. code-block:: ipython

    In [1]: from __future__ import print_function
    In [2]: print(u"something")
    something

You can print multiple things:

.. code-block:: ipython

    In [3]: print(u"the value is", 5)
    the value is 5


.. nextslide::

Python automatically adds a newline, which you can change with ``end`` argument:


.. code-block:: ipython

    In [12]: for i in range(5):
       ....:     print(u"the value is", end=' ')
       ....:     print(i)
       ....:
    the value is 0
    the value is 1
    the value is 2
    the value is 3
    the value is 4


.. nextslide::

Any python object can be printed (though it might not be pretty...)

.. code-block:: ipython

    In [1]: class Bar(object):
       ...:     pass
       ...:

    In [2]: print(Bar)
    <class '__main__.Bar'>


.. nextslide:: Code Blocks

Blocks of code are delimited by a colon and indentation:

.. code-block:: python

    def a_function():
        a_new_code_block
    end_of_the_block

.. code-block:: python

    for i in range(100):
        print(i**2)

.. code-block:: python

    try:
        do_something_bad()
    except:
        fix_the_problem()

Whitespace
--------

Python uses whitespace to delineate structure.

This means that in Python, whitespace is **significant**.

(but **ONLY** for newlines and indentation)

The standard is to indent with **4 spaces**.

**SPACES ARE NOT TABS**

**TABS ARE NOT SPACES**


.. nextslide::

These two blocks look the same:

.. code-block:: python

    for i in range(100):
        print(i**2)

.. code-block:: python

    for i in range(100):
        print(i**2)


.. nextslide::

But they are not:

.. code-block:: python

    for i in range(100):
    \s\s\s\sprint(i**2)

.. code-block:: python

    for i in range(100):
    \tprint(i**2)

**ALWAYS INDENT WITH 4 SPACES**


.. nextslide::

.. rst-class:: center large

NEVER INDENT WITH TABS

make sure your editor is set to use spaces only --

ideally even when you hit the <tab> key

Values
------

.. rst-class:: build

* Values are pieces of unnamed data: ``42, u'Hello, world',``
* In Python, all values are objects

  * Try ``dir(42)``  - lots going on behind the curtain!

* Every value belongs to a type

  * Try ``type(42)`` - the type of a value determines what it can do

.. ifslides::

    .. rst-class:: centered

        [demo]

Literals for the Basic Value types:
------------------------------------

.. rst-class:: build

Numbers:
  - floating point: ``3.4``
  - integers: ``456``

Text:
  -  ``u"a bit of text"``
  -  ``u'a bit of text'``
  - (either single or double quotes work -- why?)

Boolean values:
  -  ``True``
  -  ``False``

(There are intricacies to all of these that we'll get into later)


Values in Action
----------------

An expression is made up of values and operators

.. rst-class:: build

* An expression is evaluated to produce a new value:  ``2 + 2``

  *  The Python interpreter can be used as a calculator to evaluate expressions

* Integer vs. float arithmetic

  * `1 / 2` versus `1. / 2`
  * (Python 3 smooths this out)
  * Always use ``/`` when you want float results, ``//`` when you want floored (integer) results

* Type conversions

  * This is the source of many errors, especially in handling text
  * Python 3 will not implicitly convert bytes to unicode

* Type errors - checked at run time only

.. ifslides::

    .. rst-class:: centered

        [demo]


Symbols
-------

Symbols are how we give names to values (objects).

.. rst-class:: build

* Symbols must begin with an underscore or letter
* Symbols can contain any number of underscores, letters and numbers

  * this_is_a_symbol
  * this_is_2
  * _AsIsThis
  * 1butThisIsNot
  * nor-is-this

* Symbols don't have a type; values do

  * This is why python is 'Dynamic'


Symbols and Type
----------------

Evaluating the type of a *symbol* will return the type of the *value* to which
it is bound.

.. code-block:: ipython

    In [19]: type(42)
    Out[19]: int

    In [20]: type(3.14)
    Out[20]: float

    In [21]: a = 42

    In [22]: b = 3.14

    In [23]: type(a)
    Out[23]: int

    In [25]: a = b

    In [26]: type(a)
    Out[26]: float


Assignment
----------

A *symbol* is **bound** to a *value* with the assignment operator: ``=``

.. rst-class:: build

* This attaches a name to a value
* A value can have many names (or none!)
* Assignment is a statement, it returns no value


.. nextslide::

Evaluating the name will return the value to which it is bound

.. code-block:: ipython

    In [26]: name = u"value"

    In [27]: name
    Out[27]: u'value'

    In [28]: an_integer = 42

    In [29]: an_integer
    Out[29]: 42

    In [30]: a_float = 3.14

    In [31]: a_float
    Out[31]: 3.14


In-Place Assignment
-------------------

You can also do "in-place" assignment with ``+=``.

.. code-block:: ipython

    In [32]: a = 1

    In [33]: a
    Out[33]: 1

    In [34]: a = a + 1

    In [35]: a
    Out[35]: 2

    In [36]: a += 1

    In [37]: a
    Out[37]: 3

also: ``-=, *=, /=, **=, %=``

(not quite -- really in-place assignment for mutables....)


Multiple Assignment
-------------------

You can assign multiple variables from multiple expressions in one statement

.. code-block:: ipython

    In [48]: x = 2

    In [49]: y = 5

    In [50]: i, j = 2 * x, 3 ** y

    In [51]: i
    Out[51]: 4

    In [52]: j
    Out[52]: 243


Python evaluates all the expressions on the right before doing any assignments


Nifty Python Trick
------------------

Using this feature, we can swap values between two symbols in one statement:

.. code-block:: ipython

    In [51]: i
    Out[51]: 4

    In [52]: j
    Out[52]: 243

    In [53]: i, j = j, i

    In [54]: i
    Out[54]: 243

    In [55]: j
    Out[55]: 4

Multiple assignment and symbol swapping can be very useful in certain contexts


Equality
--------

You can test for the equality of certain values with the ``==`` operator

.. code-block:: ipython

    In [77]: val1 = 20 + 30

    In [78]: val2 = 5 * 10

    In [79]: val1 == val2
    Out[79]: True

    In [80]: val3 = u'50'

    In [81]: val1 == val3
    Out[84]: False

.. ifslides::

    .. rst-class:: centered

        [demo]


Operator Precedence
-------------------

Operator Precedence determines what evaluates first:

.. code-block:: python

    4 + 3 * 5 != (4 + 3) * 5

To force statements to be evaluated out of order, use parentheses.


Python Operator Precedence
--------------------------

Parentheses and Literals:
  ``(), [], {}``

  ``"", b'', u''``

Function Calls:
  ``f(args)``

Slicing and Subscription:
  ``a[x:y]``

  ``b[0], c['key']``

Attribute Reference:
  ``obj.attribute``

.. nextslide::

Exponentiation:
  ``**``

Bitwise NOT, Unary Signing:
  ``~x``

  ``+x, -x``

Multiplication, Division, Modulus:
  ``*, /, %``

Addition, Subtraction:
  ``+, -``

.. nextslide::

Bitwise operations:
  ``<<, >>,``

  ``&, ^, |``

Comparisons:
  ``<, <=, >, >=, !=, ==``

Membership and Identity:
  ``in, not in, is, is not``

Boolean operations:
  ``or, and, not``

Anonymous Functions:
  ``lambda``


String Literals
---------------

You define a ``string`` value by writing a *literal*:

.. code-block:: ipython

    In [1]: u'a string'
    Out[1]: u'a string'

    In [2]: u"also a string"
    Out[2]: u'also a string'

    In [3]: u"a string with an apostrophe: isn't it cool?"
    Out[3]: u"a string with an apostrophe: isn't it cool?"

    In [4]: u'a string with an embedded "quote"'
    Out[4]: u'a string with an embedded "quote"'

(what's the '``u``' about?)


Keywords
--------

Python defines a number of **keywords**

These are language constructs.

You *cannot* use these words as symbols.

::

    and       del       from      not       while
    as        elif      global    or        with
    assert    else      if        pass      yield
    break     except    import    print
    class     exec      in        raise
    continue  finally   is        return
    def       for       lambda    try

.. nextslide::

If you try to use any of the keywords as symbols, you will cause a
``SyntaxError``:

.. code-block:: ipython

    In [13]: del = u"this will raise an error"
      File "<ipython-input-13-c816927c2fb8>", line 1
        del = u"this will raise an error"
            ^
    SyntaxError: invalid syntax

.. code-block:: ipython

    In [14]: def a_function(else=u'something'):
       ....:     print(else)
       ....:
      File "<ipython-input-14-1dbbea504a9e>", line 1
        def a_function(else=u'something'):
                          ^
    SyntaxError: invalid syntax


__builtins__
------------

Python also has a number of pre-bound symbols, called **builtins**

Try this:

.. code-block:: ipython

    In [6]: dir(__builtins__)
    Out[6]:
    ['ArithmeticError',
     'AssertionError',
     'AttributeError',
     'BaseException',
     'BufferError',
     ...
     'unicode',
     'vars',
     'xrange',
     'zip']

.. nextslide::

You are free to rebind these symbols:

.. code-block:: ipython

    In [15]: type(u'a new and exciting string')
    Out[15]: unicode

    In [16]: type = u'a slightly different string'

    In [17]: type(u'type is no longer what it was')
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    <ipython-input-17-907616e55e2a> in <module>()
    ----> 1 type(u'type is no longer what it was')

    TypeError: 'unicode' object is not callable

In general, this is a **BAD IDEA**.


Exceptions
----------

Notice that the first batch of ``__builtins__`` are all *Exceptions*

Exceptions are how Python tells you that something has gone wrong.

There are several exceptions that you are likely to see a lot of:

.. rst-class:: build

* ``NameError``: indicates that you have tried to use a symbol that is not bound to
  a value.
* ``TypeError``: indicates that you have tried to use the wrong kind of object for
  an operation.
* ``SyntaxError``: indicates that you have mis-typed something.
* ``AttributeError``: indicates that you have tried to access an attribute or
  method that an object does not have (this often means you have a different
  type of object than you expect)

The ``if`` Statement
---------------------

In order to do anything interesting at all (including this week's homework), you need to be able to make a decision.

.. nextslide::

.. code-block:: python

    In [12]: def test(a):
       ....:     if a == 5:
       ....:         print(u"that's the value I'm looking for!")
       ....:     elif a == 7:
       ....:         print(u"that's an OK number")
       ....:     else:
       ....:         print(u"that number won't do!")

    In [13]: test(5)
    that's the value I'm looking for!

    In [14]: test(7)
    that's an OK number

    In [15]: test(14)
    that number won't do!

There is more to it than that, but this will get you started.


Functions
---------

What is a function?

.. rst-class:: build

A function is a self-contained chunk of code


You use them when you need the same code to run multiple times,
or in multiple parts of the program.

(DRY)


Or just to keep the code clean


Functions can take and return information

.. nextslide::

Minimal Function does nothing

.. code-block:: python

    def <name>():
        <statement>

.. nextslide::

Pass Statement (Note the indentation!)

.. code-block:: python

    def minimal():
        pass


Functions: ``def``
------------------

``def``  is a *statement*:

.. rst-class:: build

  * it is executed
  * it creates a local variable


.. nextslide::

function defs must be executed before the functions can be called:

.. code-block:: ipython

    In [23]: unbound()
    ---------------------------------------------------------------------------
    NameError                                 Traceback (most recent call last)
    <ipython-input-23-3132459951e4> in <module>()
    ----> 1 unbound()

    NameError: name 'unbound' is not defined

.. code-block:: ipython

    In [18]: def simple():
       ....:     print(u"I am a simple function")
       ....:

    In [19]: simple()
    I am a simple function


Calling Functions
-----------------

You **call** a function using the function call operator (parens):

.. code-block:: ipython

    In [2]: type(simple)
    Out[2]: function
    In [3]: simple
    Out[3]: <function __main__.simple>
    In [4]: simple()
    I am a simple function


Functions: Call Stack
---------------------

functions call functions -- this makes an execution stack -- that's all a trace
back is

.. code-block:: ipython

    In [5]: def exceptional():
       ...:     print(u"I am exceptional!")
       ...:     print(1/0)
       ...:
    In [6]: def passive():
       ...:     pass
       ...:
    In [7]: def doer():
       ...:     passive()
       ...:     exceptional()
       ...:

You've defined three functions, one of which will *call* the other two.


Functions: Tracebacks
---------------------

.. code-block:: ipython

    In [8]: doer()
    I am exceptional!
    ---------------------------------------------------------------------------
    ZeroDivisionError                         Traceback (most recent call last)
    <ipython-input-8-685a01a77340> in <module>()
    ----> 1 doer()

    <ipython-input-7-aaadfbdd293e> in doer()
          1 def doer():
          2     passive()
    ----> 3     exceptional()
          4

    <ipython-input-5-d8100c70edef> in exceptional()
          1 def exceptional():
          2     print(u"I am exceptional!")
    ----> 3     print(1/0)
          4

    ZeroDivisionError: integer division or modulo by zero



Functions: ``return``
---------------------

Every function ends by returning a value

This is actually the simplest possible function:

.. code-block:: python

    def fun():
        return None

.. nextslide::

if you don't explicilty put ``return``  there, Python will:

.. code-block:: ipython

    In [9]: def fun():
       ...:     pass
       ...:
    In [10]: fun()
    In [11]: result = fun()
    In [12]: print(result)
    None

note that the interpreter eats ``None``


.. nextslide::

Only one return statement will ever be executed.

Ever.

Anything after a executed return statement will never get run.

This is useful when debugging!

.. code-block:: ipython

    In [14]: def no_error():
       ....:     return u'done'
       ....:     # no more will happen
       ....:     print(1/0)
       ....:
    In [15]: no_error()
    Out[15]: u'done'


.. nextslide::

However, functions *can* return multiple results:

.. code-block:: ipython

    In [16]: def fun():
       ....:     return (1, 2, 3)
       ....:
    In [17]: fun()
    Out[17]: (1, 2, 3)


.. nextslide::

Remember multiple assignment?

.. code-block:: ipython

    In [18]: x,y,z = fun()
    In [19]: x
    Out[19]: 1
    In [20]: y
    Out[20]: 2
    In [21]: z
    Out[21]: 3


Functions: parameters
---------------------

In a ``def`` statement, the values written *inside* the parens are
**parameters**

.. code-block:: ipython

    In [22]: def fun(x, y, z):
       ....:     q = x + y + z
       ....:     print(x, y, z, q)
       ....:

x, y, z are *local* symbols -- so is q


Functions: arguments
--------------------

When you call a function, you pass values to the function parameters as
**arguments**

.. code-block:: ipython

    In [23]: fun(3, 4, 5)
    3 4 5 12

The values you pass in are *bound* to the symbols inside the function and used.


Enough For Now
--------------

That's it for our basic intro to Python

Before next session, you'll use what you've learned here today to do some
exercises in Python programming

Unicode Notes
-------------

You might need this for the puzzle if you use foreign languages.

To put unicode in your source file, put:

.. code-block:: python

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-

at the top of your file ... and be sure to save it as utf-8!
(file->save with encoding in Sublime)

You also might want to put::

    from __future__ import unicode_literals

Additional notes on using Unicode in Python see:

    :ref:`unicode_supplement`


Puzzle Solved
========

Now it's time to solve our puzzle. Remember it?

Write a Python program that prints "Hello, World!" if you call it with
no arguments, otherwise prints the correct translation of
"Hello, World!" in whatever language is given as the first argument
to the program.

Partner up and let's get to work!

Homework
========

.. rst-class:: center large

    Three Tasks due by Wednesday, check them out on Canvas.

Homework Task 1: Python Pre-work

Homework Task 2: Style Checking

Homework Task 3: Gitting To Know You

Homework Task 4: Break These Functions
