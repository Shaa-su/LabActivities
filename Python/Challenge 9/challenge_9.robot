*** Variables ***
${BASE_URL}    https://the-internet.herokuapp.com
${BROWSER}    chrome
${ALERT_BUTTON}    xpath://button[@onclick='jsAlert()']
${CONFIRM_BUTTON}    xpath://button[@onclick='jsConfirm()']

*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Validate Alert Text and Actions
    Open Browser    ${BASE_URL}/javascript_alerts    ${BROWSER}
    
    Click Element    ${ALERT_BUTTON}
    Alert Should Be Present    I am a JS Alert
    
    Click Element    ${CONFIRM_BUTTON}
    Handle Alert    DISMISS
    Page Should Contain    You clicked: Cancel
    
    Click Element    ${CONFIRM_BUTTON}
    Handle Alert    ACCEPT
    Page Should Contain    You clicked: Ok
    
    [Teardown]    Close Browser
