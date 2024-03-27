#!/usr/bin/env python3
"""
Contains the class definition for managing a Redis cache
"""
import redis
import uuid
from functools import wraps
from typing import Union, Callable, Optional


def count_calls(method: Callable) -> Callable:
    """
    Decorator function to count the number of times a method is called
    Args:
        method: The method to be decorated
    Returns:
        The decorated method
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper function for the decorated method
        Args:
            self: The object instance
            *args: The arguments passed to the method
            **kwargs: The keyword arguments passed to the method
        Returns:
            The return value of the decorated method
        """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator function to record the history of method calls
    Args:
        method: The method to be decorated
    Returns:
        The decorated method
    """
    key = method.__qualname__
    inputs = key + ":inputs"
    outputs = key + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper function for the decorated method
        Args:
            self: The object instance
            *args: The arguments passed to the method
            **kwargs: The keyword arguments passed to the method
        Returns:
            The return value of the decorated method
        """
        self._redis.rpush(inputs, str(args))
        data = method(self, *args, **kwargs)
        self._redis.rpush(outputs, str(data))
        return data

    return wrapper


def replay(method: Callable) -> None:
    """
    Function to replay the history of method calls
    Args:
        method: The method to be replayed
    Returns:
        None
    """
    name = method.__qualname__
    cache = redis.Redis()
    calls = cache.get(name).decode("utf-8")
    print("{} was called {} times:".format(name, calls))
    inputs = cache.lrange(name + ":inputs", 0, -1)
    outputs = cache.lrange(name + ":outputs", 0, -1)
    for i, o in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(name, i.decode('utf-8'),
                                     o.decode('utf-8')))


class Cache:
    """
    Class for managing Redis cache operations
    """
    def __init__(self) -> None:
        """
        Initializes the Redis client
        Attributes:
            self._redis (redis.Redis): Redis client instance
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores data in the Redis cache
        Args:
            data (dict): Data to be stored
        Returns:
            str: Key generated for the stored data
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None)\
            -> Union[str, bytes, int, float, None]:
        """
        Retrieves data from the Redis cache
        """
        data = self._redis.get(key)
        if data is not None and fn is not None and callable(fn):
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """
        Retrieves data as string from the Redis cache
        Args:
            key (str): Key for the data
        Returns:
            str: Retrieved data as string
        """
        data = self.get(key, lambda x: x.decode('utf-8'))
        return data

    def get_int(self, key: str) -> int:
        """
        Retrieves data as integer from the Redis cache
        Args:
            key (str): Key for the data
        Returns:
            int: Retrieved data as integer
        """
        data = self
