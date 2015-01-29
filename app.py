#!/usr/bin/python
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask( __name__ )

@app.route( "/" )
def main():
    return render_template( "page.html" )


if __name__ == "__main__":
    app.run()
