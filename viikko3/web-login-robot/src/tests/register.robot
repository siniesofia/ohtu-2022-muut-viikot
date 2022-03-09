*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
# Register With Valid Username And Password
#     Set Username  sini
#     Set Password  sini123
#     Submit User
#     Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  s
    Set Password  sini123
    Submit User
    Register Should Not Succeed

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Not Succeed
    Welcome Page Should Be Open

Submit User
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Create User And Go To Login Page
    Create User  kalle  kalle123
    Go To Login Page
    Login Page Should Be Open