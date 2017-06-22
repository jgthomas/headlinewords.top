import os.path
from flask import Blueprint, render_template, request, redirect, url_for
import plot_words
from graph import Graph, get_plot
from constants import SOURCE_BASE, PLOT_PATH
from query_functions import TODAY


serve = Blueprint("serve", __name__)


@serve.route("/graph", methods=["GET"])
def graph():
    word = request.args.get("word_to_graph", "").lower()
    source = request.args.get("check", "")
    colour = request.args.get("colour", "")
    if not word:
        return redirect(url_for("home", _anchor="graph-maker"))

    date = TODAY.strftime("_%d_%B_%Y")
    filename = ''.join([word, '_', source, date])
    full_filename = ''.join([filename, ".png"])

    if not os.path.isfile(''.join([PLOT_PATH, full_filename])):
        graph = Graph(db = source,
                  filename = filename,
                  days = "7",
                  words = [word],
                  colour = [colour],
                  period = "4")
        plot_words.main(graph.args())

    source_details = SOURCE_BASE[source]

    plot = get_plot(title=word,
                    filename=full_filename,
                    source=source_details["title"])
    return render_template("output.html",
                           plot=plot)
