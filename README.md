# Naveen_Immanuel_QA
WebPage_Test_SDET_Challenge

The Test Framework for testing the Ormuco portal.
Python Language was used to build this framework using Selenium as the tool. Since Selenium can support both Javascript and Python. Added its an open source tool for testing such portals.

Test Framework is built in below hierarchical format:


--> Data
This Folder contains all the input data related files/contents in it.
Contains Following Files in it.
1) Directory Expected Screenshots
Contains all the Test Cases expected Result Screenshots. It has captured the warning messages and error messages displayed.
2) ConfigFile.txt
Currently Contains Global/Common Variables to be used across all tests. Divided based on the section. Currently has single section for Page_Objects to select portal link, browser and Input Data Sheet name(Excel Sheet)
3) Parse_Input
Python File having reusable functions to read values, compare images, compare messages and generate test report.
4)Input_Data.xlsx
Excel Sheet containing Input Data to be tested. Browsers are identified by Sheets.Currently three Sheets are mentioned in Excel Sheet "Chrome,Firefox,Ie"

--> Config
1) Webdriver.py
This Folder contains Python Script for Selenium Webdriver Object initialisation, destruction and manipulation like screenshot.

-->PageObjects
Each Page in the Portal can be treated as object and functions can be written to manipulate on these pages as required. Currenlty Single Pageobject Home_Page has been identified for testing purpose.
1) Home_Page.py
Python Script that handles home page initialization, assigning values and finding locators.

-->Test Case
Contains Test Suite for Test Case Validation. Currently single test case for validating the invalid email/password login has been written using unittest suite format.
1) Test01_Chrome_InvalidLogin
Test Case to validate all the possible input datas fetched from Input data and validate the invalid login form in the portal.

-->Result
This Directory Consists of Test Results post test execution. We have the test result screenshots been saved, test results for each test logged and reported in text format.
1) Screenshot
Screenshot of all test outputs after test execution. This test result image is compared with the expected_screenshot to validate success/failure.
2)Test_Report_<Timestamp>
 Test Cases executed with their test id, test data and result is written into this file.
  
  Note: I had used the image comparision approach to handle the test warning flash messages validation and the test input was constructed only based to validate invalid login inputs.
  Test Cases/Inputs can be enhanced by validating forgot password,create new account, language selection. By adding more test data and reusable fnctions to manipulate across them.


