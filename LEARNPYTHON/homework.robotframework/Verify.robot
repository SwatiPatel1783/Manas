*** Settings ***
Library    SeleniumLibrary

Test Setup         open browser   https://www.cheapflights.ca/    Chrome

*** Test Cases ***
Verify 'X' Button on the Sign-In Page
      maximize browser window
      sleep    5
      click element    class:J-sA-label
      sleep    5
      click element    css:div.dDYU-close
      sleep     5
      close browser

Flight Search
    maximize browser window
    click element    class:c1qgT
    sleep    3
    click element    xpath://li[@id="oneway"]
   #click element    id:oneway
    sleep    5
   #click element   id:roundtrip
   #sleep    3
   # click element   id:multicity
   # sleep    3

Verify Input for "From?"
      maximize browser window
      click element    xpath://input[@aria-label="Flight origin input"]