
from flask import Flask

app=Flask(name)#creating the new flask object


@app.route("/")
def main():
    return "My First Flask Web Application"

@app.route("/demo")
def demo1():
    return "Demo Page"


@app.route("/admin")
def demo2():
    return "Admin Page"


@app.route("/user/<name>")
def demo3():
    return "Hello %s" %name#%s is parameter marker 


@app.route("/user")
def demo4():
    return "user Page"





if name=='main':
    app.run(debug=True)