import time
from concurrent import futures
MAX_WORKERS = 20


def double_one(multiplier):
    result = 2 * multiplier
    try:
        time.sleep(multiplier)
    except TypeError:
        return TypeError
    print(result)
    return result


def double_many(cc_list):
    workers = min(MAX_WORKERS, len(cc_list))
    with futures.ThreadPoolExecutor(workers) as executor:
        res = executor.map(double_one, cc_list)
    if res.__contains__(TypeError):
        return "Non number found"
    return "Doubled all"


def double_many_future(cc_list):
    workers = min(MAX_WORKERS, len(cc_list))
    with futures.ThreadPoolExecutor(workers) as executor:
        to_do = []
        for item in cc_list:
            try:
                future = executor.submit(double_one, item)
            except TypeError as exc:
                print(msg.format(item, exc.__class__.__name__))
            else:
                to_do.append(future)
                msg = 'Scheduled for {}: {}'
                print(msg.format(item, future))
        results = []
        for future in futures.as_completed(to_do):
            res = future.result()
            msg = '{} result: {!r}'
            print(msg.format(future, res))
            results.append(res)
    if results.__contains__(TypeError):
        return "Non number found"
    print("Doubled all")
    return results