from flask import Flask, render_template  # Import Flask to allow us to create our app
# Create a new instance of the Flask class called "app"
app = Flask(__name__)


# The "@" decorator associates this route with the function immediately following
@app.route('/')
def route():
    return render_template('index.html', x=3, color='blue')

@app.route('/play/<int:x>/<color>')
def play(x,color):
    return render_template('index.html', x=x,color=color)


if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
