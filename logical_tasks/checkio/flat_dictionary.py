"""Python dictionaries are a convenient data type to store and process configurations. They allow you to store data by
keys to create nested structures. You are given a dictionary where the keys are strings and the values are strings or
dictionaries. The goal is flatten the dictionary, but save the structures in the keys. The result should be the a
dictionary without the nested dictionaries. The keys should contain paths that contain the parent keys from the
original dictionary. The keys in the path are separated by a "/". If a value is an empty dictionary, then it should be
replaced by an empty string ("")."""
import pandas as pd
def flatten(dictionary):

     for x in dictionary:
          if dictionary[x] == {}:
               dictionary[x] = ""
     res = pd.json_normalize(dictionary, sep='/')
     return res.to_dict(orient='records')[0]


print(flatten({"key": "value"}))
print(flatten({"key": {"deeper": {"more": {"enough": "value"}}}}))
print(flatten({"empty": {}}))
print(flatten({"name": {
     "first": "One",
     "last": "Drone"},
     "job": "scout",
     "recent": {},
     "additional": {
          "place": {
               "zone": "1",
               "cell": "2"}}}))
