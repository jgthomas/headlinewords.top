from operator import itemgetter


def composite_ranks(data, rev=True):
    """
    Return ordered sequence of summed counts for all
    words from all sources specified in data.

    """
    combined_count = {}
    for source in data:
        for record in source:
            word, count = record
            if word not in combined_count:
                combined_count[word] = count
            else:
                combined_count[word] += count
    ranked = [(k, v) for k, v in combined_count.items()]
    return sorted(ranked, key=itemgetter(1), reverse=rev)
