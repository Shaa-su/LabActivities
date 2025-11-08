*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${BASE_URL}    https://the-internet.herokuapp.com
${LOGIN_PATH}    /login
${BROWSER}    chrome
${USERNAME_FIELD}    id=username
${PASSWORD_FIELD}    id=password
${LOGIN_BUTTON}    css:button[type='submit']

*** Keywords ***
Given I am on the login Page
    Open Browser    ${BASE_URL}${LOGIN_PATH}    ${BROWSER}

When I submit credentials
    [Arguments]    ${user}    ${pass}
    Input Text    ${USERNAME_FIELD}    ${user}
    Input Text    ${PASSWORD_FIELD}    ${pass}
    Click Element    ${LOGIN_BUTTON}

Then I should see the secure area
    Page Should Contain    You logged into a secure area!

And I close the browser
    Close Browser