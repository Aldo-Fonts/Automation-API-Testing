###############################################################################################################
# script:       demo_steps.py
# description:  This script has the regular expressions and their implementation
# version:      0.1 
# creation:     January 10, 2023
# update:       January 27, 2023
###############################################################################################################
# Library/ies
from behave import *
import src.packages.request     as SR
import src.packages.Collection  as SC

# Object(s)
collection = SC.collection()
request    = SR.request()

# Regular expression(s) and function(s)
@step('I test the collection "{text}"')
def set_collection(context, text):
    collection.set_collection(text)
    print(f"{collection.collection}\n")
    
@step('I test the environment "{text}"')
def set_environment(context, text):
    collection.set_environment(text)

@step('I repeat it "{text}" time(s)')
def set_repetitions(context, text):
    request.build_options("n",text)

@step('I "{text}" the failed tests')
def set_skip_test(context, text):
    if(text == "accept"):
        request.build_options("x")

@step('I wait "{text}" seconds for requests to return a response')
def set_request_time(context, text):
    request.build_options("tr", str(1000 * int(text)))

@step('I wait "{text}" seconds for scripts to return a response')
def set_script_time(context, text):
    request.build_options("ts", str(1000 * int(text)))

@step('I "{text}" SSL')
def set_ssl_status(context, text):
    if(text == "disable"):
        request.build_options("k")

@step('I report it on "{text}"')
def set_report_output(context, text):
    if(text == "html"):
        request.build_options("html")

@step('I send the request')
def send_request(context):
    request.collection  = collection.collection
    request.environment = collection.environment
    request.build_request()
    request.send_request()
 