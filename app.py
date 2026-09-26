from flask import Flask

app = Flask(_name_)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>My PaaS Application</title>
    </head>
    <body>
        <h1>Hello from Render!</h1>
        <h2>My First PaaS Web Application</h2>
        <p>Created using Python and Flask.</p>
    </body>
    </html>
    """

if _name_ == "_main_":
    app.run()
