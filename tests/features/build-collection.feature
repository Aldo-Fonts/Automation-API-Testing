Feature: build-collection.feature

    This feature is an example to build collections

    Scenario: Build a collection
        Given From the collection: "api-v2"
        Then I choose the API: "region"
        And I choose the API: "email"
        Given From the collection: "apps-amx_activity"
        Then I choose the API: "self"
        Given From the collection: "middleware"
        Then I choose the API: "ping"
        Then I build the new collection: "Automation"

    @Run
    Scenario: Run the builded collection
        Given I test the collection "Automation"
        And I test the environment "Prod"
        Then I send the request