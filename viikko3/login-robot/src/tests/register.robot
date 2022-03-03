*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User


*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  sini  sini1234
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  si  sini1234
    Output Should Contain  Length of username must be at least 3 characters

Register With Valid Username And Too Short Password
    Input Credentials  sini  sin
    Output Should Contain  Length of password must be at least 8 characters

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  sini  siniasdfasdfaf
    Output Should Contain  Salasana ei saa koostua pelkästään kirjaimista

*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  kalle  kalle123
