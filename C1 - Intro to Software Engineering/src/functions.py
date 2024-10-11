from flask import Flask, render_template

def greet():
    message = "Server side data has to be refeshed"
    return render_template('index.html', message=message)