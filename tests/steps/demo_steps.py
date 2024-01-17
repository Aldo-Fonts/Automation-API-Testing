###############################################################################################################
# script:       demo_steps.py
# description:  This script has the regular expressions and their implementation
# version:      0.1 (Alpha)
# creation:     January 10, 2023
# update:       January 16, 2023
###############################################################################################################
# Library/ies
from behave import given, when, then
import src.packages.request     as SR
import src.packages.Collection  as SC

# Regular expression(s) and function(s)
@given('I set a collection')
def set_collection(context):
    context.collection = SC.collection()
    context.collection.getCollection()
    
@then('I set an environment')
def set_collection(context):
    context.collection.getEnvironment()
    
@given('I send the request with {options}')
def send_request(context, options):
    #TODO: Get the options and use them to send a request
    return