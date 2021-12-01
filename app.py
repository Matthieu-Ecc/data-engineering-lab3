from flask import Flask, render_template, request
import numpy

app = Flask(__name__)


@app.route("/mean_get", methods=["GET"])
def mean_get():
        mean_terms = request.args.get("q")
        if(mean_terms is None):
            return "no list were given"
        list_split = mean_terms.split(",")
        clean_list = filter(lambda x: x.isdigit(), list_split)
        numbers = list(map(int,clean_list))
        total = numpy.mean(numbers)
        return "{}".format(total)

@app.route('/')
def hello():
    return "hello to my sample flask app, if you want to test the app please enter http://localhost:5000/mean_get?q=[1,2,3] in the url"

if __name__ == '__main__':
	app.run(debug=True)