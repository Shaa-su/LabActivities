*** Variables ***
${BASE_URL}    https://the-internet.herokuapp.com


*** Settings ***
Library    SeleniumLibrary


*** Test Cases ***
Interact With Dropdown
    Open Browser    ${BASE_URL}/dropdown    chrome
    Select From List By Value    id:dropdown    2
    List Selection Should Be    id:dropdown    Option 2
    Select From List By Label    id:dropdown    Option 1
    List Selection Should Be    id:dropdown    Option 1
    [Teardown]    Close Browser

