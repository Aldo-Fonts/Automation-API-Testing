###############################################################################################################
# script:       builder.py
# description:  This script build a complex request and save it as a file
# version:      1.1
# creation:     December 2, 2023
# update:       January 2, 2024
###############################################################################################################
# Library(ies)
import json

# Function(s)
# new_collection creates a new name.postman_collection.json
def new_collection(name, apis):
    # All saved collections are in the path '/src/collection'
    origin_path = "../src/collection/"
    
    # Load the template JSON file
    with open(origin_path + "template.json", "r") as json_file:
        json_data = json.load(json_file)
    json_file.close()
    
    # Update collection information with the provided name
    json_data["info"]["name"] = name
    
    try:
        # Process each API
        for api in apis:
            # Load the JSON file for the current API
            with open(origin_path + api[0], "r") as json_file:
                json_api_data = json.load(json_file)
            json_file.close()
            
            # Search for the API in the loaded data and append it to the collection
            json_data["item"].append(search_api(json_api_data["item"], api[1]))
                    
        # Convert the updated JSON to a string with indentation
        updated_json = json.dumps(json_data, indent=4)
    except:
        return ["8"]
    try:    
        # Save the updated JSON to a new file with the specified name
        with open(origin_path + name + '.postman_collection.json', 'w') as json_file:
            json_file.write(updated_json)
        json_file.close()
    except:
        # Handle exceptions and return 0 on failure
        return ["5"]

def search_api(data, api_name, result=None):
    # Initialize the result list if not provided
    if result is None:
        result = []

    # Recursively search for the API in the data
    if isinstance(data, list):
        for element in data:
            result.extend(search_api(element, api_name))
    elif isinstance(data, dict):
        # Check if the current dictionary has a "name" key with the specified API name
        if "name" in data and data["name"] == api_name:
            result.append(data)
        # Recursively search through key-value pairs in the dictionary
        for key, value in data.items():
            result.extend(search_api(value, api_name))
    return result


new_collection(
    "new_collection",
    [
        ["api-v1.postman_collection.json",      "preferences"],
        ["automation.postman_collection.json",  "login i01 Copy"],
        ["test.postman_collection.json",        "region Copy"]
    ]
)
