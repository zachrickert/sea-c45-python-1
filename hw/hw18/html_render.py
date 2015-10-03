#!/usr/bin/env python

"""
Python class example.

"""

# The start of it all:
# Fill it all in here.


class Element(object):
    def __init__(self, tag=""):
        self.tag = tag
        self.contents = []

    def append(self, child):
        # child = child.split('\n')
        # for items in child:
        #     self.contents.append(items)
        self.contents.append(child)

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
        if(self.tag == 'html'):
            f.write('<!DOCTYPE html>\n')

        tab = '    ' + ind
        opening = ind + "<{tag}>\n".format(tag=self.tag)
        closing = ind + "</{tag}>\n".format(tag=self.tag)
        f.write(opening)
        for child in self.contents:
            if (type(child) == str):
                f.write(tab + child + '\n')
            else:
                child.render(f, tab)

        f.write(closing)


class Html(Element):
    def __init__(self):
        Element.__init__(self, "html")


class Head(Element):
    def __init__(self):
        Element.__init__(self, "head")


class Body(Element):
    def __init__(self):
        Element.__init__(self, "body")


class P(Element):
    def __init__(self, line=""):
        Element.__init__(self, "p")
        self.line = line
        self.append(line)


class Title(Element):
    def __init__(self, line=""):
        Element.__init__(self, "title")
        self.line = line
        self.append(line)

    def render(self, f, ind=''):
        tline = "{t}<{tag}>{line}</{tag}>\n"
        tline = tline.format(t=ind, tag=self.tag, line=self.line)
        f.write(tline)
