*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  sini
    Set Password  sini1234567
    Set Password_Confirmation  sini1234567
    Submit User
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  s
    Set Password  sini1234567
    Set Password_Confirmation  sini1234567
    Submit User
    Register Should Not Succeed

Register With Valid Username And Too Short Password
    Set Username  kayttaja
    Set Password  12
    Set Password_Confirmation  12
    Submit User
    Register Should Not Succeed

Register With Nonmatching Password And Password Confirmation
    Set Username  sini
    Set Password  sini1234567
    Set Password_Confirmation  sini123457
    Submit User
    Register Should Not Succeed

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Not Succeed
    Register Page Should Be Open

Submit User
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password_Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Create User And Go To Login Page
    Create User  kalle  kalle123
    Go To Login Page
    Login Page Should Be Open
