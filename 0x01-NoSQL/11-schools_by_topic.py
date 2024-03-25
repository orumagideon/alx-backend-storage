#!/usr/bin/env python3
"""
search by topic
"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    search by topic
    """
    return mongo_collection.find({"topics": topic})
