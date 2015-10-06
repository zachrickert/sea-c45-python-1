#!/usr/bin/env python

"""
Python class example.

"""

# The start of it all:
# Fill it all in here.


class Element(object):
    def __init__(self, tag="", **kwargs):
        self.tag = tag
        self.open_tag = tag
        self.close_tag = tag
        self.contents = []
        self.pre = ''
        self.style = ''
        self.in_line = False
        self.set_in_line_element()
        self.set_kwargs(kwargs)

    def append(self, child):
        self.contents.append(child)

    def render(self, f, ind=''):

        f.write(self.pre)
        if(self.tag == ''):
            f.write('\n')
        tab = '    ' + ind

        if (self.style != ''):
            style_text = ' style="{style}"'.format(style=self.style)
        else:
            style_text = self.style

        opening = ind + '<{open_tag}'
        opening = opening + style_text
        opening = opening + '>' + self.after_opening
        opening = opening.format(open_tag=self.open_tag)
        f.write(opening)

        if self.in_line:
            tab = ''
            ind = ''

        for child in self.contents:
            if (type(child) == str):
                f.write(tab + child + self.after_child)
            else:
                child.render(f, tab)

        closing = ind + "</{close_tag}>{after_closing}".format(close_tag=self.close_tag, after_closing=self.after_closing)
        f.write(closing)

    def set_kwargs(self, kwargs):
        for key in kwargs:
            setattr(self, key, kwargs[key])

    def set_in_line_element(self):
        if self.in_line:
            self.after_opening = ''
            self.after_child = ''
            self.after_closing = '\n'
        else:
            self.after_opening = '\n'
            self.after_child = '\n'
            self.after_closing = '\n'


class Html(Element):
    def __init__(self):
        super(Html, self).__init__(tag="html")
        self.pre = '<!DOCTYPE html>\n'
        self.after_closing = ''


class Head(Element):
    def __init__(self):
        super(Head, self).__init__(tag="head")


class Body(Element):
    def __init__(self):
        super(Body, self).__init__(tag="body")


class P(Element):
    def __init__(self, line="", **kwargs):
        super(P, self).__init__(tag="p")
        self.line = line
        self.append(line)
        super(P, self).set_kwargs(kwargs)


class Title(Element):
    def __init__(self, line=""):
        super(Title, self).__init__(tag="title")
        self.line = line
        self.append(line)

    def render(self, f, ind=''):
        tline = "{t}<{tag}>{line}</{tag}>{end}"
        tline = tline.format(t=ind, tag=self.tag, line=self.line,
                             end=self.after_closing)
        f.write(tline)


class A(Element):
    def __init__(self, link='', line=''):
        super(A, self).__init__(tag="a")
        self.link = link
        self.line = line
        self.append(line)
        self.open_tag = self.tag + ' href="' + link + '"'
        self.in_line = True
        super(A, self).set_in_line_element()


class SelfCloseElement(Element):
    def __init__(self, tag):
        super(SelfCloseElement, self).__init__()
        self.tag = tag

    def render(self, f, ind=''):
        closing = ind + "<{tag} />{after_closing}".format(tag=self.tag, after_closing=self.after_closing)
        f.write(closing)


class Hr(SelfCloseElement):
    def __init__(self):
        super(Hr, self).__init__(tag="hr")


class Br(SelfCloseElement):
    def __init__(self):
        super(Br, self).__init__(tag="br")
