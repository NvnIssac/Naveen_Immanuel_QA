import unittest
from Config.Webdriver import Driver
from PageObjects.Home_page import LoginScreen
from Data.Parse_Input import number_of_tests,look4_xlrd,look4_input,read_dict,compare_images,compare_warning,Test_Report
import os

#Variables with Global Scope in this File
#Below Variables are fetched from ConfigFile.txt
#URL-- Value of URL to be Tested
#Input_File --- The Input Data File, an excel sheet which has test data(ID, username, password etc) for testing
#Browser_onTest --- Select Chrome/Firefox/Ie
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
URL = str(look4_input('Home_URL'))
Input_File = str(look4_input('Home_TestInput'))
Browser_onTest = str(look4_input('Home_Browser'))

class Browser(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        "Constructor for the Driver factory"
        inst.driver = Driver(URL)

    def test_Case_Invalid_Login_case1(self):
        Page=LoginScreen(self.driver)
        #Loop through all the test inputs from the Excel Sheet
        for i in range(1,number_of_tests(Input_File,Browser_onTest)):
            Test_ID='Test_ID'+str(i)
            Dic=look4_xlrd(Input_File,Browser_onTest,Test_ID)
            Page.assign_values(read_dict(Dic,'Username'),read_dict(Dic,'Password'))
            Page.login()
            #Test Case Warning Message Validation
            Msg_Validation_Flag=compare_warning(read_dict(Dic,'Expected_Output'),Page.warning_message())
            #Take Screenshot for the text executed
            Screen_DIR = os.path.join(BASE_DIR, 'Data\Expected_Screenshot', Test_ID + '.png')
            Result_DIR = os.path.join(BASE_DIR, 'Result\Screenshot', 'Res' + Test_ID + '.png')
            self.driver.screenshot_page(Result_DIR)
            #Screenshot Image comparision to validate the exceptions are validated
            Img_Validation_Flag = compare_images(Screen_DIR, Result_DIR)
            Flag = lambda x1, x2: 'Success' if (x1 is True and x2 is True) else 'Failure'
            #Test Report Generation for tests validated
            Test_Report(Test_ID,read_dict(Dic, 'Username'),read_dict(Dic, 'Password'),Flag(Msg_Validation_Flag, Img_Validation_Flag),Result_DIR)

    @classmethod
    def tearDownClass(inst):
        # close the browser window
        inst.driver.close_web()

def Testsuite():
    Testsuite=unittest.TestSuite()
    return Testsuite

if __name__ == '__main__':
   unittest.main()


