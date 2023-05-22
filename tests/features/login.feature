Feature: Modify the login process so that in addition to username and password it is mandatory to accept a privacy policy check before to click the submit button
# Scenario: 1
Scenario: Check the login correctly to site
 Given user is at the login page
 When user enter the '<username>'
 And user enter a '<password >'
 And user check the Privacy Policy checkbox
 And user click on submit button
 Then should display a title is '<title>'

# Scenario: 2
Scenario : Missing username
 Given user is at the login page
 When  user do not enter a '<username>'
 And user enter a '<password>'
 And user check the privacy policy checkbox
 Then should display the message alert as "Username, Password, and Privacy Policy Check are required"
 And user click on submit button
 And should not display the title '<title>'


# Scenario: 3
Scenario : Missing password
 Given user is at the login page
 When user enter a '<username>'
 And  user do not enter a '<password>'
 And user check the privacy policy checkbox
 Then should display the message alert as "Username, Password, and Privacy Policy Check are required"
 And user click on submit button
 And should not display the title '<title>'

# Scenario: 4
Scenario : Privacy policy checkbox not checked
 Given user is at the login page
 When user enter a valid '<username>'
 And user enter a valid '<password>'
 And user do not check the privacy policy checkbox
 Then should display the message alert as "Username, Password, and Privacy Policy Check are required"
 And user click on submit button
 And should not display the title '<title>'

# Scenario: 5
Scenario : Valid username and password
 Given user is at the login page
 When user enter a valid '<username>'
 And user enter a valid '<password>'
 And user check the privacy policy checkbox
 And user click on submit button
 Then should display the title '<title>'

# Scenario: 6
Scenario : Invalid username
 Given user is at the login page
 When user enter an invalid '<username>'
 And user enter a valid '<password>'
 And user check the privacy policy checkbox
 And user click on submit button
 Then should display the message alert as "Invalid username or password"
 And should not display the title '<title>'

# Scenario: 7
Scenario : Invalid password
 Given user is at the login page
 When user enter a valid '<username>'
 And user enter an invalid '<password>'
 And user check the privacy policy checkbox
 And user click on submit button
 Then should display the message alert "Invalid username or password"
 And should not display the title '<title>'

# Scenario: 8
Scenario : Active user
 Given user is at the login page
 When user enter an active '<username>'
 And user enter a valid '<password>'
 And user check the privacy policy checkbox
 And user click on submit button
 Then should display the title '<title>'

# Scenario: 9
Scenario : Inactive user
 Given user is at the login page
 When user enter an inactive '<username>'
 And user enter a '<password>'
 And user check the privacy policy checkbox
 And user click on submit button
 Then should display the message alert "Inactive User"
 And should not display the title '<title>'