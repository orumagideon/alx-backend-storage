#!/usr/bin/env python3
"""
Transforms school topic
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """
    updated many rows
    """
    return mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
