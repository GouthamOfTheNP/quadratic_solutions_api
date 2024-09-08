from flask import Flask, render_template
import math

app = Flask(__name__)


@app.route('/')
def home():
    try:
        return render_template("index.html")
    except Exception as e:
        print(f"Error occurred: {e}")
        return "An error occurred while processing your request.", 500


@app.route('/v1.1')
def changelog():
    try:
        return render_template("changelog.html")
    except Exception as e:
        print(f"Error occurred: {e}")
        return "An error occurred while processing your request.", 500


@app.route('/v1.1/<a>_<b>_<c>')
def solutions(a, b, c):
    try:
        try:
            a = float(a)
            b = float(b)
            c = float(c)
        except ValueError:
            positive = "Cannot calculate due to non-integer types"
            negative = "Cannot calculate due to non-integer types"
        else:
            try:
                positive = (-b+math.sqrt((b**2)-(4*a*c)))
                negative = (-b-math.sqrt((b**2)-(4*a*c)))
            except ValueError:
                positive = "Not real solution"
                negative = "Not real solution"
        return render_template("solutions.html", entered_data=[a, b, c], positive=positive, negative=negative)
    except Exception as e:
        print(f"Error occurred: {e}")
        return "An error occurred while processing your request.", 500

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run()
