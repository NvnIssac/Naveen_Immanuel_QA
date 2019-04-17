import xlrd
import configparser
import os
import datetime
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def look4_input(input_string):
    #Read Input Contents from Config File
    DIR = os.path.join(BASE_DIR, 'Data', 'ConfigFile.txt')
    config = configparser.RawConfigParser()
    config.read(DIR)
    return(config.get('Page_Object',input_string))

def number_of_tests(File,Browser):
    #Find the number of test cases from the excel sheet by counting the number of rows
    File_Dir = os.path.join(BASE_DIR, 'Data', File)
    data_load = xlrd.open_workbook(File_Dir)
    data = data_load.sheet_by_name(Browser)
    return (data.nrows)

def look4_xlrd (File,Browser,search_value):
    #Find each test data value and store it a sDictionary Key-> Value pair
    File_Dir=os.path.join(BASE_DIR, 'Data', File)
    data_load = xlrd.open_workbook(File_Dir)
    data = data_load.sheet_by_name(Browser)
    #Search for the test ID match and return dict of input username, password and Output
    dic_input={}
    for i in range(0, data.nrows - 1):
        if data.cell_value(i, 0) == search_value:
           break
    for j in range(0, data.ncols):
        key_pair = data.cell_value(0, j)
        dic_input[key_pair] = data.cell_value(i, j)
    return dic_input

def read_dict(dict,key_search):
    #Read Dictionary Values
    for key,value in dict.items():
        if key == key_search:
            return dict[key]

def compare_images(image1,image2):
    #Screenshot Image comparision
    Image1=open(image1,"rb")
    Image2=open(image2,"rb")
    Ret_val=(Image1.read()==Image2.read())
    Image1.close()
    Image2.close()
    return Ret_val

def compare_warning(expected,result):
    #Test Warning Result comparision
    return(expected==result)

def Test_Report(ID,Username,Password,Result,Screenshot_Path):
    #Test Report generation on a new result file with timestamp
    res1 = "Test Case"+ID+"is executed"
    res2 = "Username:"+Username
    res3 = "Password:"+Password
    res4 = "The Test result Screen shot for the test is file:"+Screenshot_Path
    res5 = "Test has been executed and test result is:"+Result
    res6 = "--------------------------------------------------------------------"
    timestamp = datetime.datetime.now().strftime("%Y%m%d")
    DIR = os.path.join(BASE_DIR, 'Result', 'Test_Report_'+timestamp)
    with open(DIR, 'a') as out:
        out.writelines([res1,"\n",res2,"\n",res3,"\n",res4,"\n",res5,"\n",res6,"\n"])