*** Settings ***
Library     SeleniumLibrary

*** Test Cases ***
verifyCategoryfromloop
       [Documentation]    Verify thot category should be displayed from list
        open browser    https://tutorialsninja.com/demo/ chrome
        maximize browser window
        ${element}    get webelements   css:h4 > a
         FOR    ${getcategory}    IN    @{element}