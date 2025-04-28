#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 02:58:20 2025

@author: josegomez7_snhu
"""

from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    def __init__(self, username, password, host='nv-desktop-services.apporto.com', port=31701, db='AAC', col='animals'):
        self.client = MongoClient(f'mongodb://{username}:{password}@{host}:{port}')
        self.database = self.client[db]
        self.collection = self.database[col]

    def create(self, data):
        if data is not None:
            self.collection.insert_one(data)
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    def read(self, query):
        if query is not None:
            return list(self.collection.find(query))
        else:
            raise Exception("Query parameter is empty")

    def update(self, query, update_values):
        if query is not None and update_values is not None:
            result = self.collection.update_many(query, {"$set": update_values})
            return result.modified_count
        else:
            raise Exception("Query and/or update values missing")

    def delete(self, query):
        if query is not None:
            result = self.collection.delete_many(query)
            return result.deleted_count
        else:
            raise Exception("Query parameter is empty")
            
        