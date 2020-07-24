# Your code here
import urllib.request,urllib.parse
import os
cache = {}

def finder(files, queries):
    """
    YOUR CODE HERE
    """

    for path in files:
            resp = open(path)
            data = resp.read()
            data = data.split()
            cache[data] = []
            for q in queries:
                if q not in cache[data]:
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
