*** Settings ***
Library    SeleniumLibrary
Test Setup    open browser    https://tutorialsninja.com/demo/    Chrome


*** Test Cases ***
VerifySearchSuggestionPage
    [Documentation]    Verify that search suggestion page should be opened
    maximize browser window
    input text    name:search   iPhone
    click element    css:.btn.btn-default.btn-lg