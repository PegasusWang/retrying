#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from retrying import retry

# @retry
# def do_something_unreliable():
    # print('hehe')
    # if random.randint(0, 10) > 5:
        # raise IOError("Broken sauce, everything is hosed!!!111one")
    # else:
        # return "Awesome sauce!"


# def retry_if_io_error(exception):
    # return isinstance(exception, IOError)

# @retry(retry_on_exception=retry_if_io_error)
# def read_a_file():
    # with open("file", "r") as f:
        # return f.read()


def retry_if_result_none(result):
    """Return True if we should retry (in this case when result is None), False otherwise"""
    return result is None


def after_attempts(num):
    return 0

def stop_func()
@retry(retry_on_result=retry_if_result_none, stop_max_attempt_number=7,
       after_attempts=after_attempts, wrap_exception=True,
       default_return_value=1000)
def might_return_none():
    print "Retry forever ignoring Exceptions with no wait if return value is None"
    return None
    # return 1


print(might_return_none())
