1. Search 'flask minimal app' you will get a quickstart page for flask. We copied that cide as a starter.
    https://flask.palletsprojects.com/en/2.0.x/quickstart/

        from flask import Flask
        
        app = Flask(__name__)

        @app.route("/")
        def hello_world():
             return "<p>Hello, World!</p>"

2. This is only started code you have to add some code to run the app.

        if __name__ == "__main__":
            app.run(debug=True)

3. now to run the app:
        click play icon on top-right, or type: python .\app.py 
        
4. This will start running the server.

5. You will 'Running on link' you have to press ctrl+click on that link.

ProTip: You can change the host and port of server running.
If your port is taken by other application, you can change it like this:
you have port to exisitng code:
            app.run(debug=True, port=8000)

when you save the file, the running server will automatically reload.

For the warning which you are getting after running the server:
---------------------------------------------------------------
Warning: This is a developement server. Do not use it in a production deployment.

We need to use other server to deploy this.
More info: https://flask.palletsprojects.com/en/2.0.x/tutorial/deploy/

ON harry tutorial, he is using 'heroku'

------------------------------------
Understanding @app.route("/") --
------------------------------------

we have have mutiple endpoints, jaise hum hyperlinks se pages join karte hai. 
@app.route("/") -- yene / apka main page hoga
manlo apko /products page banana hai:

@app.route("/products")
def products():
    return "<p>This is my product page.</p>"

so ye dusra page ban jayega like
link:8000/products

after running you have to add /products in url that is running in browser to move to this page

Moving on,
---------------------
static and templates
---------------------
Create folder 'static' and 'templates' in same folder where you created app.py.
These are primary (i mean, standard folders)
Remember in same path where app.py is located.

Understanding static folder:
-----------------------------

Whatever file you will put here, it will be rendered as it is in your broswer.
Suppose, you will make file Mayur.txt in it and put some text in it:
Hello this is Mayur. Now you will save this.

Server will detect this automatically, if your server is running.

after that move to broswer where you have the page running.

add /static/Mayur.txt to link which is running. You will you text file rendered/ displayed as it is.

This is for Understanding sake dont add this text file Mayur.txt in production deployment.


Understanding templates folder: 
--------------------------------
templates folder is where your html files and others are kept to render them.

suppose you added index.html to template folder.

now you want to render it, (it has different method than we use for static)

you have to import 'render_template' from flask
and add code:
     'return render_template('index.html')'

you starter code will change like this, after you make above chnages:


        from flask import Flask, render_template
        
        app = Flask(__name__)

        @app.route("/")
        def hello_world():
             return render_template('index.html')
             # return "<p>Hello, World!</p>"


        if __name__ == "__main__":
            app.run(debug=True)


this how you embed html templates, and make the website beautiful. css, and js toh html mein linked rahenge.


after this we will now use bootstrap framework, in index.html
get the starter code from here:

https://getbootstrap.com/docs/5.0/getting-started/introduction/



