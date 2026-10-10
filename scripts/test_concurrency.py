import json
import sys
import urllib.request
import uuid
from concurrent.futures import ThreadPoolExecutor

BASE_URL = "http://localhost:8000"
TOTAL_REQUESTS = 200
WORKERS = 40


def call_fizzbuzz(params: str) -> int:
    with urllib.request.urlopen(f"{BASE_URL}/api/v1/fizzbuzz?{params}") as resp:
        return resp.status


def main() -> int:
    tag = uuid.uuid4().hex[:8]
    params = f"int1=3&int2=5&limit=10&str1=T{tag}&str2=B{tag}"

    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        statuses = list(pool.map(call_fizzbuzz, [params] * TOTAL_REQUESTS))

    failed = [s for s in statuses if s != 200]
    if failed:
        print(f"FAIL: {len(failed)} requests returned non-200")
        return 1

    with urllib.request.urlopen(f"{BASE_URL}/api/v1/stats") as resp:
        stats = json.load(resp)

    print(f"sent: {TOTAL_REQUESTS}, recorded hits: {stats['hits']}")

    if stats["str1"] != f"T{tag}":
        print("FAIL: most frequent entry is not ours (server not fresh?)")
        return 1
    if stats["hits"] != TOTAL_REQUESTS:
        print(f"FAIL: lost {TOTAL_REQUESTS - stats['hits']} updates (race condition)")
        return 1

    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
