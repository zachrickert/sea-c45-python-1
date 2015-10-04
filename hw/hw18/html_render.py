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
        self.pre = ''
        self.post = ''

    def append(self, child):
        self.contents.append(child)

    def render(self, f, ind=''):
        if(self.tag == 'html'):
            f.write(self.pre)
        if(self.tag == ''):
            f.write('\n')

        tab = '    ' + ind
        opening = ind + "<{tag}>\n".format(tag=self.tag)
        closing = ind + "</{tag}>{post}".format(tag=self.tag, post=self.post)
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
        self.pre = '<!DOCTYPE html>\n'


class Head(Element):
    def __init__(self):
        Element.__init__(self, "head")
        self.post = '\n'


class Body(Element):
    def __init__(self):
        Element.__init__(self, "body")
        self.post = '\n'


class P(Element):
    def __init__(self, line=""):
        Element.__init__(self, "p")
        self.line = line
        self.append(line)
        self.post = '\n'


class Title(Element):
    def __init__(self, line=""):
        Element.__init__(self, "title")
        self.line = line
        self.append(line)
        self.post = '\n'

    def render(self, f, ind=''):
        tline = "{t}<{tag}>{line}</{tag}>{end}"
        tline = tline.format(t=ind, tag=self.tag, line=self.line,
                             end=self.post)
        f.write(tline)
