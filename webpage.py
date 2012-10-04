# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 20:17:35 2012

Creates a simple website using the Flask module to implement a template
that wraps some strings with HTML markup. In-class example.

@author: robert
"""

from flask import Flask

site = Flask("MySite")
css = """
h1 {color: red}
"""
tpl = """
        <html>
            <head>
                <title>{title}</title>
            </head>
            <body>
                <h1>Robert's Site</h1>
                <br>
                <div id="conen">
                    <h2>{title}</h2>
                    <p>{body}</p>
                </div>
            </body>
        </html>
"""

def template(fn):
    def wrapped():
        return tpl.format(**fn())
    return wrapped # name of wrapped content, by convention

@site.route("/")
@template # decorator
def index():
    return {
        'title': 'My Website',
        'body': 'Hello World'
    }

site.run()




