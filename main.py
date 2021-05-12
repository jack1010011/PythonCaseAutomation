# This is a sample Pythcript.

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
from tkinter import messagebox, Button, Label

def Navegation():
    browser.set_window_size(1500, 1500, windowHandle='current')
    phase[0] = 0
    phase[1] = "Navigation Initiation "
    phase[2] = "Authentication"

def timeManager(seconds):
    import time as t
    for i in range(seconds):
        print(str(seconds - i) + " seconds remaining \n")
    t.sleep(1)
    print("Time is up")

def conseroGlobalAuth():

    browser.get('https://clientlogin.conseroglobal.com/')
    browser.find_element_by_id('username').send_keys('shalom@conseroglobal.com')
    elem = browser.find_element_by_id('password')
    elem.send_keys('#SHALOMeli1')
    elem.submit()

    phase[0] = 0
    phase[1] = "Authentication"
    phase[2] = "Search CompanyName Details"
    print_hi(f' - Phase {phase[0]} - {phase[1]} - Completed!')

def get_CompanyID():
    #                       PHASE 1 (Search CompanyName Details)
    browser.get('https://clientlogin.conseroglobal.com/Company/Index')

    #Wait Element to show
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as ec
    # myElem = browser.find_element_by_id('companyListSearch')
    try:
        myElem = WebDriverWait(browser, 60).until( ec.visibility_of_element_located((By.ID, 'companyListSearch')))
    except:
        print(f"Item didn't load. Re-attempting... ")
        get_CompanyID()
        pass
    print(f" Item Loaded! ")

    # Pop up user input interaction window requesting Company Name
    import tkinter as tk
    from tkinter import simpledialog
    ROOT = tk.Tk()
    ROOT.withdraw()
    # the input dialog
    USER_INP_CompanyName = simpledialog.askstring(title="Test", prompt="What's the Company Name?:")

    CompanyName = USER_INP_CompanyName.rstrip().lstrip()

    # Search the CompanyId based on the CompanyName entered
    myElem.send_keys(CompanyName)

    #CompanyIdEle = browser.find_element_by_class_name('ag-cell-wrapper')
    CompanyIdEle = WebDriverWait(browser, 60).until(ec.visibility_of_element_located((By.CLASS_NAME, 'ag-cell-wrapper')))
    CompanyId = CompanyIdEle.text

    #time.sleep(5)

    #print(f"CompanyName: '{CompanyName}', CompanyId: '{CompanyId}'")
    Company.Id = CompanyId
    setattr(Company, "Name", CompanyName)


    phase[0] = 1
    phase[1] = "Search CompanyName Details"
    phase[2] = "Add members"
    print_hi(f' - Phase {phase[0]} - {phase[1]} - Completed!')

    #browser.get(f'https://clientlogin.conseroglobal.com/Company/Details/{elem}')

    # If the button is not enabled then we need to edit the company
    #link = browser.find_element_by_link_text('Edit')
    #link.click()
    #or visit https://clientlogin.conseroglobal.com/Company/Edit?id=2323  but replacing the id with companyId

def addMembers():
    #                       PHASE 2 (Add members)
    browser.find_element_by_link_text('Details').click()
    browser.find_element_by_link_text('Add Member').click()
    user = 'shalom@conseroglobal.com'

    try:
        # Select User
        browser.find_element_by_id('select2-user-container').click()
        browser.find_element_by_class_name('select2-search__field').send_keys(user)
        browser.find_element_by_class_name('select2-results__option').click()

        # Select Role
        browser.find_element_by_id('select2-role-container').click()
        browser.find_element_by_class_name('select2-search__field').send_keys('Consero - Manager')
        browser.find_element_by_class_name('select2-results__option').click()

        # Select Title
        browser.find_element_by_id('select2-roleTitle-container').click()
        browser.find_element_by_class_name('select2-search__field').send_keys('Resource')
        browser.find_element_by_class_name('select2-results__option').click()

        # Click on the 'Add' yellow Button
        browser.find_element_by_id('teamMemberAdd').click()
    except:
        print(f'Skip adding. "{user}" is already a Team member for "{Company.Name}".')
        messagebox.showinfo("User is Already a member for this company.Skip ", f'{user} is already a member of {Company.Name}.')
        pass


    phase[0] = 2
    phase[1] = "Add members"
    phase[2] = "Filtering CompanyName & CompanyID Details"
    print_hi(f' - Phase {phase[0]} - {phase[1]} - Completed!')

def get_CompanyID_from_CompanyName():
    #                       PHASE 3 Filtering CompanyName & CompanyID Details

    #ir a ControlDock
    browser.get('https://clientlogin.conseroglobal.com/Activity/Index')

    #Client -> unselect all -> select the companyName -> CLick out of the box
    #CLick on clients
    #import wait
    #wait.until(browser.presence_of_element_located((By.__class__, 'multiselect-selected-text')))

    time.sleep(5)
    # browser.find_element_by_class_name('multiselect-selected-text').click()
    # Wait Element to show
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as ec

    # myElem = browser.find_element_by_class_name('multiselect-selected-text')
    myElem = WebDriverWait(browser, 60).until(ec.visibility_of_element_located((By.CLASS_NAME, 'multiselect-selected-text')))
    print(f" Item Loaded! ")
    myElem.click()


    #Select all
    # browser.find_element_by_class_name('multiselect-all').click()
    myElem = WebDriverWait(browser, 60).until(ec.visibility_of_element_located((By.CLASS_NAME, 'multiselect-all')))
    print(f" Item Loaded! ")
    myElem.click()


    #Unselect all
    #browser.find_element_by_class_name('multiselect-all').click()
    myElem = WebDriverWait(browser, 60).until(ec.visibility_of_element_located((By.CLASS_NAME, 'multiselect-all')))
    print(f" Item Loaded! ")
    myElem.click()


        #Search for the CompanyName
    #link = browser.find_element_by_link_text(Company.Name)
    link = WebDriverWait(browser, 60).until(ec.visibility_of_element_located((By.LINK_TEXT, Company.Name)))
    print(f" Item Loaded! ")
    link.click()

        #Click out of the box
    browser.find_element_by_class_name('activitySelectedClient').click()

    time.sleep(5)
    #Click on Apply Filter oragnge button
    btnFilter = browser.find_element_by_class_name('activityApplyFilterSpan')
    btnFilter.click()

    time.sleep(5)
    #on the Search box, type financials
    searchFilter = browser.find_element_by_xpath("//div[@id='activitiesTable_filter']/label/input[@aria-controls='activitiesTable']");
    searchFilter.send_keys('financials')
    time.sleep(2)


    phase[0] = 3
    phase[1] = "Filtering CompanyName & CompanyID Details"
    phase[2] = "Confirm the Status of the ActivityId"
    print_hi(f' - Phase {phase[0]} - {phase[1]} - Completed!')

def get_activityId_status(ActivityId):
    #                       PHASE 4 Confirm the Status of the ActivityId

    #if status = review, we cannot see the view financial button - (We want them to be in 'In Progress' status. Otherwise we can't do much)

    #Take the Actividad id = 1400198     https://clientlogin.conseroglobal.com/Activity/Details/1400198
    #if status != progress => go to https://clientlogin.conseroglobal.com/FinancialReports/LoadStandardReportIndex?activityId=1400198&companyId=2323
    # if Intacct Validation Errors != 0 => on Variance, get the item different than 0 => get the account (number)
    phase[0] = 4
    phase[1] = "Confirm the Status of the ActivityId"
    phase[2] = "DB Query to retrieve Debit and Credit values"
    print_hi(f' - Phase {phase[0]} - {phase[1]} - Completed!')

    return ActivityId

def DefaultDateRange():

    # Set Default Date
    import datetime
    today = f'{datetime.date.today().month}/{datetime.date.today().day}/{datetime.date.today().year}'
    StartDate = f'{datetime.date.today().month - 1}/{1}/{datetime.date.today().year}'
    EndDate = f'{datetime.date.today().month - 1}/{30}/{datetime.date.today().year}'
    setattr(Company, "StartDate", StartDate)
    setattr(Company, "EndDate", EndDate)

    UseDefaultDateRange = messagebox.askyesno('Continue with default range date?', f'From {StartDate} to {EndDate}')
    if UseDefaultDateRange:
        Company.EndDate = EndDate
        return (StartDate, EndDate)
    else:
        UseDefaultDateRange = messagebox.askyesno('Continue with recommended range date?',
                                                  f'From {StartDate} to {today}')
        if UseDefaultDateRange:
            Company.EndDate = today
            return (StartDate, today)
        else:
            UpdateDateRange()

def UpdateDateRange():
    import tkcalendar as calendar
    import tkinter.messagebox

    root = tkinter.Tk()
    root.title('Codemy.com')
    #root.iconbitmap('c:/gui/codemy.ico')
    root.geometry("400x800")

    from_label = Label(root, text="From")
    from_label.pack()

    cal = calendar.Calendar(root)
    cal.pack(pady=20)

    to_label = Label(root, text="To")
    to_label.pack()

    cal2 = calendar.Calendar(root)
    cal2.pack(pady=20)

    my_label = Label(root, text="")
    my_label.pack(pady=20)
    my_label.config(text='')

    def onClick():
        Company.StartDate = cal.get_date()
        Company.EndDate = cal2.get_date()
        my_label.config(text=f'From {Company.StartDate} to {Company.EndDate}')


    def onClickExit():
        root.destroy()
        root.quit()

    button = tkinter.Button(root, text="Update", command=onClick)
    button.pack()

    buttonExit = tkinter.Button(root, text="Continue", command=onClickExit)
    buttonExit.pack(pady=10)

    root.mainloop()

    phase[0] = 4
    phase[1] = "Set Date Range"
    phase[2] = "DB Query to retrieve Debit and Credit values"
    print_hi(f' - Phase {phase[0]} - {phase[1]} - Completed!')

def get_Debit_and_Credit_DB():
    #                       PHASE 5 DB Query (to retrieve the "Debit" and "Credit" values
    # Go to DB with that Account number and return the amount (acumulado de esa cuenta para el mes en curso)
    # Reference =>  https://docs.microsoft.com/en-us/azure/azure-sql/database/connect-query-python#create-code-to-query-your-database

    import pyodbc
    server = 'jvtmcg7krk.database.windows.net'
    database = f'consero-prod-{Company.Id}'
    username = 'conThinkSupport'
    password = 'C0n$ero@l0ckDown_469'
    driver = '{ODBC Driver 17 for SQL Server}'
    startDate = Company.StartDate
    endDate = Company.EndDate
    CreditTotal = 0
    DebitTotal = 0

    with pyodbc.connect(
            'DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password) as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                f"SELECT DebitAmount, CreditAmount FROM [{database}].[dbo].[GLDETAILSDDSDATAS] WHERE GlAccountNumber IN (68000) AND glpostingdate BETWEEN '{startDate}' AND '{endDate}' AND IsDeleted=0")
            row = cursor.fetchone()
            while row:
                print(str(row[0]) + " " + str(row[1]))
                CreditTotal += int(row[0])
                DebitTotal += int(row[0])
                row = cursor.fetchone()

    setattr(Company, "Debit", DebitTotal)
    setattr(Company, "Credit", CreditTotal)


    phase[0] = 5
    phase[1] = 'DB Query to retrieve Debit and Credit values'
    phase[2] = "Go to Intacct and compare the Debit and Credit values"
    print_hi(f' - Phase {phase[0]} - {phase[1]} - Completed!')

def get_Debit_and_Credit_Intacct():

    #                       PHASE 6 Go to Intacct and compare the "Debit" and "Credit" values

    # Go to intact con el rango de la fecha y account number (1400198)
    EdgeBrowser = webdriver.Edge('D:\\msedgedriver.exe')
    EdgeBrowser.get('https://www.intacct.com/ia/acct/frameset.phtml?.sess=AJxHs50-9USRDQRQRmB_sDdsRJANBA..&.cc=RaQslWQXvAEgzxFDvNhkfE4dhd-p004ui9fZgIV0hDQ.')
    time.sleep(10)
    EdgeBrowser.find_element_by_id('company').send_keys('consero')
    EdgeBrowser.find_element_by_id('login').send_keys('shalom')
    EdgeBrowser.find_element_by_id('passwd').send_keys('16I@Jma1KBk1')
    EdgeBrowser.find_element_by_id('retbutton').click()

    # Pop up user input interaction window requesting Company Name
    import tkinter as tk
    from tkinter import simpledialog
    ROOT = tk.Tk()
    ROOT.withdraw()
    # the input dialog
    USER_INP_VerificationCode = simpledialog.askstring(title="Test",prompt="Enter the verification code:")

    EdgeBrowser.find_element_by_id('verify_code').send_keys(USER_INP_VerificationCode)
    EdgeBrowser.find_element_by_id('verify_button').click()

    ele = EdgeBrowser.find_element_by_xpath("//input[@class='mfa_green_button notrust_settrust_button']");
    ele.click()
    time.sleep(10)
    EdgeBrowser.set_window_size(1500, 1500, windowHandle='current')


    clientMenu = EdgeBrowser.find_element_by_class_name('input-group-addon dropdown-toggle')


    try:
        clientMenu = EdgeBrowser.find_element_by_id('_spickent') # n
        clientMenu = EdgeBrowser.find_element_by_class_name('input-group') # n
        clientMenu = EdgeBrowser.find_element_by_id('.pickent') # n
        clientMenu = EdgeBrowser.find_element_by_name('.pickent') # n
        clientMenu = EdgeBrowser.find_element_by_id('span_.pickent') # n
        clientMenu = EdgeBrowser.find_element_by_class_name('input-group-addon dropdown-toggle') # n
        ele = EdgeBrowser.find_element_by_xpath("//span[@id='input-group-addon dropdown-toggle']"); # n
        ele = EdgeBrowser.find_element_by_xpath("//span[@id='span_.pickent']"); # n
        clientMenu = EdgeBrowser.find_element_by_class_name('qx-icon fa fa-angle-down') # n
        ele = EdgeBrowser.find_element_by_link_text('5 Star') # n

        ele = EdgeBrowser.find_element_by_xpath("//input[@class='form-control']")  # maso
        ele = EdgeBrowser.find_element_by_class_name('form-control')  # maso
        ele = EdgeBrowser.find_element_by_xpath("//i[@class='qx-icon fa fa-angle-down']")  # maso
        ele = EdgeBrowser.find_element_by_css_selector("input[type='text']") # maso
        ele = EdgeBrowser.find_element_by_css_selector("input#[@id='.pickent']")

        ele = EdgeBrowser.find_element_by_id('_cpickentlst')# n
        ele = EdgeBrowser.find_element_by_class_name('baseIconArrowDown') # n
        ele = EdgeBrowser.find_element_by_xpath("//select[@id='_cpickentsel']") #n
        ele = EdgeBrowser.find_element_by_xpath("//div[@class='dashboard_container_bottom_div']")  # n
        ele = EdgeBrowser.find_element_by_class_name('comp_holder dashboard_transparentbackground')

        from selenium.webdriver.support.select import Select
        s2 = Select(EdgeBrowser.find_element_by_id('_cpickentsel'))
        s2.select_by_value('5 Star')
        # '5 Star'

        ele = EdgeBrowser.find_element_by_xpath("//i[@class='qx-icon fa fa-angle-down']")

        ele = EdgeBrowser.find_elements_by_tag_name('tag-name')[0]
        EdgeBrowser.switch_to.frame(ele)
        EdgeBrowser.switch_to.__class__('form-control')

        from selenium.webdriver.common.keys import Keys
        from selenium.webdriver.common.action_chains import ActionChains
        actions = ActionChains(EdgeBrowser)
        actions.send_keys(Keys.TAB * 12)
        actions.perform()

        x = EdgeBrowser.find_element_by_link_text("Welcome Everyone").send_keys(Keys.NULL)
        search = ele.find_element_by_tag_name("input")

        ele.send_keys(Keys.ARROW_DOWN)
        ele =  EdgeBrowser.find_element_by_xpath("//label[text='Client']")
    except:
        pass

    phase[0] = 6
    phase[1] = 'Go to Intacct and compare Debit and Credit values'
    phase[2] = "Phase 10 Close Tool"
    print_hi(f' - Phase {phase[0]} - {phase[1]} - Completed!')


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

def list_Companies():
    #elem = browser.find_element_by_class_name('ag-center-cols-container')
    bol1 = messagebox.askquestion("Title", "askquestion")
    messagebox.showinfo("Title", f'ans is {bol1}')

    bol2 = messagebox.askokcancel("Title", "askokcancel")
    messagebox.showwarning("Title", f"showwarning {bol2}")

    bol3 = messagebox.askyesno("Title", "askyesno")
    messagebox.showerror("Title", f"showerror {bol3}")

    n =  messagebox.askretrycancel("Title", "askretrycancel")
    messagebox.showerror("Title", f"showerror {n}")

    table_id = browser.find_element_by_id('nlrTable1_wrapper')
    rows = table_id.find_element_by_tag_name("tr")  # get all of the rows in the table
    for row in rows:
        # Get the columns (all the column 2)
        col = row.find_element_by_tag_name("td")[1]  # note: index start from 0, 1 is col 2
        print
        col.text  # prints text from the element

def close_Browser():
    # Phase 10 Close Tool
    browser.close()


def wrapUp ():
    output = messagebox.askokcancel("Title", f"Phase {phase[0]}: {phase[1]} Completed. Continue with Phase {phase[0] + 1}?")
    if (output == True):
        print(f'Phase {phase} started! ')
        True
        print(f'Phase {phase} Finished! ')
    else:
        False
    return

def confirm_Next():
    output = messagebox.askokcancel("Completed!",f"{phase[1]} Completed!\nPhase {phase[0]} DONE! "
                                                 f"\n\nStart Phase {phase[0] + 1} \n{phase[2]} ?")

    if (output == True):
        print(f'Phase {phase[0]} started! ')
        return True
    else:
        print(f'Phase {phase[0]} discarted with error ', output)
        False



class Company():
	def __init__(self):
		self.Name = "Id"

	def newAttr(self, attr):
		setattr(self, attr, attr)
Company = Company()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # constructor
    phase = [0, "",""]
    phase[1] = ''
    phase[2] = ''

    # Navegation
    browser = webdriver.Chrome('D:\\chromedriver.exe')
    Navegation()

    # Authentication
    # conseroGlobalAuth()
    if confirm_Next():
        conseroGlobalAuth()

    # PHASE 1 (Search CompanyName Details)
    # get_CompanyNameDetails()
    if confirm_Next():
        get_CompanyID()
        print(f"CompanyName: '{Company.Name}', CompanyId: '{Company.Id}'")

    # PHASE 2 (Add members)
    # addMembers()
    if confirm_Next():
        addMembers()

    # PHASE 3 Filtering CompanyName & CompanyID Details
    # get_CompanyID_from_CompanyName()
    if confirm_Next():
        get_CompanyID_from_CompanyName()


    # PHASE 4 Confirm the Status of the ActivityId
    # get_activityId_status(ActivityId):
    output = messagebox.askokcancel("Title", f"Phase {phase[0]}: {phase[1]}  - Completed. Continue with Phase {phase[0] + 1}?")
    if confirm_Next():
        get_activityId_status("ActivityId")

    # Get Default Date Range
    if confirm_Next():
        DateRange = DefaultDateRange()
        print(f'Selected date from {Company.StartDate} to {Company.EndDate}')


    # PHASE 5 DB Query (to retrieve the "Debit" and "Credit" values
    # get_Debit_and_Credit_DB(CompanyId)
    if confirm_Next():
        get_Debit_and_Credit_DB()
        messagebox.showinfo(f'{Company.Id} - {Company.Name} ', f'DebitAmount    = {Company.Debit} '
                                                             f'\nCreditAmount   = {Company.Credit}'
                                                             f'\nDo they match? =  {Company.Credit == Company.Debit}'

                                                           f'\n\nFrom {Company.StartDate} to {Company.EndDate}')


    # Phase 10 Close Tool
    if confirm_Next():
        close_Browser()

    browser.close()
    browser.quit()
    print_hi('Completed with no errors! ')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
