###############################################################################################################
# script:       Collection.py
# description:  This script read a given postman collection to get the APIs and its information
# version:      1.3
# creation:     December 2, 2023
# update:       January 27, 2023
###############################################################################################################
# Library/ies
import json
import shutil
from os import listdir
from os.path import isfile, join
from os import getcwd

import src.packages.finder as finder
import src.packages.printData as printData
import src.packages.error as error
# Class
class collection:
    # Constructor
    def __init__(self):
        # Attribute(s)
        self.path            = getcwd()
        self.environment     = "../src/environment/PROD.postman_environment.json"       # Prod
        self.collection      = "../src/collection/automation.postman_collection.json"   # Login
        self.table           = [["Name", "Method", "Endpoint","Collection"]]            # Data table
        self.collection_name = "automation.postman_collection.json"                     # Collection name
        self.collections     = []                                                       # No collections
        
    # Method(s)
    def set_environment(self, env):
        self.environment = self.path + '/assets/environment/' + env + '.postman_environment.json'
        if(validate_environment(self.environment) == False):
            # It returns the error 2, it can be read in the error.py
            error.popup_showerror("2")
            
    def set_collection(self, col):
        self.collection = self.path + '/assets/collection/' + col + '.postman_collection.json'
        if(validate_collection(self.collection) == False):
            # It returns the error 1, it can be read in the error.py 
            error.popup_showerror("1")
    
    def get_environment(self):
        # Open a file finder to upload the environment file
        self.environment = finder.search("environment")
        # Validate the environment as a file and its content
        if(validate_environment(self.environment) == False):
            # It returns the error 2, it can be read in the error.py 
            self.environment = ["2"]
            
    def get_collection(self):
        # Open a file finder to upload the environment file
        self.collection = finder.search("collection")
        # Validate the environment as a file and its content
        if(validate_collection(self.collection) == False):
            # It returns the error 2, it can be read in the error.py 
            self.environment = ["1"]
        
    # Collection name and return it full name
    def get_collection_name(self):
        self.collection_name = self.collection.split("/")[-1]

    # Read all the collections and its apis
    def read_collections(self):
        try:
            # All saved collections are in the path '/src/collection'
            origin_path = self.path + '/assets/collection'
            # Give a list of all files on the path
            files = [arch for arch in listdir(origin_path) if isfile(join(origin_path, arch))]
            # Iterate on every file in files
            for file in files:
                # The file must be different to 'template.json'
                if(file != 'template.json'):
                    apis = []
                    # The value on the index 0 is the collection's name
                    apis.append(file)
                    # Open every json file to read it and load it as a json variable
                    with open(origin_path + '/' + file,'r') as json_file:
                        json_data = json.load(json_file)
                    json_file.close()
                    # Iterate on the items of the json variable
                    for item in json_data['item']:
                        # Add the api's name
                        apis.append(item['name'])
                    # Make a list of lists with the API's    
                    self.collections.append(apis)    
        # It returns the error 3, it can be read in the error.py        
        except:
            self.collections = ["7"]
            
    # Read the collection from a postman collection file
    def get_table(self):
        try:
            # Open the file with read mode
            with open(self.collection,"r") as json_file:
                # # The infomation is load and saved as a json data
                json_data = json.load(json_file)
            # Close the given file
            json_file.close()
            # Save the collection name
            collection_name = json_data['info']['name']
            # Iterate on the json data values with the parent key 'item'
            for i in json_data['item']:
                # Use an empty list
                key_value = []
                # Append the values of the keys 'name', 'method', 'url' and the collection name
                key_value.append(i['name'])
                key_value.append(i['request']['method'])
                key_value.append(i['request']['url']['raw'].replace("{{portal}}","").replace("{{instance}}",""))
                key_value.append(collection_name)
                # The result list is appended to the table list
                self.table.append(key_value)
        except: 
            self.table = ["3"]
                
    # copyCollection. It saves the given collection on the path /src/collection            
    def copy_collection(self):
        try:
            self.fileName()
            # Copy the given collection on a new path, /src/collection
            shutil.copy(
                self.collection,
                "../src/collection/" + self.collection_name
            )
        # If it fails, the function return the error #4 from error.py
        except:
            self.collection_name = ["4"]

# Validate the environment file given in getEnvironment()
def validate_environment(postman_environment):
    try:
        # Open the file with read mode
        with open(postman_environment, 'r') as json_file:
            # The infomation is load and saved as a json data
            json_data = json.load(json_file)
        # Close the given file
        json_file.close()
        # If the json_data contains the key '_postman_variable_scope' the value will be a string
        if(type(json_data['_postman_variable_scope']) == str):
            # If is true, it pass the validation
            validation = True
    # The exception happens when the json_data does not contain the given key        
    except:
        # It fails the validation
        validation = False
    finally:
        # Return the validation value
        return validation

# Validate the collection file given in readCollectionJson()  
def validate_collection(postman_collection):
    try:
        # Open the file with read mode
        with open(postman_collection, 'r') as json_file:
            # The infomation is load and saved as a json data
            json_data = json.load(json_file)
        # Close the given file
        json_file.close()
        # If the json_data contains the key 'info' and it has a key called '_collection_link' the value will be a string
        if(type(json_data['info']['name']) == str):
            # If is true, it pass the validation
            validation = True
    # The exception happens when the json_data does not contain the given keys        
    except:
        # It fails the validation
        validation = False
    finally:
        # Return the validation value
        return validation
