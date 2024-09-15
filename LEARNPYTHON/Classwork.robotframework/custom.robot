*** Settings ***
Library    SeleniumLibrary
Library    robot-custom.py

*** Test Cases ***
verifycustomtestcase
    [Documentation]    verify that custom should be run
     open_website
     print_title
