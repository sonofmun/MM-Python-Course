from feedparser import parse

def read_rss(address="http://www.enc-sorbonne.fr/fr/rss"):
    """ Read a RSS feed and returns a simpler format

    :param address: URI Address of the RSS Feed
    :type address: str
    :yields: Tuple of (Title, Summary, Link, Published)
    """
    feed = parse(address)
    for item in feed["items"]:
        line = (
            item["title_detail"]["value"],
            item["summary_detail"]["value"],
            item["link"],
            item["published"]
        )
        yield line