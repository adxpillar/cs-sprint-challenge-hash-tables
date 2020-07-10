# Your code here
import urllib.request
import datetime

CACHE_EXPIRATION_SECONDS = 10


cache = {}

def get_timestamp():
    return datetime.datetime.now().timestamp()


timestamp = get_timestamp()

def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here

    cur_time = get_timestamp()

    for path in files:
        if (path not in cache) or (cur_time - cache[path].timestamp > CACHE_EXPIRATION_SECONDS):
            print("cache miss!")
            resp = urllib.request.urlopen(path)

            data = resp.read()
            resp.close()
            data = data.decode()
            # cache[path] = CacheEntry(path,data)
            result = cache[path].data
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



