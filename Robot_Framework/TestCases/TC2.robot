*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${BROWSER}     chrome
${URL}         https://demo.nopcommerce.com/
${CHROMEDRIVER_PATH}    /usr/bin/chromedriver

*** Test Cases ***
LoginTest
    Open Browser    ${URL}    ${BROWSER}  executable_path=${CHROMEDRIVER_PATH}
    Click link      xpath://a[@class='ico-login']
    Close Browser