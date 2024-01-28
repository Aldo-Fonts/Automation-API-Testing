Feature: Demo. The current feature is a demo for api testing automation

Background: Setting up the automation
    Given I test the collection "test"
    And   I test the environment "PROD"
    And   I repeat it "1" time(s)
    And   I "accept" the failed tests
    And   I wait "10" seconds for requests to return a response
    And   I wait "10" seconds for scripts to return a response
    And   I "disable" SSL

Scenario: Report it on terminal
    Then  I send the request

Scenario: Report it on an html file
    And   I report it on "html"
    Then  I send the request

