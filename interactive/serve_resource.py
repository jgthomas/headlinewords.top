from flask import Blueprint, render_template
import plot_words
from graph import Graph, get_plot
from constants import SOURCE_BASE


serve = Blueprint("serve", __name__)


@app.route("/graph")
def graph():
    word = request.args.get("word_to_graph", "")
    source = request.args.get("check", "")

    graph = Graph(db = source,
                  filename = word,
                  days = "7",
                  words = [word],
                  colour = ["blue"],
                  period = "4")

    plot = get_plot(title=word,
                    filename=''.join([word, ".png"])
    source_details = SOURCE_BASE[source]
    return render_template("output.html",
                           publication=source_details,
                           plot=plot)
