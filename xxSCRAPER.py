def __init__(self, config):
    self.config = config
    pass


# start initial request
def search(self, query):
    print('INFO: Searching FMovies for "' + query + '"...')
    url = str(self.config['indexer fmovies']['url'])
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    }
    params = (
        ('keyword', query),
    )




## to get cookies and return ehader
def get_cookie(self, url):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    }

    response = requests.get(url, headers=headers, verify=False)
    cookie = '; '.join([x.name + '=' + x.value for x in response.cookies])

    return cookie



