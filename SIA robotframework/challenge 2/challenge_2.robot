*** Variables ***
${BASE_URL}    https://the-internet.herokuapp.com
${LOGIN_PATH}    /login
${BROWSER}    chrome

*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Verify Login Page Title
    Open Browser    ${BASE_URL}${LOGIN_PATH}    ${BROWSER}
    Title Should Be    The Internet
    Close Browser
