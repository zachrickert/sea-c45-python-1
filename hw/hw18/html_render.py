#!/usr/bin/env python

"""
Python class example.

"""

# The start of it all:
# Fill it all in here.
TEXT1 = '''Here is a paragraph of text -- there could be more of them, but this is enough to
show that we can do some text'''

TEXT2 = '''And here is another piece of text -- you should be able to add any number'''


class Element(object):
    def __init__(self, tag=""):
        self.tag = tag
        self.contents = []

    def append(self, child):
        child = child.split('\n')
        for items in child:
            self.contents.append(items)

    def print_to_terminal(self, ind_level):
        tab = '    ' * ind_level
        opening = "<{tag}>".format(tag=self.tag)
        closing = "</{tag}>".format(tag=self.tag)
        print(opening)
        for child in self.contents:
            child = tab + child
            print (child)
        print(closing)

    def render(self, f, ind=''):
        tab = '    ' + ind
        opening = "<{tag}>\n".format(tag=self.tag)
        closing = "</{tag}>\n".format(tag=self.tag)
        f.write(opening)
        for child in self.contents:
            child = tab + child + '\n'
            f.write(child)
        f.write(closing)


def main():
    output_file = 'test_html_output1.html'
    f = open(output_file, 'w')
    my_web = Element()
    my_web.append(TEXT1)
    my_web.append(TEXT2)

    my_web.render(f, "")
