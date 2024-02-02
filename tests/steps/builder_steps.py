###############################################################################################################
# script:       builder_steps.py
# description:  This script has the regular expressions and their implementation
# version:      0.1 
# creation:     January 10, 2023
# update:       January 27, 2023
###############################################################################################################
# Library/ies
from behave import *
import src.packages.builder as B

# Object(s)
builder = B.Builder()

# Regular expression(s) and function(s)
@step('From the collection: "{collection}"')
def set_collection(context, collection):
    builder.set_collection(collection)
    return

@step('I choose the API: "{api}"')
def set_api(context, api):
    builder.api = api
    builder.build_option()
    return

@step('I build the new collection: "{new_collection}"')
def build_collection(contex, new_collection):
    builder.new_collection(new_collection)
    return


 