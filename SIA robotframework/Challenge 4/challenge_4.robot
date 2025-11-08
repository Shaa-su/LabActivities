*** Variables ***
${BASE_URL}    https://the-internet.herokuapp.com
${LOGIN_PATH}    /login
${BROWSER}    chrome
${USERNAME_FIELD}    id:username
${PASSWORD_FIELD}    id:password
${LOGIN_BUTTON}    css:button[type='submit']

*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Validate Successful Login
    Perform Login    tomsmith    SuperSecretPassword!
    Page Should Contain    You logged in to the secure area!
    [Teardown]    Close Browser

*** Keywords ***
Perform Login
    [Arguments]    ${username}    ${password}
    Open Browser    ${BASE_URL}${LOGIN_PATH}    ${BROWSER}
    Input Text    ${USERNAME_FIELD}    ${username}
    Input Text    ${PASSWORD_FIELD}    ${password}
    Click Element    ${LOGIN_BUTTON}
