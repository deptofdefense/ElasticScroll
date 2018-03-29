import elasticsearch


class ElasticMinimal:
    def __init__(self, elastic_endpoint):
        """

        :param elastic_endpoint: a url corresponding to the api endpoint of the elasticsearch service
        :type elastic_endpoint: str
        """
        self.endpoint = elastic_endpoint
        self.es_client = elasticsearch.Elasticsearch(elastic_endpoint)

    def scroll_query(self, index, lookup, size=10, scroll='2m'):
        """

        :param index: the name of the index to query
        :type index: str

        :param lookup: the elasticsearch query
        :type lookup: dict

        :param size: (optional) size parameter for the query
        :type size: int

        :param scroll: (optional) scroll parameter for the query, default to '2m'
        :type scroll: str

        :return: iterator pointing to the data resulting from the query
        """
        page = self.es_client.search(index=index, scroll=scroll, size=size, body=lookup)
        sid = page['_scroll_id']
        scroll_size = page['hits']['total']

        while(scroll_size > 0):
            page = self.es_client.scroll(scroll_id=sid, scroll=scroll)
            sid = page['_scroll_id']
            scroll_size = len(page['hits']['hits'])

            for res in page['hits']['hits']:
                yield res['_source']