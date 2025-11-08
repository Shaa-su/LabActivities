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
Attempt Login Form Entry
    Open Browser    ${BASE_URL}${LOGIN_PATH}    ${BROWSER}
    Input Text    ${USERNAME_FIELD}    tomsmith
    Input Text    ${PASSWORD_FIELD}    SuperSecretPassword!
    Click Element    ${LOGIN_BUTTON}
    Close Browser
