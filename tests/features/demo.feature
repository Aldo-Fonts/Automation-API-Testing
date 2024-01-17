Feature: Demo. The current feature is a demo for api testing automation

Scenario Outline: Demo for automation collection
    Then  I send the request with <options>

    Examples:
        | options                           | 
        | iterations = 1, SSL, report, skip | 

