###############################################################################################################
# script:       builder.py
# description:  This script build a complex request and save it as a file
# version:      1.1
# creation:     December 2, 2023
# update:       January 2, 2024
###############################################################################################################
# Library(ies)
import json
import os

# Class
class Builder:
    def __init__(self):
        self.path           = os.getcwd() + '/assets/collection/'   # All saved collections are in the path '/assets/collection/'
        self.collection     = ''                                    # Given collection that contains an specific API
        self.api            = ''                                    # Given API to build a collection
        self.builder_args   = []                                    # Must be a list of lists

    # Method(s)
    # new_collection creates a new name.postman_collection.json
    def new_collection(self, name):
        # Load the template JSON file
        with open(self.path + "template.json", "r") as json_file:
            json_data = json.load(json_file)
        json_file.close()
        
        # Update collection information with the provided name
        json_data["info"]["name"] = name
        
        try:
            # Process each API
            for api in self.builder_args:
                # Load the JSON file for the current API
                with open(self.path + api[0], "r") as json_file:
                    json_api_data = json.load(json_file)
                json_file.close()
                
                # Search for the API in the loaded data and append it to the collection
                json_data["item"].append(self.search_api(json_api_data["item"], api[1])[0])
                        
            # Convert the updated JSON to a string with indentation
            updated_json = json.dumps(json_data, indent=4)
        except:
            return ["8"]
        try:    
            # Save the updated JSON to a new file with the specified name
            with open(self.path + name + '.postman_collection.json', 'w') as json_file:
                json_file.write(updated_json)
            json_file.close()
        except:
            # Handle exceptions and return 0 on failure
            return ["5"]

    # Search an API from a given collection
    def search_api(self, data, api_name, result=None, depth=0, max_depth=100):
        # Initialize the result list if not provided
        if result is None:
            result = []

        # Check if the depth exceeds the maximum allowed depth
        if depth > max_depth:
            print("Exceeded maximum depth. Returning.")
            return result

        # Recursively search for the API in the data
        if isinstance(data, list):
            for element in data:
                result.extend(self.search_api(element, api_name, depth=depth + 1, max_depth=max_depth))
        elif isinstance(data, dict):
            # Check if the current dictionary has a "name" key with the specified API name
            if "name" in data and data["name"] == api_name:
                result.append(data)
            # Recursively search through key-value pairs in the dictionary
            for key, value in data.items():
                result.extend(self.search_api(value, api_name, depth=depth + 1, max_depth=max_depth))
        return result

    # Set collection name
    def set_collection(self, name):
        self.collection = name + ".postman_collection.json"

    # Make a list of lists that cointains arguments to build a collection
    def build_option(self):
        self.builder_args.append(
            [
                self.collection,
                self.api
            ]
        )
        
'''
build = Builder()
build.builder_args = [
        ['api-v2.postman_collection.json', 'region'], 
        ['api-v2.postman_collection.json', 'email'], 
        ['apps-amx_activity.postman_collection.json', 'self'], 
        ['Muchas-cosas.postman_collection.json', 'ping']
    ]
build.new_collection("Automation")
'''
