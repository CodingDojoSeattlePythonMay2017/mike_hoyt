# -*- python -*-

from flask import Flask, render_template, redirect, request, session, flash
import re
from datetime import datetime

app = Flask( __name__ )

app.secret_key = "RegistrationFormSecretKey"

email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route( "/" )
def index():
    return( render_template( "index.html" ) )

def validate_passwd( passwd ):
    if len( passwd ) < 1:
        return( "field CANNOT be empty!" )
    elif len( passwd ) < 8:
        return( "MUST be AT LEAST 8 characters!" )
    elif not re.match( r'^.*[A-Z]+.*$', passwd ):
        return( "MUST contain AT LEAST 1 capital letter!" )
    elif not re.match( r'^.*\d+.*$', passwd ):
        return( "MUST contain AT LEAST 1 number!" )
    return( "" )

@app.route( "/validate", methods=['POST'] )
def validate():
    nr_errors = 0

    # validate email
    email = request.form['email']
    if len( email ) < 1:
        flash( "The 'Email' field CANNOT be empty!")
        nr_errors += 1
    elif not email_regex.match( email ):
        flash( "Incorrectly formed 'Email' value!")
        nr_errors += 1

    # validate f_name
    f_name = request.form['f_name']
    if len( f_name ) < 1:
        flash( "The 'First Name' field CANNOT be empty!")
        nr_errors += 1
    elif not f_name.isalpha():
        flash( "The 'First Name' field CANNOT contain numbers!")
        nr_errors += 1

    # validate l_name
    l_name = request.form['l_name']
    if len( l_name ) < 1:
        flash( "The 'Last Name' field CANNOT be empty!")
        nr_errors += 1
    elif not l_name.isalpha():
        flash( "The 'Last Name' field CANNOT contain numbers!")
        nr_errors += 1

    # validate b_date
    b_date = request.form['b_date']
    today_date = datetime.now().strftime( "%Y-%m-%d" )
    if not re.match( r'^\d{4}[-/]\d{2}[-/]\d{2}$', b_date ):
        flash( "The 'Date' field format MUST follow YYYY-MM-DD!" )
        nr_errors += 1
    elif b_date >= today_date:
        flash( "The 'Date' field MUST be in the PAST!" )
        nr_errors += 1

    # validate passwd_1
    passwd_1 = request.form['passwd_1']
    passwd_msg = validate_passwd( passwd_1 )
    if len( passwd_msg ) > 0:
        flash( "The 'Password' " + passwd_msg )
        nr_errors += 1

    # validate passwd_2 against passwd_1
    passwd_2 = request.form['passwd_2']
    if passwd_1 != passwd_2:
        flash( "The 'Password' and 'Confirm Password' MUST match!")
        nr_errors += 1

    if nr_errors:
        return( redirect( "/" ) )
    else:
        return( redirect( "/confirmation" ) )

@app.route( "/confirmation" )
def confirmation():
    return( render_template( "confirmation.html" ) )

app.run( debug=True )
