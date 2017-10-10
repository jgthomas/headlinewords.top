import os.path
from flask import Blueprint, render_template, request, redirect, url_for
from plot_words import bar_plot, line_plot
from graph import Graph, get_plot, make_bar_chart
from constants import (COUNTRY_SOURCES, SOURCE_BASE,
                       PLOT_PATH, ON_DEMAND_PATH, ON_DEMAND_LOAD)
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

    if source in COUNTRY_SOURCES:
        source_orgs = COUNTRY_SOURCES[source]
        filename = ''.join([source, "_", word, "_", colour, ".png"])
        if not os.path.isfile(''.join([ON_DEMAND_PATH, filename])):
            sources = word_count_by_source(word, "word_ever", source_orgs)
            graph = make_bar_chart(word,
                                   sources,
                                   filename,
                                   colour,
                                   ON_DEMAND_PATH)
            bar_plot(graph)
        plot = get_plot(title=word,
                        filename=filename,
                        source="Comparative Frequency",
                        path=ON_DEMAND_LOAD)

    else:
        filename = ''.join([word, "_", source, "_", colour, ".png"])

        if not os.path.isfile(''.join([ON_DEMAND_PATH, filename])):
            graph = Graph(db = source,
                    filename = ''.join([word, '_', source, '_', colour]),
                    path = ON_DEMAND_PATH,
                    days = 7,
                    words = [word],
                    colour = [colour],
                    period = 4)
            line_plot(graph)

        source_details = SOURCE_BASE[source]

        plot = get_plot(title=word,
                    filename=filename,
                    source=source_details["title"],
                    path=ON_DEMAND_LOAD)

    return render_template("output.html", plot=plot)
