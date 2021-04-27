# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Process {name} ')  # Press Ctrl+F8 to toggle the breakpoint.


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from tkinter import messagebox

browser = webdriver.Chrome('D:\\chromedriver.exe')
#EdgeBrowser = webdriver.Edge('D:\\msedgedriver.exe')

# Login phase
def log_into_conseroGlobal():
    browser.get('https://clientlogin.conseroglobal.com/')
    browser.set_window_size(1500, 1500,windowHandle='current')
    username = browser.find_element_by_id('username')
    username.send_keys('shalom@conseroglobal.com')
    elem = browser.find_element_by_id('password')
    elem.send_keys('#SHALOMeli1')
    elem.submit()

def search_Companies():
    browser.get('https://clientlogin.conseroglobal.com/Company/Index')
    time.sleep(5)
    delay = 10  # seconds
    try:
        myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'companyListSearch')))
        print
        "Page is ready!"
    except TimeoutException:
        print
        "Loading took too much time!"
    companyName = input("Company Name:")
    print("Username is: " + companyName)
    #user input interaction window
    import tkinter as tk

    root = tk.Tk()
    root.wm_geometry("800x600")
    dialog = tk.Toplevel(root)
    root_name = root.winfo_pathname(root.winfo_id())
    dialog_name = dialog.winfo_pathname(dialog.winfo_id())
    root.tk.eval('tk::PlaceWindow {0} widget {1}'.format(dialog_name, root_name))
    root.mainloop()
    #another user input interaction window
    import tkinter as tk
    from tkinter import simpledialog

    ROOT = tk.Tk()

    ROOT.withdraw()
    # the input dialog
    USER_INP = simpledialog.askstring(title="Test",
                                      prompt="What's the Company Name?:")

    # check it out
    print("Hello", USER_INP)





    myElem = browser.find_element_by_id('companyListSearch')
    myElem.send_keys('CompanyName')
    time.sleep(5)

def MainMethod():
    browser.get('https://clientlogin.conseroglobal.com/Company/Index')
    time.sleep(45)
    myElem = browser.find_element_by_id('companyListSearch')

    # Pop up user input interaction window requesting Company Name
    import tkinter as tk
    from tkinter import simpledialog
    ROOT = tk.Tk()
    ROOT.withdraw()
    # the input dialog
    USER_INP_CompanyName = simpledialog.askstring(title="Test",
                                      prompt="What's the Company Name?:")
    # Show CompanyName input
    print('Company selected:', USER_INP_CompanyName)

    # Search the CompanyId based on the CompanyName entered
    myElem.send_keys(USER_INP_CompanyName)
    time.sleep(5)
    CompanyId = browser.find_element_by_class_name('ag-cell-wrapper')
    print(f"CompanyName: '{USER_INP_CompanyName}', CompanyId: '{CompanyId.text}'")

    # Make sure the window has the correct size so theres no need for horizontal scrolling
    browser.set_window_size(1500, 1500, windowHandle='current')
    #browser.get(f'https://clientlogin.conseroglobal.com/Company/Details/{elem}')



    # If the button is not enabled then we need to edit the company
    #link = browser.find_element_by_link_text('Edit')
    #link.click()
    #or visit https://clientlogin.conseroglobal.com/Company/Edit?id=2323  but replacing the id with companyId


    #Add members
    link = browser.find_element_by_link_text('Details')
    link.click()

    AddMemberButton = browser.find_element_by_link_text('Add Member')
    AddMemberButton.click()

        # Select User
    UserField = browser.find_element_by_id('select2-user-container')
    UserField.click()
    searchUserField = browser.find_element_by_class_name('select2-search__field')
    searchUserField.send_keys('shalom@conseroglobal.com')

    searchUser = browser.find_element_by_class_name('select2-results__option')
    searchUser.click()
        #or
    #browser.find_element_by_id('select2-user-results').click()
        #or
    #from selenium.webdriver.common.keys import Keys
    #UserField.sendKeys(Keys.TAB);

        # Select Role
    UserField = browser.find_element_by_id('select2-role-container')
    UserField.click()
    searchUserField = browser.find_element_by_class_name('select2-search__field')
    searchUserField.send_keys('Consero - Manager')
    searchRole = browser.find_element_by_class_name('select2-results__option')
    searchRole.click()

        # Select Title
    UserField = browser.find_element_by_id('select2-roleTitle-container')
    UserField.click()
    searchUserField = browser.find_element_by_class_name('select2-search__field')
    searchUserField.send_keys('Resource')
    searchRole = browser.find_element_by_class_name('select2-results__option')
    searchRole.click()

    # Click on the 'Add' yellow Button
    submit = browser.find_element_by_id('teamMemberAdd')
    submit.click()

    #ir a ControlDock
    browser.get('https://clientlogin.conseroglobal.com/Activity/Index')

    #Client -> unselect all -> select the companyName -> CLick out of the box
        #CLick on clients
    browser.find_element_by_class_name('multiselect-selected-text').click()

        #Select all
    browser.find_element_by_class_name('multiselect-all').click()

        #Unselect all
    browser.find_element_by_class_name('multiselect-all').click()

        #Search for the CompanyName
    link = browser.find_element_by_link_text(USER_INP_CompanyName)
    link.click()

        #Click out of the box
    browser.find_element_by_class_name('activitySelectedClient').click()

    #Click on Apply Filter oragnge button
    btnFilter = browser.find_element_by_class_name('activityApplyFilterSpan')
    btnFilter.click()

    #on the Search box, type financials
    searchFilter = browser.find_element_by_xpath("//div[@id='activitiesTable_filter']/label/input[@aria-controls='activitiesTable']");
    searchFilter.send_keys('financials')

    #if status = review, we cannot see the view financial button - (We want them to be in 'In Progress' status. Otherwise we can't do much)

    #Take the Actividad id = 1400198     https://clientlogin.conseroglobal.com/Activity/Details/1400198
    #if status != progress => go to https://clientlogin.conseroglobal.com/FinancialReports/LoadStandardReportIndex?activityId=1400198&companyId=2323
    # if Intacct Validation Errors != 0 => on Variance, get the item different than 0 => get the account (number)


    #=========================================   DB  ===========================================================
    # Go to DB with that Account number and return the amount (acumulado de esa cuenta para el mes en curso)

    # ======================================  INTACCT ===========================================================
    # Go to intact con el rango de la fecha y account number (1400198)
    # https://www.intacct.com/ia/acct/frameset.phtml?.sess=AJxHs50-9USRDQRQRmB_sDdsRJANBA..&.cc=RaQslWQXvAEgzxFDvNhkfE4dhd-p004ui9fZgIV0hDQ.
    # Go to Applications => my Practice => Clients/Entities => Flat View button click =>
    # Go simple then go to Companies => find the company name => Edit
    # In Intacct.com Settings , get the 'Company ID" and 'Entity ID'
    # Go back to intacct and enter the companyId hit enter/search
    # Enter the EntityID and hit enter/search
    #click on 'Switch to client' ignore the sandbox option at the end
    #On the new tab, go to Applications => General Ledger (make sure it's set to "All" instead of "Setup")=> General ledger
    # set 'Start date' and 'End date' 03/01/2021 to today's date 04/21/2021
    #On Filters => set 'Account from' with error 68000 if intacct errors != 0
    #On Format, make sure the 'Show zero balance accounts' is set to 'Only with activity' radio button
    # click on the upper right side button named "View"
    #IF And alert pops up, click "OK"
    # wait, it might take up to 30 sec
    # Compare the "Debit" and "Credit" amounts from this website (buttom 'Grand Total') with the ones in return from DB
    # SELECT DebitAmount, CreditAmount FROM GLDETAILSDDSDATAS WHERE GlAccountNumber IN (68000) AND
    # glpostingdate BETWEEN '03/01/2021' AND '04/21/2021' AND IsDeleted=0




    # click on (GenerateValidate and Review Financial  =>  https://clientlogin.conseroglobal.com/Activity/Details/1421502

    # wait.until(EC.presence_of_element_located((By.XPATH, xpath_value))).send_keys(Keys.RETURN)


def SIMPL_Access():
    browser.get('https://clientlogin.conseroglobal.com/Home/ClientPortalOverview')
    time.sleep(5)

def ControlDock_ActivityList():
    browser.get('https://clientlogin.conseroglobal.com/Activity/Index')
    time.sleep(7)
    browser.find_element_by_xpath("//select[@name='SelectedKickOffMonth']/option[text()='2021-4']").click()
    time.sleep(5)

def list_Companies():
    #elem = browser.find_element_by_class_name('ag-center-cols-container')
    bol1 =  messagebox.askquestion("Title", "askquestion")
    messagebox.showinfo("Title", f'ans is {bol1}')

    bol2 = messagebox.askokcancel("Title", "askokcancel")
    messagebox.showwarning("Title", f"showwarning {bol2}")

    bol3 = messagebox.askyesno("Title", "askyesno")
    messagebox.showerror("Title", f"showerror {bol3}")

    n =  messagebox.askretrycancel("Title", "askretrycancel")
    n

def close_Browser():
    time.sleep(5)
    browser.quit()

def interactive_Financials():
    browser.get('https://clientlogin.conseroglobal.com/Home/ClientPortalOverview')
    time.sleep(5)
    link = browser.find_element_by_link_text('Interactive Financials')
    link.click()
    time.sleep(5)
    link = browser.find_element_by_link_text('Sales')
    link.click()
    time.sleep(5)
    elem = browser.find_element_by_class_name('dataTables_scrollBody')

    table_id = browser.find_element_by_id('nlrTable1_wrapper')
    rows = table_id.find_element_by_tag_name("tr")  # get all of the rows in the table
    for row in rows:
        # Get the columns (all the column 2)
        col = row.find_element_by_tag_name("td")[1]  # note: index start from 0, 1 is col 2
        print
        col.text  # prints text from the element


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    log_into_conseroGlobal()
    MainMethod()
    #search_Companies()
    #SIMPL_Access()
    #ControlDock_ActivityList()
    #interactive_Financials()
    #list_Companies()
    #close_Browser()
    print_hi('Completed')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/