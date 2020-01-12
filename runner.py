
from flask import Flask
from flask import render_template
from app import app, db, routes
from app.models import User, Post



@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}

if __name__ == '__main__':
    app.run()

