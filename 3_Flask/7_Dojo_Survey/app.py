# -*- python -*-

from flask import Flask, render_template, request

app = Flask( __name__ )

@app.route( '/' )
def index():
    return( render_template( "index.html" ) )

@app.route( '/submit', methods=['POST'] )
def results():
    print "Got /submit POST data"
    name = request.form['name']
    loc = request.form['loc']
    lang = request.form['lang']
    comments = request.form['comments']
    return( render_template( "results.html", name=name, loc=loc, lang=lang, comments=comments ) )

app.run( debug=True )
