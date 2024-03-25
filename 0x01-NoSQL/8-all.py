#!/usr/bin/env python3
"""
function that lists all document
"""
import pymongo


def list_all(mongo_collection):
    """
    all collections list
    """
    if not mongo_collection:
        return []
    return list(mongo_collection.find())
