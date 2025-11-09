*** Settings ***
Library    SeleniumLibrary


*** Variables ***
${BASE_URL}    https://the-internet.herokuapp.com


*** Test Cases ***
Validate Checkbox States
    Open Browser    ${BASE_URL}/checkboxes    chrome
    Checkbox Should Not Be Selected    xpath://form[@id='checkboxes']/input[1]
    Checkbox Should Be Selected    xpath://form[@id='checkboxes']/input[2]
    Select Checkbox    xpath://form[@id='checkboxes']/input[1]
    Unselect Checkbox    xpath://form[@id='checkboxes']/input[2]
    Checkbox Should Be Selected    xpath://form[@id='checkboxes']/input[1]
    Checkbox Should Not Be Selected    xpath://form[@id='checkboxes']/input[2]
    [Teardown]    Close Browser
