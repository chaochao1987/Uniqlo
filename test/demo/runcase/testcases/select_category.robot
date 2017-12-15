*** Settings ***
#Suite Setup    Init set up
#Library         demo/workflow/BaseWorkFlow.py
Library         demo.workflow.BaseWorkFlow




*** Variables ***


*** Test Cases ***
select two items into cart then check if the properties are correct
    [Documentation]  select women type from navigation bar
    [Tags]  homepage
    [Setup]
    get data from file     different_items.yaml
    open url
    choose category
    choose different products
    check product info


*** Keywords ***
#Init set up     get data from file      $ {data_file}







