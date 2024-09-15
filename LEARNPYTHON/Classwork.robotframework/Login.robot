*** Settings ***
Library    SeleniumLibrary
Test Setup    open browser    https://tutorialsninja.com/demo/    Chrome
Test Teardown    close browser

*** Test Cases ***
VerifyThatLoginPageShouldBeOpened
    [Documentation]    Verify that login page should be opened
    maximize browser window
    click element    css:a[title='My Account']
    click link    Login
    title should be    Account Login
    sleep    5

VerifyThatUserShouldBeAbleToLogin
    [Documentation]    Verify that user should be able to do the login
    maximize browser window
    click element    css:a[title='My Account']
    click link    Login
    input text    name:email    abc@abc.com
    input text    id:input-password   abc@123

