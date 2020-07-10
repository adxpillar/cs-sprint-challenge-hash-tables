# Your code here
import urllib.request,urllib.parse
import datetime
import os

CACHE_EXPIRATION_SECONDS = 10

class CacheEntry:
    def __init__(self, files, data):
        self.files = files
        self.data = data
        self.timestamp = get_timestamp()

cache = {}

def get_timestamp():
    return datetime.datetime.now().timestamp()


# timestamp = get_timestamp()

def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here

    cur_time = get_timestamp()
    result = []
    for path in files:
        if (path not in cache) or (cur_time - cache[path].timestamp > CACHE_EXPIRATION_SECONDS):
            print("cache miss!")
            resp = open(path)
            data = resp.read()
            resp.close()
            for d in data:
                if str(d) in path:
                    data = data.decode()
                    cache[path] = CacheEntry(path,data)
                    result.append(cache[path])
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
