*** Variables ***
${BASE_URL}    https://the-internet.herokuapp.com
${BROWSER}    chrome
${START_BUTTON}    css:#start button
${FINISH_TEXT}    css:#finish h4

*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Handle Dynamic Load
    Open Browser    ${BASE_URL}/dynamic_loading/1    ${BROWSER}
    Click Element    ${START_BUTTON}
    Wait Until Element Is Visible    ${FINISH_TEXT}    10s
    Page Should Contain    Hello World!
    [Teardown]    Close Browser
