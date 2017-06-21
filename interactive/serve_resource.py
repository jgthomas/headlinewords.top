import os.path
from flask import Blueprint, render_template, request
import plot_words
from graph import Graph, get_plot
from constants import SOURCE_BASE, PLOT_PATH
from query_functions import TODAY


serve = Blueprint("serve", __name__)


@serve.route("/graph", methods=['GET'])
def graph():
    word = request.args.get("word_to_graph", "").lower()
    source = request.args.get("check", "")
    date = TODAY.strftime("_%d_%B_%Y")
    filename = ''.join([word, '_', source, date, '.png'])

    if not os.path.isfile(''.join(["./", PLOT_PATH, filename])):
        graph = Graph(db = source,
                  filename = ''.join([word, '_', source, date]),
                  days = "7",
                  words = [word],
                  colour = ["blue"],
                  period = "4")

        plot_words.main(graph.args())

    source_details = SOURCE_BASE[source]
    plot = get_plot(title=word,
                    filename=filename,
                    source=source_details["title"])
    return render_template("output.html",
                           #publication=source_details,
                           plot=plot)
