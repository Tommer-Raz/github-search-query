import time
import requests

FILE_PATH = "C:\\Users\\tomme\\github-search-query\\queries.txt"

def query_github(filename):
    result = {
        "sum_total_count": 0,
        "items": [],
    }

    with open(FILE_PATH) as file:
        for query in file:
            for attempt in range(10):
                try:
                    response = requests.get(query.encode("utf-8")).json()
                    result["sum_total_count"] += response["total_count"]
                    result["items"] += response["items"]
                    break
                except:
                    time.sleep(60)
        return result

if __name__ == "__main__":
    query_github(FILE_PATH)