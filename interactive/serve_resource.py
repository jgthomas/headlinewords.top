import os.path
from flask import Blueprint, render_template, request, redirect, url_for
import plot_words
from graph import Graph, get_plot
from constants import SOURCES, SOURCE_BASE, PLOT_PATH, ON_DEMAND_PATH, ON_DEMAND_LOAD
from query import word_count_by_source
from query_functions import TODAY


serve = Blueprint("serve", __name__)


@serve.route("/graph", methods=["GET"])
def graph():
    word = request.args.get("word_to_graph", "").lower()
    colour = request.args.get("colour", "")
    source = request.args.get("check", "")

    if not word:
        return redirect(url_for("home", _anchor="graph-maker"))

    if source == "all":
        if not os.path.isfile(''.join([ON_DEMAND_PATH, word, ".png"])):
                sources = word_count_by_source(word, "word_ever", SOURCES)
                plot_words.plot_bar(sources, colour=colour, path=ON_DEMAND_PATH)
        plot = get_plot(title=word,
                        filename=''.join([word, ".png"]),
                        source="Comparative Frequency",
                        path=ON_DEMAND_LOAD)

    else:
        filename = ''.join([word, "_", source, ".png"])

        if not os.path.isfile(''.join([ON_DEMAND_PATH, filename])):
            graph = Graph(db = source,
                    filename = ''.join([word, '_', source]),
                    path = ON_DEMAND_PATH,
                    days = "7",
                    words = [word],
                    colour = [colour],
                    period = "4")
            plot_words.main(graph.args())

        source_details = SOURCE_BASE[source]

        plot = get_plot(title=word,
                    filename=filename,
                    source=source_details["title"],
                    path=ON_DEMAND_LOAD)

    return render_template("output.html", plot=plot)
