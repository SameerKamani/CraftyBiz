# Importing essential modules
import typing
from PyQt6 import QtCore, QtWidgets, uic
from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QHeaderView
import sys
import pyodbc

# Replace these with your own database connection details
server = ''
database = ''  # Name of your Northwind database
use_windows_authentication = False  # Set to True to use Windows Authentication
username = ''  # Specify a username if not using Windows Authentication
password = ''  # Specify a password if not using Windows Authentication

# Create the connection string based on the authentication method chosen
if use_windows_authentication:
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
else:
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

# MAIN
class UI(QtWidgets.QMainWindow):
    def __init__(self):
        # Call the inherited classes __init__ method
        super(UI, self).__init__()

        # Load the .ui file
        uic.loadUi('Screens/1 User Type.ui', self)
        self.setWindowTitle("Select Login Type")
        
        self.loginAdmin.clicked.connect(lambda: self.open_Login('Employee'))
        self.loginSupplier.clicked.connect(lambda: self.open_Login('Supplier'))
        self.loginCustomer.clicked.connect(lambda: self.open_Login('Customer'))
        self.createAccount.clicked.connect(self.open_createAccountForm)
        # self.openLogin(self.type)
    def open_Login(self, type):
        self.loginDialog = Login(type)
        self.loginDialog.show()

    def open_createAccountForm(self):
        self.createDialog = CreateAccount()
        self.createDialog.show()

# LOGIN
class Login(QtWidgets.QMainWindow):
    def __init__(self, typ):
        self.type = typ
        # Call the inherited classes __init__ method
        super(Login, self).__init__()

        # Load the .ui file
        uic.loadUi('Screens/3 Login screen.ui', self)
        # self.password_line_edit.setEchoMode(QWidgets.QLineEdit.Password)
        # Connect Submit Button to Event Handling Code
        self.logInButton.clicked.connect(self.logIn)
        self.createAccount.clicked.connect(self.open_createAccountForm)

    def logIn(self):
        id = self.userId.text()
        password = self.password.text()
        user_type = self.type

        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        q = "SELECT * FROM Registrations WHERE id = ? AND Password = ? AND User_Type = ?"
        cursor.execute(q, (id, password, user_type))
        row = cursor.fetchone() 
        if row:
            if user_type == 'Employee':
                self.open_adminDashboard(id)
            elif user_type == 'Distributor':
                self.open_distributorDashboard()
            elif user_type == 'Supplier':
                self.open_supplierDashboard(id)
            elif user_type == 'Customer':
                self.open_customerDashboard(id)
        else:
            QtWidgets.QMessageBox.warning(self, "Login Failed", "Invalid username or password. Please try again.")
        
        connection.close()

    def open_createAccountForm(self):
        self.createDialog = CreateAccount()
        self.createDialog.show()
        self.close()

    def open_adminDashboard(self, current_id):
        self.startAdmin = AdminDashboard(current_id)
        self.startAdmin.show()
        self.close()

    def open_customerDashboard(self, current_id):
        self.startCustomerView = CustomerDashboard(current_id)
        self.startCustomerView.show()
        self.close()

    def open_supplierDashboard(self, current_id):
        # TODO Supplier HERE
        self.startSupplierView = SupplierDashboard(current_id)
        self.startSupplierView.show()
        self.close()


    
    

# CREATE ACCOUNT
class CreateAccount(QtWidgets.QMainWindow):
    def __init__(self):
        super(CreateAccount, self).__init__()

        uic.loadUi('Screens/2 Sign up.ui', self)
        self.setWindowTitle("Create Account")

        self.createAccount_button.clicked.connect(self.insertCreate)
        self.cancel.clicked.connect(self.closeCreate)

    def insertCreate(self):
        name = self.name.text()
        phoneNum = self.phoneNum.text()
        address = self.address.toPlainText()
        userType = self.userType.currentText()
        email = self.email.text()
        password = self.password.text()
        reEnterPassword = self.reEnterPassword.text()

        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        if password == reEnterPassword:
            #Inserted in Registrations
            sql_query_registrations = """
            INSERT INTO Registrations ([Password], [User_Type]) 
            VALUES (?, ?)
            """

            # Execute the SQL query with parameter values
            cursor.execute(sql_query_registrations, (password, userType))
            connection.commit()

            # Getting Registration
            latest = "SELECT IDENT_CURRENT('Registrations')"
            cursor.execute(latest)
            latest_id_into_registration = cursor.fetchone()[0]
            print(latest_id_into_registration)

            #Insert In Others
            if userType == 'Customer':
                activity_status = 'Active'
                sql_query_customers = "INSERT INTO Customers ([customer_id], [customer_name], [address], [phone_number], [email], [activity_status]) VALUES (?, ?, ?, ?, ?, ?)"
                cursor.execute(sql_query_customers, (int(latest_id_into_registration), name, address, phoneNum, email, activity_status))
                connection.commit()
                QtWidgets.QMessageBox.information(self, "Success", f"The registration was successful. Your {userType} id is {latest_id_into_registration}.")
        else:
            QtWidgets.QMessageBox.warning(self, "Password Error", "The Two password don't Match")

        connection.close()

    def closeCreate(self):
        self.close()

class AdminDashboard (QtWidgets.QMainWindow):
    def __init__(self, current_id):
        self.current_id = current_id
        # Call the inherited classes __init__ method
        super(AdminDashboard, self).__init__()

        # Load the .ui file
        uic.loadUi('Screens/4 Admin dashboard.ui', self)

        self.productView.clicked.connect(self.open_productView)
        # self.inventoryView.clicked.connect(self.open_inventoryView)
        self.rawMaterialView.clicked.connect(self.open_rawmatView)
        # self.orderView.clicked.connect(self.open_orderView)
        # self.distributorView.clicked.connect(self.open_distributorView)
        self.manufactureProduct.clicked.connect(self.open_manufactureView)
        self.supplierView.clicked.connect(self.open_supplierView)
        self.exitDatabase.clicked.connect(self.open_exitDatabase)
        # print(self.current_id)
        self.customerView.clicked.connect(lambda: self.open_customerView(current_id))
        self.currentOrders.clicked.connect(lambda: self.open_currentOrders(current_id))
        #TODO: Add a functionality such that Admin can view the customers Feedback!!
    def open_productView(self):
        self.startProductView = AdminProductView()
        self.startProductView.show()
    #     pass
    # def open_inventoryView(self):
    #     pass
    def open_rawmatView(self):
        self.adminraw = AdminRawMaterial()
        self.adminraw.show()
    # def open_distributorView(self):
    #     pass
    def open_manufactureView(self):
        self.startManufacturingView = ManufacturingViewProducts()
        self.startManufacturingView.show()

    def open_supplierView(self):
        # print("h")
        self.adminSupp = AdminSupplierView()
        self.adminSupp.show()
    def open_customerView(self, current_id):
        self.CustView = AdminCustomerView()
        self.CustView.show()
    def open_exitDatabase(self):
        # QCoreApplication.instance().quit()
        self.close()

    def open_currentOrders(self, current_id):
        self.startCurrentOrders = CurrentOrders(current_id)
        self.startCurrentOrders.show()


###########################
class AdminProductView (QtWidgets.QMainWindow):
    def __init__(self):
        # self.current_id = current_id
        # Call the inherited classes __init__ method
        super(AdminProductView, self).__init__()

        # Load the .ui file
        uic.loadUi('Screens/5 Admin Product Button.ui', self)
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        prods = "select P.product_id, P.product_name, C.category_name, P.price from products P inner Join Category C on P.category_id = C.category_id"
        cursor.execute(prods)

        for row_index, row_data in enumerate(cursor.fetchall()):
            self.booksTableWidget.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.booksTableWidget.setItem(row_index, col_index, item)

        prod_name = "select product_name from products"
        cursor.execute(prod_name)
        # names =  list(cursor.fetchall())
        names = [row.product_name for row in cursor.fetchall()]
        # print(names)
        self.categoryCombo.addItems(names)

        cat_name = "select category_name from Category"
        cursor.execute(cat_name)
        # names =  list(cursor.fetchall())
        names = [row.category_name for row in cursor.fetchall()]
        # print(names)
        self.catcombo.addItems(names)

        self.searchButton.clicked.connect(self.searchClicked)
        self.viewButton.clicked.connect(self.viewMaterial_clicked)
        self.closeButton.clicked.connect(self.closeButton_clicked)
        self.addButton.clicked.connect(self.addButton_clicked)

    def addButton_clicked(self):
        self.startAddProduct = AddProduct()
        self.startAddProduct.show()

    def viewMaterial_clicked(self, current_id):
        selected_row = self.booksTableWidget.currentRow()
        if selected_row >= 0:
            material_id = self.booksTableWidget.item(selected_row, 0).text()
            material_name = self.booksTableWidget.item(selected_row, 1).text()
            categorys_name = self.booksTableWidget.item(selected_row, 2).text()
            cost = self.booksTableWidget.item(selected_row, 3).text()
            
            self.view_prod_details = viewProductDetails(material_id, material_name, categorys_name, cost)
            self.view_prod_details.show()
    def closeButton_clicked(self):
        self.close()
    def searchClicked(self):
        prod_name = self.categoryCombo.currentText()
        price = self.price.text()
        cat_name = self.catcombo.currentText()
        #for activity status
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        prods = "select product_name from products"
        cursor.execute(prods)
        for row_index in range(self.booksTableWidget.rowCount()):
                row_hidden = True  # Assume the row will be hidden, unless a match is found

                if prod_name and self.booksTableWidget.item(row_index, 1).text() == prod_name:
                    row_hidden = False

                if price and self.booksTableWidget.item(row_index, 3).text() == price:
                    row_hidden = False

                if cat_name and self.booksTableWidget.item(row_index, 2).text() == cat_name:
                    row_hidden = False

                self.booksTableWidget.setRowHidden(row_index, row_hidden)

class AddProduct (QtWidgets.QMainWindow):
    def __init__(self):
        # self.current_id = current_id
        # Call the inherited classes __init__ method
        super(AddProduct, self).__init__()

        # Load the .ui file
        uic.loadUi('Screens/7 Add Products.ui', self)
        
        self.add.clicked.connect(self.openAdd)
        self.cancel.clicked.connect(self.openCloseButton)
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        fetchCategories = "SELECT Category_name from Category"
        cursor.execute(fetchCategories)

        for row_data in cursor.fetchall():
            for cell_data in row_data:
                self.category.addItem(str(cell_data))
        # addMaterial = "INSERT INTO RAW_MAterial ()"

    def openCloseButton(self):
        self.close()
    def openAdd(self):
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        product_name = self.product_name.text()
        category_name = self.category.text()
        cost = round(float(self.price.text()),2)

        getCategoryid = "SELECT Category_id from Cateogry where category_name = ?"
        cursor.execute(getCategoryid, category_name)
        category_id = cursor.fetchone()[0]
        # conintu = self.quality_metric.text()
        addProduct = "INSERT INTO Products (product_name, category_id, price, continuity_status) VALUES (?, ?, ?, True)"
        latest = "SELECT IDENT_CURRENT('Products')"
        insertProductStock = "INSERT INTO Product_INventory (Product_id, warehouse_id, product_stock) VALUES (?, 2, 0)"

        # addMaterial = "INSERT INTO RAW_Material (material_name, supplier_id, cost, quality_metric) VALUES (?, ?, ?, ?)"
        # latest = "SELECT IDENT_CURRENT('Raw_Material')"
        # insertMaterialStock = "INSERT INTO Material_Inventory (material_id, warehouse_id, material_stock) VALUES (?, 1, 0)"
        cursor.execute(addProduct, product_name, category_id, cost)
        # cursor.execute(addMaterial, material_name, supplier_id, cost, quality_metric)
        cursor.commit()

        cursor.execute(latest)
        latest_id = cursor.fetchone()[0]
        print(latest_id)

        cursor.execute(insertProductStock, latest_id)

class viewProductDetails (QtWidgets.QMainWindow):
    def __init__(self, product_id, prod_name, categorys_name, cost):
        # self.current_id = current_id
        # Call the inherited classes __init__ method
        super(viewProductDetails, self).__init__()

        # Load the .ui file
        uic.loadUi('Screens/30 Customer View Products.ui', self)
        self.name.setText(prod_name)
        self.category.setText(categorys_name)
        self.price.setText(cost)
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        self.closeButton.clicked.connect(self.closeButton_clicked)


        fetchCustomerName = "SELECT continuity_status from products where product_id = ?"
        cursor.execute(fetchCustomerName, product_id)
        row = cursor.fetchone()
        status = str(row.continuity_status)
        # print(status)
        if status:
            self.cont_stat.setChecked(True) 
        else:
            self.cont_stat.setChecked(False) 
        # price = float(cursor.fetchone())
        # print(price)
        # price = float(row.price)
        # print(price)
        # cost = price
        fetchCustomerName = "select M.material_name from Raw_Material M inner join Products_RawMaterial PR on M.material_id = PR.material_id where PR.product_id = ?;"
        cursor.execute(fetchCustomerName, product_id)
        # row = cursor.fetchall()
        # print(row)
        rows = cursor.fetchall()
        self.populate_table(rows)

    def populate_table(self, rows):
        # Assuming you have a QTableWidget named self.tableWidget
        self.booksTableWidget.setColumnCount(1)  # Set the number of columns
        self.booksTableWidget.setRowCount(len(rows))  # Set the number of rows

        for row_index, row_data in enumerate(rows):
            item = QTableWidgetItem(str(row_data.material_name))
            self.booksTableWidget.setItem(row_index, 0, item)

        
    def closeButton_clicked(self):
        self.close()

##################################3

class AdminCustomerView (QtWidgets.QMainWindow):
    def __init__(self):
        # Call the inherited classes __init__ method
        super(AdminCustomerView, self).__init__()

        uic.loadUi('Screens/23 Customer Button.ui', self)
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        fillSupplierComboBox = "SELECT customer_name from Customers"
        cursor.execute(fillSupplierComboBox)

        for row_data in cursor.fetchall():
            for cell_data in row_data:
                self.customer_name.addItem(str(cell_data))

        all_cust = "select * from Customers"
        cursor.execute(all_cust)

        for row_index, row_data in enumerate(cursor.fetchall()):
            self.booksTableWidget.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.booksTableWidget.setItem(row_index, col_index, item)

        self.searchButton.clicked.connect(self.adminSearchcust)
        self.cust_view.clicked.connect(self.adminCustview)
        self.closeButton.clicked.connect(self.closeButtonClicked)
        self.changeActivityStatus.clicked.connect(self.changeActivityStatusfunc)

        connection.close()

    def changeActivityStatusfunc(self):
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        # selected_items = self.pendingOrderTable.selectedItems()

        selected_items = self.booksTableWidget.selectedItems()

        if len(selected_items) > 0:
            selected_item = selected_items[0]
            selected_row = selected_item.row()

            # Get all items in the selected row
            row_items = []
            for col in range(self.booksTableWidget.columnCount()):
                item = self.booksTableWidget.item(selected_row, col)
                if item is not None:
                    row_items.append(item.text())

            # print(f"Selected Row {selected_row} Items: {row_items}")
            cust_id = row_items[0]
            print(cust_id)
            # supp_name = self.booksTableWidget.item(selected_row, 1).text()
            # supp_addr = self.booksTableWidget.item(selected_row, 2).text()
            # supp_cont = self.booksTableWidget.item(selected_row, 3).text()
            # supp_email = self.booksTableWidget.item(selected_row, 4).text()
            # supp_status = self.booksTableWidget.item(selected_row, 5).text()

            selectActStatus = "SELECT activity_status from Customers where customer_id = ?"
            cursor.execute(selectActStatus, cust_id)

            activity_status = cursor.fetchone()[0]
            # print(activity_status)

            if activity_status == "Inactive":
                activity_status2 = "Active"
            elif activity_status == "Active":
                activity_status2 = "Inactive"

            updateSQL = "UPDATE Customers SET activity_status = ? where customer_id = ?"
            cursor.execute(updateSQL, activity_status2, cust_id)
            cursor.commit()

            QtWidgets.QMessageBox.information(self, "Success", f"Activity Status of Customer ID: {cust_id} is changed from {activity_status} to {activity_status2}")

        connection.close()

    def closeButtonClicked(self):
        self.close()

    def adminCustview(self):
        selected_row = self.booksTableWidget.currentRow()
        # print(selected_row)
        if selected_row > 0:
            cust_name = self.booksTableWidget.item(selected_row, 1).text()
            cust_id = self.booksTableWidget.item(selected_row, 0).text()
            cust_addr = self.booksTableWidget.item(selected_row, 2).text()
            cust_cont = self.booksTableWidget.item(selected_row, 3).text()
            cust_email = self.booksTableWidget.item(selected_row, 4).text()
            cust_status = self.booksTableWidget.item(selected_row, 5).text()

            self.custView = AdminCustInfo(cust_name,cust_id, cust_addr, cust_email, cust_cont, cust_status)
            self.custView.show()
            

    def adminSearchcust(self):

        cust_name = self.customer_name.currentText() 
        cust_id = self.customer_id.text()

        # Iterate through rows and compare values
        for row in range(self.booksTableWidget.rowCount()):
            current_cust_name = self.booksTableWidget.item(row, 1).text()
            current_cust_id = self.booksTableWidget.item(row, 0).text()

            if (not cust_name or current_cust_name == cust_name) and (not cust_id or current_cust_id == cust_id):
                # Show the row if it matches the search criteria
                self.booksTableWidget.setRowHidden(row, False)
            else:
                # Hide the row if it does not match the search criteria
                self.booksTableWidget.setRowHidden(row, True)

class AdminCustInfo (QtWidgets.QMainWindow):
    def __init__(self, cust_name,cust_id, cust_addr, cust_email, cust_cont, cust_status):
        # Call the inherited classes __init__ method
        super(AdminCustInfo, self).__init__()

        # Load the .ui file
        uic.loadUi('Screens/24 View Customer.ui', self)
        self.closeButton.clicked.connect(self.closeButtonClicked)


        self.cust_name.setText(str(cust_name))
        self.cust_id.setText(str(cust_id))
        self.cust_address.setText(str(cust_addr))
        self.cust_contact.setText(str(cust_cont))
        self.email.setText(str(cust_email))
        self.status.setText(str(cust_status))


    def closeButtonClicked(self):
        self.close()

class AdminRawMaterial (QtWidgets.QMainWindow):
    def __init__(self):
        # Call the inherited classes __init__ method
        super(AdminRawMaterial, self).__init__()

        
        uic.loadUi('Screens/11 Admin Raw Material Button.ui', self)
        self.searchButton.clicked.connect(self.searchClicked   )

        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        #populate table
        materials = "select RM.material_id, RM.material_name, RM.supplier_id, RM.cost, RM.quality_metric, MI.material_stock from Raw_Material RM FULL OUTER JOIN Material_Inventory MI ON RM.material_id = MI.material_id"
        cursor.execute(materials)
        self.closeButton.clicked.connect(self.closeButton_clicked)
        self.viewButton.clicked.connect(self.view_material)
        self.addButton.clicked.connect(self.open_add)

        for row_index, row_data in enumerate(cursor.fetchall()):
            self.booksTableWidget.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.booksTableWidget.setItem(row_index, col_index, item)
    
    def open_add(self):
        self.startAdd = AdminAddRawMaterial()
        self.startAdd.show()

    def closeButton_clicked(self):
        self.close()

    def view_material(self):
            selected_row = self.booksTableWidget.currentRow()
            if selected_row >= 0:
                material_id = self.booksTableWidget.item(selected_row, 0).text()
                material_name = self.booksTableWidget.item(selected_row, 1).text()
                supp_name = self.booksTableWidget.item(selected_row, 2).text()
                cost = self.booksTableWidget.item(selected_row, 3).text()
                
                self.view_prod_details = viewRawMatDetails(material_id, material_name, supp_name, cost)
                self.view_prod_details.show()

    def searchClicked(self):
        # prod_name = self.categoryCombo.currentText()
        # price = self.price.text()
        # cat_name = self.catcombo.currentText()
        #for activity status
        matId = self.mat_id.text()
        matName = self.mat_name.text()
        suppId = self.supp_id.text()
        cost = self.cost.text()

        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        prods = "select * from Raw_Material"
        cursor.execute(prods)
        for row_index in range(self.booksTableWidget.rowCount()):
            row_hidden = True  # Assume the row will be shown, unless a mismatch is found

            # Match material ID
            if matId and self.booksTableWidget.item(row_index, 0).text() == matId:
                row_hidden = False

            # Match material name
            if matName and self.booksTableWidget.item(row_index, 1).text() == matName:
                row_hidden = False

            # Match supplier ID
            if suppId and self.booksTableWidget.item(row_index, 2).text() == suppId:
                row_hidden = False

            # Match cost
            if cost and self.booksTableWidget.item(row_index, 3).text() == cost:
                row_hidden = False

            # Set the row visibility
            self.booksTableWidget.setRowHidden(row_index, row_hidden)

class AdminAddRawMaterial (QtWidgets.QMainWindow):
    def __init__(self):
        # Call the inherited classes __init__ method
        super(AdminAddRawMaterial, self).__init__()

        uic.loadUi('Screens/13 Add Raw Material.ui', self)
        # material_id = self.material_id.text()
        self.add.clicked.connect(self.openAdd)
        self.closeButton.clicked.connect(self.openCloseButton)
        # addMaterial = "INSERT INTO RAW_MAterial ()"

    def openCloseButton(self):
        self.close()
    def openAdd(self):
        material_name = self.material_name.text()
        supplier_id = int(self.supplier_id.text())
        cost = round(float(self.cost.text()),2)
        quality_metric = self.quality_metric.text()

        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        addMaterial = "INSERT INTO RAW_Material (material_name, supplier_id, cost, quality_metric) VALUES (?, ?, ?, ?)"
        latest = "SELECT IDENT_CURRENT('Raw_Material')"
        insertMaterialStock = "INSERT INTO Material_Inventory (material_id, warehouse_id, material_stock) VALUES (?, 1, 0)"

        cursor.execute(addMaterial, material_name, supplier_id, cost, quality_metric)
        cursor.commit()

        cursor.execute(latest)
        latest_id = cursor.fetchone()[0]
        print(latest_id)

        cursor.execute(insertMaterialStock, latest_id)


class viewRawMatDetails (QtWidgets.QMainWindow):
    def __init__(self, material_id, material_name, supp_name, cost):
        # Call the inherited classes __init__ method
        super(viewRawMatDetails, self).__init__()
        # Load the .ui file
        uic.loadUi('Screens/12 View Raw Material.ui', self)  
        self.closeButton.clicked.connect(self.closeButton_clicked)          
        self.matId.setText(material_id)
        self.mat_name.setText(material_name)
        self.suppId.setText(supp_name)
        self.cost.setText(cost)

        self.matId.setDisabled(True)
        self.mat_name.setDisabled(True)
        self.suppId.setDisabled(True)
        self.cost.setDisabled(True)
        

    def closeButton_clicked(self):
        self.close()   


class ManufacturingViewProducts (QtWidgets.QMainWindow):
    def __init__(self):
        # Call the inherited classes __init__ method
        super(ManufacturingViewProducts, self).__init__()

        # Load the .ui file
        uic.loadUi('Screens/low_stock prod view.ui', self)

        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        fetchProductLowInInventory = "select p.product_id, p.product_name, c.category_name, P.Price, P_I.Product_stock from Products P INNER JOIN Category C ON P.category_id = C.category_id INNER JOIN Product_Inventory P_I ON P.product_id = P_I.product_id where P_I.product_stock < 1500"
        cursor.execute(fetchProductLowInInventory)
         
        for row_index, row_data in enumerate(cursor.fetchall()):
            self.low_inventory_products.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                if col_index == 3:
                    cell_data = round(float(cell_data), 2)
                item = QTableWidgetItem(str(cell_data))
                self.low_inventory_products.setItem(row_index, col_index, item)
        
        connection.close()

        self.manufacture_product.clicked.connect(self.open_manufactureProduct)

    def open_manufactureProduct(self):
        selected_items = self.low_inventory_products.selectedItems()

        if len(selected_items) > 0:
            selected_item = selected_items[0]
            selected_row = selected_item.row()

            # Get all items in the selected row
            row_items = []
            for col in range(self.low_inventory_products.columnCount()):
                item = self.low_inventory_products.item(selected_row, col)
                if item is not None:
                    row_items.append(item.text())

            # print(f"Selected Row {selected_row} Items: {row_items}")
            product_id = row_items[0]
            product_name = row_items[1]
            category_name = row_items[2]
            price = row_items[3]
            stock_left = row_items[4]

            print(product_id, product_name, category_name, price, stock_left)

            self.startManufactureProduct = ManufactureProduct(product_id, product_name)
            self.startManufactureProduct.show()

            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()

            # selectEmployeeId = "select employee_id from Employees where employee_name = ?"
            # cursor.execute(selectEmployeeId, employee_name)
            # employee_id = cursor.fetchone()[0]
            # # print(employee_id)
            
            # getDate = "SELECT CONVERT(DATE, GETDATE(), 103) AS CurrentDate"
            # cursor.execute(getDate)
            # today = cursor.fetchone()[0]
            # updateOrder = "UPDATE Orders SET Employee_id = ?, delivery_status = ?, shipped_date = ? where Order_id = ?"
            # cursor.execute(updateOrder, employee_id, 'Delivered', today, order_id)
            # cursor.commit()

            # fetchOrderProducts = "Select * from Order_Details where order_id = ?"
            # cursor.execute(fetchOrderProducts, order_id)
            # temp = cursor.fetchall()
            # for i in temp:
            #     product_id = i[1]
            #     quantity = i[2]
            #     updateProductInventory = "update Product_Inventory SET product_stock = product_stock - ? where product_id = ?;"
            #     cursor.execute(updateProductInventory, int(quantity), int(product_id))
            #     cursor.commit()

            connection.close()
        else:
            QtWidgets.QMessageBox.warning(self, "Error", f"No Product Selected")

        #############################3
        #Retrive INFO
        


class ManufactureProduct (QtWidgets.QMainWindow):
    def __init__(self, product_id, product_name):
        # Call the inherited classes __init__ method
        super(ManufactureProduct, self).__init__()

        # Load the .ui file
        uic.loadUi('Screens/raw_mat manufacture.ui', self)

        self.product_name.setText(product_name)
        self.product_id.setText(product_id)
        self.product_name.setEnabled(False)
        self.product_id.setEnabled(False)

        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        ############################################

        fetchProductMaterials = "select R.material_name, PR.material_used from Raw_Material R INNER JOIN Products_RawMaterial PR ON R.material_id = PR.material_id INNER JOIN Products P ON P.product_id = PR.product_id where p.product_id = ?"
        cursor.execute(fetchProductMaterials, int(product_id))

        for row_index, row_data in enumerate(cursor.fetchall()):
            self.rawMaterial_table.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                if col_index == 3:
                    cell_data = round(float(cell_data), 2)
                item = QTableWidgetItem(str(cell_data))
                self.rawMaterial_table.setItem(row_index, col_index, item)

        self.initiate_manufacturing.clicked.connect(self.transactManufacturing)
        connection.close()

    def transactManufacturing(self):
        product_id = int(self.product_id.text())
        product_name = self.product_name.text()
        print(product_id, product_name)

        quantity_of_product_to_manufacture = self.quantity.text()
        if quantity_of_product_to_manufacture != "":
            quantity_of_product_to_manufacture = int(quantity_of_product_to_manufacture)
            table_data = []
            for row in range(self.rawMaterial_table.rowCount()):
                material_name_item = self.rawMaterial_table.item(row, 0)
                quantity_item = self.rawMaterial_table.item(row, 1)
                
                # Check if items exist to avoid NoneType errors
                if material_name_item is not None and quantity_item is not None:
                    material_name = material_name_item.text()
                    quantity = quantity_item.text()
                    table_data.append([material_name, int(quantity)])

            print(table_data)
            
            for i in table_data:
                i[1] = i[1] * quantity_of_product_to_manufacture
            print(table_data)

            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()   
            fetchMaterialID = "SELECT material_id from Raw_Material where material_name = ?"
            updateMaterialStock = "UPDATE Material_Inventory SET material_stock = material_stock - ? where material_id = ?"
            for i in table_data:
                cursor.execute(fetchMaterialID, i[0])
                material_id = int(cursor.fetchone()[0])
                print(material_id)

                cursor.execute(updateMaterialStock, i[1], material_id)
                cursor.commit()
            
            updateProductStock = "update Product_Inventory SET product_stock = product_stock + ? where product_id = ?"
            cursor.execute(updateProductStock, quantity_of_product_to_manufacture, product_id)
            cursor.commit()
            
            QtWidgets.QMessageBox.information(self, "Success", f"{quantity_of_product_to_manufacture} Units of {product_name} were Manufactured")



        else:
            QtWidgets.QMessageBox.warning(self, "Error", f"Please specify the Quantity of {product_name} to Manufacture")

        pass

class AdminSupplierView (QtWidgets.QMainWindow):
    def __init__(self):
        # Call the inherited classes __init__ method
        super(AdminSupplierView, self).__init__()

        # Load the .ui file
        uic.loadUi('Screens/21 Supplier Button.ui', self)
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        fillSupplierComboBox = "SELECT supplier_name from Suppliers"
        cursor.execute(fillSupplierComboBox)

        for row_data in cursor.fetchall():
            for cell_data in row_data:
                self.supplier_name.addItem(str(cell_data))

        all_supp = "select * from Suppliers"
        cursor.execute(all_supp)

        for row_index, row_data in enumerate(cursor.fetchall()):
            self.booksTableWidget.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.booksTableWidget.setItem(row_index, col_index, item)

        self.searchButton.clicked.connect(self.adminSearchsupp)
        self.supp_view.clicked.connect(self.adminSuppview)
        self.closeButton.clicked.connect(self.closeButtonClicked)
        self.changeActivityStatus.clicked.connect(self.changeActivityStatusfunc)

        connection.close()

    def changeActivityStatusfunc(self):
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        # selected_items = self.pendingOrderTable.selectedItems()

        selected_items = self.booksTableWidget.selectedItems()

        if len(selected_items) > 0:
            selected_item = selected_items[0]
            selected_row = selected_item.row()

            # Get all items in the selected row
            row_items = []
            for col in range(self.booksTableWidget.columnCount()):
                item = self.booksTableWidget.item(selected_row, col)
                if item is not None:
                    row_items.append(item.text())

            # print(f"Selected Row {selected_row} Items: {row_items}")
            supp_id = row_items[0]
            print(supp_id)
            # supp_name = self.booksTableWidget.item(selected_row, 1).text()
            # supp_addr = self.booksTableWidget.item(selected_row, 2).text()
            # supp_cont = self.booksTableWidget.item(selected_row, 3).text()
            # supp_email = self.booksTableWidget.item(selected_row, 4).text()
            # supp_status = self.booksTableWidget.item(selected_row, 5).text()

            selectActStatus = "SELECT activity_status from Suppliers where supplier_id = ?"
            cursor.execute(selectActStatus, supp_id)

            activity_status = cursor.fetchone()[0]
            # print(activity_status)

            if activity_status == "Inactive":
                activity_status2 = "Active"
            elif activity_status == "Active":
                activity_status2 = "Inactive"

            updateSQL = "UPDATE Suppliers SET activity_status = ? where supplier_id = ?"
            cursor.execute(updateSQL, activity_status2, supp_id)
            cursor.commit()

            QtWidgets.QMessageBox.information(self, "Success", f"Activity Status of Supplier ID: {supp_id} is changed from {activity_status} to {activity_status2}")

        connection.close()

    def closeButtonClicked(self):
        self.close()

    def adminSuppview(self):
        selected_row = self.booksTableWidget.currentRow()
        # print(selected_row)
        if selected_row > 0:
            supp_name = self.booksTableWidget.item(selected_row, 1).text()
            supp_id = self.booksTableWidget.item(selected_row, 0).text()
            supp_addr = self.booksTableWidget.item(selected_row, 2).text()
            supp_cont = self.booksTableWidget.item(selected_row, 3).text()
            supp_email = self.booksTableWidget.item(selected_row, 4).text()
            supp_status = self.booksTableWidget.item(selected_row, 5).text()

            self.suppView = AdminSuppInfo(supp_name,supp_id, supp_addr, supp_email, supp_cont, supp_status)
            self.suppView.show()
            

    def adminSearchsupp(self):

        sup_name = self.supplier_name.currentText() 
        sup_id = self.supplier_id.text()

        # Iterate through rows and compare values
        for row in range(self.booksTableWidget.rowCount()):
            current_sup_name = self.booksTableWidget.item(row, 1).text()
            current_sup_id = self.booksTableWidget.item(row, 0).text()

            if (not sup_name or current_sup_name == sup_name) and (not sup_id or current_sup_id == sup_id):
                # Show the row if it matches the search criteria
                self.booksTableWidget.setRowHidden(row, False)
            else:
                # Hide the row if it does not match the search criteria
                self.booksTableWidget.setRowHidden(row, True)


class AdminSuppInfo (QtWidgets.QMainWindow):
    def __init__(self, supp_name,supp_id, supp_addr, supp_email, supp_cont, supp_status):
        # Call the inherited classes __init__ method
        super(AdminSuppInfo, self).__init__()

        # Load the .ui file
        uic.loadUi('Screens/22 View Supplier.ui', self)
        self.closeButton.clicked.connect(self.closeButtonClicked)


        self.supp_name.setText(str(supp_name))
        self.supp_id.setText(str(supp_id))
        self.supp_address.setText(str(supp_addr))
        self.supp_contact.setText(str(supp_cont))
        self.email.setText(str(supp_email))
        self.status.setText(str(supp_status))


    def closeButtonClicked(self):
        self.close()


class CurrentOrders (QtWidgets.QMainWindow):
    def __init__(self, current_id):
        self.current_id = current_id
        # Call the inherited classes __init__ method
        super(CurrentOrders, self).__init__()

        # Load the .ui file
        uic.loadUi('Screens/5 Admin Order Approve.ui', self)

        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        searchOrdersForApproval = "SELECT order_id, customer_id, order_date, required_date from Orders where employee_id is NULL"
        cursor.execute(searchOrdersForApproval)
        # for i in cursor.fetchall():
        #     self.pendingOrderTable.
        for row_index, row_data in enumerate(cursor.fetchall()):
            self.pendingOrderTable.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.pendingOrderTable.setItem(row_index, col_index, item)

        fillEmployeeComboBox = "SELECT employee_name from Employees where department = ?"
        cursor.execute(fillEmployeeComboBox, "Sales")

        for row_data in cursor.fetchall():
            for cell_data in row_data:
                self.employeeToBeAssigned.addItem(str(cell_data))

        connection.close()

        self.approveOrder.clicked.connect(lambda: self.transact_approveOrder(self.employeeToBeAssigned.currentText()))
        self.closeButton.clicked.connect(self.closeScreen)
        # header = self.pendingOrderTable.horizontalHeader()
        # header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        # header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        # header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
    
    def closeScreen(self):
        self.close()

    def transact_approveOrder(self, employee_name):
        selected_items = self.pendingOrderTable.selectedItems()

        if len(selected_items) > 0:
            selected_item = selected_items[0]
            selected_row = selected_item.row()

            # Get all items in the selected row
            row_items = []
            for col in range(self.pendingOrderTable.columnCount()):
                item = self.pendingOrderTable.item(selected_row, col)
                if item is not None:
                    row_items.append(item.text())

            # print(f"Selected Row {selected_row} Items: {row_items}")
            order_id = row_items[0]
            customer_id = row_items[1]
            order_date = row_items[2]
            required_date = row_items[3]

            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()

            selectEmployeeId = "select employee_id from Employees where employee_name = ?"
            cursor.execute(selectEmployeeId, employee_name)
            employee_id = cursor.fetchone()[0]
            # print(employee_id)
            
            getDate = "SELECT CONVERT(DATE, GETDATE(), 103) AS CurrentDate"
            cursor.execute(getDate)
            today = cursor.fetchone()[0]
            updateOrder = "UPDATE Orders SET Employee_id = ?, delivery_status = ?, shipped_date = ? where Order_id = ?"
            cursor.execute(updateOrder, employee_id, 'Delivered', today, order_id)
            cursor.commit()

            fetchOrderProducts = "Select * from Order_Details where order_id = ?"
            cursor.execute(fetchOrderProducts, order_id)
            temp = cursor.fetchall()
            for i in temp:
                product_id = i[1]
                quantity = i[2]
                updateProductInventory = "update Product_Inventory SET product_stock = product_stock - ? where product_id = ?;"
                cursor.execute(updateProductInventory, int(quantity), int(product_id))
                cursor.commit()

            connection.close()
            QtWidgets.QMessageBox.information(self, "Success", f"Order ID: {order_id} has been handed over to Employee ID: {employee_id}")
        else:
            QtWidgets.QMessageBox.warning(self, "Error", f"No Order selected from the Table")

class CustomerDashboard (QtWidgets.QMainWindow):
    def __init__(self, current_id):
        self.current_id = current_id
        # Call the inherited classes __init__ method
        super(CustomerDashboard, self).__init__()

        # Load the .ui file
        uic.loadUi('Screens/25 Customer Dashboard.ui', self)

        # connection = pyodbc.connect(connection_string)
        # cursor = connection.cursor()

        self.customerInfo.clicked.connect(lambda: self.open_customerInfo(current_id))
        self.orders.clicked.connect(lambda: self.open_customerOrders(current_id))
        self.productView.clicked.connect(self.customerProd)
        self.feedback.clicked.connect(lambda: self.open_customerFeedback(current_id))

    def open_customerFeedback(self, current_id):
        self.startCustomerFeedback = CustomerFeedback(current_id)
        self.startCustomerFeedback.show()
    
    def open_customerOrders(self, current_id):
        #To be Editied TODO
        # self.startCustomerOrders = CustomerOrdersView()
        self.startCustomerOrders = CustomerPlaceOrder(current_id)
        self.startCustomerOrders.show()
    
    def open_customerInfo(self, current_id):
        self.c_info = CustomerInformation(current_id)
        self.c_info.show()
    def customerProd(self):
        self.c_prod = CustomerProductView()
        self.c_prod.show()

class CustomerFeedback (QtWidgets.QMainWindow):
    def __init__(self, current_id):
        # self.current_id = current_id
        # Call the inherited classes __init__ method
        super(CustomerFeedback, self).__init__()

        # Load the .ui file
        uic.loadUi('Screens/46 feedbacks.ui', self)

        ###################################################
        self.customer_id.setText(current_id)
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        fetchOrdersWithoutFeedback = "SELECT order_id from Orders where order_feedback is null and customer_id = ? and delivery_status = 'Delivered'"
        cursor.execute(fetchOrdersWithoutFeedback, current_id)

        for row_data in cursor.fetchall():
            for cell_data in row_data:
                self.order_id.addItem(str(cell_data))

        connection.close()

        self.submit.clicked.connect(lambda: self.submitButton(current_id))
        self.closeButton.clicked.connect(self.closeFeedback)

    def submitButton(self, current_id):
        order_id = self.order_id.currentText()
        if order_id == "":
            QtWidgets.QMessageBox.information(self, "Information", f"You have no pending feedbacks to give!")
        else:
            order_id = int(order_id)
            print(order_id)
            feedback = self.feedback.toPlainText()
            print(feedback)
            if feedback != "":
                connection = pyodbc.connect(connection_string)
                cursor = connection.cursor()

                UpdateFeedbackInOrders = "UPDATE Orders SET order_feedback = ? where order_id = ?"
                cursor.execute(UpdateFeedbackInOrders, feedback, order_id)
                cursor.commit()

                connection.close()
                QtWidgets.QMessageBox.information(self, "Success", f"Thank you for your feedback!")
            else:
                QtWidgets.QMessageBox.warning(self, "Error", f"You can not submit an empty feedback!")

    def closeFeedback(self):
        self.close()

class CustomerProductView (QtWidgets.QMainWindow):
    def __init__(self):
        # self.current_id = current_id
        # Call the inherited classes __init__ method
        super(CustomerProductView, self).__init__()

        # Load the .ui file
        uic.loadUi('Screens/29 Customer Product Button.ui', self)
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        prods = "select P.product_id, P.product_name, C.category_name, P.price from products P inner Join Category C on P.category_id = C.category_id"
        cursor.execute(prods)

        for row_index, row_data in enumerate(cursor.fetchall()):
            self.booksTableWidget.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.booksTableWidget.setItem(row_index, col_index, item)

        prod_name = "select product_name from products"
        cursor.execute(prod_name)
        # names =  list(cursor.fetchall())
        names = [row.product_name for row in cursor.fetchall()]
        # print(names)
        self.categoryCombo.addItems(names)

        cat_name = "select category_name from Category"
        cursor.execute(cat_name)
        # names =  list(cursor.fetchall())
        names = [row.category_name for row in cursor.fetchall()]
        # print(names)
        self.catcombo.addItems(names)

        self.searchButton.clicked.connect(self.searchClicked)
        self.viewButton.clicked.connect(self.viewMaterial_clicked)
        self.closeButton.clicked.connect(self.closeButton_clicked)

    def viewMaterial_clicked(self, current_id):
        selected_row = self.booksTableWidget.currentRow()
        if selected_row >= 0:
            material_id = self.booksTableWidget.item(selected_row, 0).text()
            material_name = self.booksTableWidget.item(selected_row, 1).text()
            categorys_name = self.booksTableWidget.item(selected_row, 2).text()
            cost = self.booksTableWidget.item(selected_row, 3).text()
            
            self.view_prod_details = viewProductDetails(material_id, material_name, categorys_name, cost)
            self.view_prod_details.show()
    def closeButton_clicked(self):
        self.close()
    def searchClicked(self):
        prod_name = self.categoryCombo.currentText()
        price = self.price.text()
        cat_name = self.catcombo.currentText()
        #for activity status
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        prods = "select product_name from products"
        cursor.execute(prods)
        for row_index in range(self.booksTableWidget.rowCount()):
                row_hidden = True  # Assume the row will be hidden, unless a match is found

                if prod_name and self.booksTableWidget.item(row_index, 1).text() == prod_name:
                    row_hidden = False

                if price and self.booksTableWidget.item(row_index, 3).text() == price:
                    row_hidden = False

                if cat_name and self.booksTableWidget.item(row_index, 2).text() == cat_name:
                    row_hidden = False

                self.booksTableWidget.setRowHidden(row_index, row_hidden)

                
class viewProductDetails (QtWidgets.QMainWindow):
    def __init__(self, product_id, prod_name, categorys_name, cost):
        # self.current_id = current_id
        # Call the inherited classes __init__ method
        super(viewProductDetails, self).__init__()

        # Load the .ui file
        uic.loadUi('Screens/30 Customer View Products.ui', self)
        self.name.setText(prod_name)
        self.category.setText(categorys_name)
        self.price.setText(cost)
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        self.closeButton.clicked.connect(self.closeButton_clicked)


        fetchCustomerName = "SELECT continuity_status from products where product_id = ?"
        cursor.execute(fetchCustomerName, product_id)
        row = cursor.fetchone()
        status = str(row.continuity_status)
        # print(status)
        if status:
            self.cont_stat.setChecked(True) 
        else:
            self.cont_stat.setChecked(False) 
        # price = float(cursor.fetchone())
        # print(price)
        # price = float(row.price)
        # print(price)
        # cost = price
        fetchCustomerName = "select M.material_name from Raw_Material M inner join Products_RawMaterial PR on M.material_id = PR.material_id where PR.product_id = ?;"
        cursor.execute(fetchCustomerName, product_id)
        # row = cursor.fetchall()
        # print(row)
        rows = cursor.fetchall()
        self.populate_table(rows)

    def populate_table(self, rows):
        # Assuming you have a QTableWidget named self.tableWidget
        self.booksTableWidget.setColumnCount(1)  # Set the number of columns
        self.booksTableWidget.setRowCount(len(rows))  # Set the number of rows

        for row_index, row_data in enumerate(rows):
            item = QTableWidgetItem(str(row_data.material_name))
            self.booksTableWidget.setItem(row_index, 0, item)

        
    def closeButton_clicked(self):
        self.close()





class CustomerInformation (QtWidgets.QMainWindow):
    def __init__(self, current_id):
        self.current_id = current_id
        # Call the inherited classes __init__ method
        super(CustomerInformation, self).__init__()

        # Load the .ui file
        uic.loadUi('Screens/31 Customer info form.ui', self)

        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        fetchCustomerName = "SELECT * from Customers where customer_id = ?"
        cursor.execute(fetchCustomerName, current_id)
        name = cursor.fetchone()#[0]
        # print(name)
        self.id.setText(str(name[0]))
        self.name.setText(str(name[1]))
        self.address.setText(str(name[2]))
        self.contact.setText(str(name[3]))
        self.email.setText(str(name[4]))

        self.id.setEnabled(False)
        self.name.setEnabled(False)
        self.address.setEnabled(False)
        self.contact.setEnabled(False)
        self.email.setEnabled(False)

        self.closeButton.clicked.connect(self.closeButtonClicked)

    def closeButtonClicked(self):
        self.close()

class CustomerPlaceOrder (QtWidgets.QMainWindow):
    def __init__(self, current_id):
        self.current_id = current_id
        # Call the inherited classes __init__ method
        super(CustomerPlaceOrder, self).__init__()

        # Load the .ui file
        uic.loadUi('Screens/45 Customer Order Placing.ui', self)

        self.customer_id.setText(str(current_id))
        self.customer_id.setEnabled(False)

        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        fetchCustomerName = "SELECT customer_name from Customers where customer_id = ?"
        cursor.execute(fetchCustomerName, current_id)
        name = cursor.fetchone()[0]
        self.customer_name.setText(str(name))
        self.customer_name.setEnabled(False)

        # print(QDate.currentDate())
        order_date = QDate.currentDate()
        self.order_date.setDate(order_date)
        self.order_date.setEnabled(False)

        self.required_date.setDate(order_date)
        #if statements to be added req date > order date

        fetchAllProducts = "SELECT product_name from Products where continuity_status = 'True'"
        cursor.execute(fetchAllProducts)
        for i in cursor.fetchall():
            self.available_products.addItem(i[0])

        self.add_to_cart.clicked.connect(self.AddProductToCart)
        self.place_order.clicked.connect(self.PlaceOrder)
        self.cancel.clicked.connect(self.cancelPlaceOrder)
        # self.total.setText("{:.2f}".format(0.00))
        self.total.setText(str(0.00))
        self.total.setEnabled(False)
        connection.close()

    def cancelPlaceOrder(self):
        self.close()
    
    def PlaceOrder(self):
        customer_id = self.customer_id.text()
        customer_name = self.customer_name.text()
        order_date = self.order_date.date().toString("yyyy-MM-dd")
        required_date = self.required_date.date().toString("yyyy-MM-dd")
        # print(order_date, required_date)

        products_to_be_ordered = []
        for row in range(self.productTable.rowCount()):
            row_items = []
            for col in range(self.productTable.columnCount()):
                item = self.productTable.item(row, col)
                if item is not None:
                    row_items.append(item.text())
                else:
                    row_items.append(None)

            products_to_be_ordered.append(row_items)
        
        print(products_to_be_ordered)

        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        
        if products_to_be_ordered != []:
            insertIntoOrders = "INSERT INTO Orders (customer_id, employee_id, order_date, required_date, delivery_status, shipped_date) VALUES (?, NULL, ?, ?, 'Pending', NULL)"
            cursor.execute(insertIntoOrders, customer_id, order_date, required_date)
            cursor.commit()
            latest_in_order = "SELECT IDENT_CURRENT('Orders')"
            cursor.execute(latest_in_order)
            order_id = cursor.fetchone()[0]
            print(order_id)

            for i in products_to_be_ordered:
                product_id = i[0]
                quantity = i[2]
                total_product_price = i[4]
                #Multiple Inserts here.
                insertIntoOrderDetails = "INSERT INTO Order_Details (order_id, product_id, quantity, price) VALUES (?, ?, ?, ?)"
                cursor.execute(insertIntoOrderDetails, order_id, product_id, quantity, total_product_price)
                cursor.commit()
            
            self.close()
            QtWidgets.QMessageBox.information(self, "Success", f"Order successfully generated. Your order ID is: {order_id}.")
            # self.close()
            # self.close()
        else:
            QtWidgets.QMessageBox.warning(self, "Error", f"Order generation failed as there are no products in the cart.")


    def AddProductToCart(self):
        try:
            quantity = int(self.quantity.text())
            product_name = self.available_products.currentText()

            num_rows = self.productTable.rowCount()
            flag = False
            for row in range(num_rows):
                product_name_in_table = self.productTable.item(row, 1).text()
                if product_name_in_table == product_name:
                    flag = True
                    product_id_in_table = self.productTable.item(row, 0).text()
                    quantity_in_table = self.productTable.item(row, 2).text()
                    product_price_in_table = self.productTable.item(row, 3).text()
                    product_total_in_table = self.productTable.item(row, 4).text()

                    total_quantity = int(quantity_in_table) + quantity
                    total_price = float(product_total_in_table) + (quantity * float(product_price_in_table))
                    connection = pyodbc.connect(connection_string)
                    cursor = connection.cursor()

                    checkInventory = "SELECT Product_stock from Product_Inventory where product_id = ?"
                    cursor.execute(checkInventory, product_id_in_table)
                    product_stock_in_table = int(cursor.fetchone()[0])
                    if product_stock_in_table >= total_quantity:
                        #Replace the total quantity and new price
                        total_price = round(total_price, 2)
                        self.productTable.setItem(row, 2, QTableWidgetItem(str(total_quantity)))
                        self.productTable.setItem(row, 4, QTableWidgetItem(str(total_price)))

                        #ERROR: Calculating Fault
                        final_total = float(self.total.text())
                        final_total += float(total_price)
                        final_total = round(final_total, 2)
                        self.total.setText(str(final_total))
                    else:
                        QtWidgets.QMessageBox.warning(self, "Error", f"Failed to add to cart. Only {product_stock_in_table} units of the product named '{product_name}' are available, and {total_quantity} units are requested for addition.")

            if not(flag):
                connection = pyodbc.connect(connection_string)
                cursor = connection.cursor()

                getId = "SELECT product_id, price from products where product_name = ?"
                cursor.execute(getId, product_name)
                temp = cursor.fetchone()
                # print(temp)
                product_id = int(temp[0])
                product_price = float(temp[1])
                # print(product_id, product_price)

                checkInventory = "SELECT Product_stock from Product_Inventory where product_id = ?"
                cursor.execute(checkInventory, product_id)
                product_stock = int(cursor.fetchone()[0])
                # print(product_stock)

                if product_stock >= quantity:
                    product_total = quantity * product_price
                    product_total = round(product_total, 2)
                    self.productTable.insertRow(self.productTable.rowCount())
                    self.productTable.setItem(self.productTable.rowCount() - 1, 0, QTableWidgetItem(str(product_id)))
                    self.productTable.setItem(self.productTable.rowCount() - 1, 1, QTableWidgetItem(product_name))
                    self.productTable.setItem(self.productTable.rowCount() - 1, 2, QTableWidgetItem(str(quantity)))
                    self.productTable.setItem(self.productTable.rowCount() - 1, 3, QTableWidgetItem(str(product_price)))
                    self.productTable.setItem(self.productTable.rowCount() - 1, 4, QTableWidgetItem(str(product_total)))
                    # self.productTable.add_table_item(str(product_id), product_name, str(product_price), str(product_total))
                    final_total = float(self.total.text())
                    final_total += float(product_total)
                    final_total = round(final_total, 2)
                    self.total.setText(str(final_total))
                else:
                    QtWidgets.QMessageBox.warning(self, "Error", f"Only {product_stock} units of the product named '{product_name}' are remaining.") 

                connection.close()

        except ValueError:
            QtWidgets.QMessageBox.critical(self, "Error", f"Quantity must be a numeric value.")
        
class SupplierDashboard (QtWidgets.QMainWindow):
    def __init__(self, current_id):
        self.current_id = current_id
        # Call the inherited classes __init__ method
        super(SupplierDashboard, self).__init__()

        # Load the .ui file
        uic.loadUi('Screens/39 supplier dashboard.ui', self)

        self.send_order.clicked.connect(lambda: self.open_generateOrder(self.current_id))
        self.supp_info.clicked.connect(lambda: self.open_supplierInfo(self.current_id))

    def open_generateOrder(self, current_id):
        self.startRawMaterialMaster = SupplierRawMaterials(current_id)
        self.startRawMaterialMaster.show()

    def open_supplierInfo(self, current_id):
        self.startsupplierInfoView = SupplierInformation(current_id)
        self.startsupplierInfoView.show()

class SupplierGenerateOrder (QtWidgets.QMainWindow):
    def __init__(self, current_id):
        self.current_id = current_id
        # Call the inherited classes __init__ method
        super(SupplierGenerateOrder, self).__init__()

        # Load the .ui file
        uic.loadUi('Screens/42 Supplier Generate Order Form.ui', self)

        self.supplier_id.setText(current_id)
        self.supplier_id.setEnabled(False)

        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        fetchMaterials = "SELECT material_name from Raw_Material"
        cursor.execute(fetchMaterials)

        for row_data in cursor.fetchall():
            for cell_data in row_data:
                self.material_name.addItem(str(cell_data))
        
        getDate = "SELECT CONVERT(DATE, GETDATE(), 103) AS CurrentDate"
        cursor.execute(getDate)
        today = cursor.fetchone()[0]

        self.order_date.setDate(today)
        self.order_date.setEnabled(False)

        self.generate_order.clicked.connect(lambda: self.tranactionSupplierGenerateOrder(self.material_name.currentText(), int(self.quantity.text())))

        connection.close()

    def tranactionSupplierGenerateOrder(self, material_name, quantity):
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        
        fetchMaterialId = "SELECT material_id from Raw_Material where material_name = ?"
        cursor.execute(fetchMaterialId, material_name)
        material_id = cursor.fetchone()[0]
        print(material_id)

        updateRawMaterialInventory = "UPDATE Material_Inventory SET material_stock = material_stock + ? where material_id = ?"
        cursor.execute(updateRawMaterialInventory, quantity, material_id)
        cursor.commit()
        self.close()
        QtWidgets.QMessageBox.information(self, "Success", f"Your Raw Material are Delivered to the Warehouse.")
        connection.close()

class SupplierInformation(QtWidgets.QMainWindow):
    def __init__(self, current_id):
        self.current_id = current_id
        super(SupplierInformation, self).__init__()
        uic.loadUi('Screens/43 Supplier info form.ui', self)
        self.setWindowTitle("Supplier Information")

        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        #detch data from raw_mat table 
        query = "select * from Suppliers where supplier_id = ?"
        cursor.execute(query, current_id)

        row = cursor.fetchone() 
        self.closeButton.clicked.connect(self.view_close)
        print(row)
        suppID = row[0]
        suppName = row[1]
        suppAdd = row[2]
        suppPhone = row[3]
        suppEmail = row[4]
        suppActStatus = row[5]

        self.supp_id.setText(str(suppID))
        self.supp_name.setText(str(suppName))
        self.supp_addr.setText(str(suppAdd))
        self.supp_phone.setText(str(suppPhone))
        self.supp_email.setText(str(suppEmail))
        self.supp_act_status.setText(str(suppActStatus))

        # Disable QLineEdit widgets
        self.supp_id.setEnabled(False)
        self.supp_name.setEnabled(False)
        self.supp_addr.setEnabled(False)
        self.supp_phone.setEnabled(False)
        self.supp_email.setEnabled(False)
        self.supp_act_status.setEnabled(False)

    def view_close(self):
        self.close()

class SupplierRawMaterials(QtWidgets.QMainWindow):
    def __init__(self, current_id):
        self.current_id = current_id
        super(SupplierRawMaterials, self).__init__()
        
        uic.loadUi('Screens/40 Supplier Order form.ui', self)
        self.setWindowTitle("Materials Supplied")
        
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        fillSupplierOrders = "select R.material_name, R.cost, MI.material_stock from Raw_Material R INNER JOIN Material_Inventory MI ON R.material_id = MI.material_id where R.supplier_id = ?"
        cursor.execute(fillSupplierOrders, current_id)
        
        for row_index, row_data in enumerate(cursor.fetchall()):
            self.booksTableWidget.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.booksTableWidget.setItem(row_index, col_index, item)

        #TODO: Change Material Name Liine edit to ComboBOX
        connection.close()

        self.supp_order_search.clicked.connect(self.suppMaterialSearch)
        self.viewButton.clicked.connect(lambda: self.viewMaterial_clicked(current_id))
        self.closeButton.clicked.connect(self.view_close)
        self.generateOrder.clicked.connect(lambda: self.generate_Order_Clicked(current_id))
    

    def populate_supp_rawMat(self):
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        # Clear existing rows in the table
        self.booksTableWidget.setRowCount(0)

        #detch data from raw_mat table 
        cursor.execute("select * from Raw_Material")

        # Fetch all rows and populate the table
        for row_index, row_data in enumerate(cursor.fetchall()):
            self.booksTableWidget.insertRow(row_index)
            print(row_data)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.booksTableWidget.setItem(row_index, col_index, item)

        #close database connection
        connection.close()

    def viewMaterial_clicked(self, current_id):
        selected_row = self.booksTableWidget.currentRow()
        # material_id = self.booksTableWidget.item(selected_row, 0)
        # material_name = self.booksTableWidget.item(selected_row, 1)
        # supplier_id = self.booksTableWidget.item(selected_row, 2)
        # cost = self.booksTableWidget.item(selected_row, 3)
        # inventory_level = self.booksTableWidget.item(selected_row, 4)
        # quality_metric = self.booksTableWidget.item(selected_row, 5)
        if selected_row >= 0:
            # material_id = self.booksTableWidget.item(selected_row, 0)
            material_name = self.booksTableWidget.item(selected_row, 0)
            # supplier_id = self.booksTableWidget.item(selected_row, 2)
            cost = self.booksTableWidget.item(selected_row, 1)
            inventory_level = self.booksTableWidget.item(selected_row, 2)
            #############
            self.viewMat = viewRawMaterial(material_name, current_id, cost,inventory_level)
            self.viewMat.show()

    def view_close(self):
        self.close()

    #TODO: RESOLVE SEARCH
    def suppMaterialSearch(self):
        # material_id = self.mat_name.text()
        # supp_id = self.supp_id.text()
        material_name = self.mat_name.text()

        # for row in range(self.booksTableWidget.rowCount()):
        #     # m_id = self.booksTableWidget.item(row, 0).text() if self.booksTableWidget.item(row, 0) is not None else ""
        #     # s_id = self.booksTableWidget.item(row, 2).text() if self.booksTableWidget.item(row, 1) is not None else ""
        #     # m_name = self.booksTableWidget.item(row, 0).text() if self.booksTableWidget.item(row, 0) is not None else ""
        #     try:
        #         m_name = self.booksTableWidget.item(row, 0).text()
        #     except AttributeError:
        #         m_name = ""
        #     # if not (material_name==m_name):
        #     #     self.booksTableWidget.setRowHidden(row, False)
        #     # else:
        #         # Show the row if at least one criterion matches
        #     if m_name == material_name:
        #         self.booksTableWidget.setRowHidden(row, False)
        #     else:
        #         self.booksTableWidget.setRowHidden(row, True)
        for row in range(self.booksTableWidget.rowCount()):
            try:
                m_name = self.booksTableWidget.item(row, 0).text()
            except AttributeError:
                m_name = ""

            if not material_name or m_name == material_name:
                # Show the row if no search criteria or if the material name matches
                self.booksTableWidget.setRowHidden(row, False)
            else:
                # Hide the row if material name does not match the search criteria
                self.booksTableWidget.setRowHidden(row, True)
    def generate_Order_Clicked(self, current_id):

        self.startSupplierOrderGen = SupplierGenerateOrder(current_id)
        self.startSupplierOrderGen.show()
        
class viewRawMaterial(QtWidgets.QMainWindow):
    def __init__(self, material_name, supplier_id, cost, inventory_level):
        super(viewRawMaterial, self).__init__()
        
        uic.loadUi('Screens/41 Supplier View Order Form.ui', self)
        self.setWindowTitle("Material Info")

        self.closeButton.clicked.connect(self.view_close)

        self.mat_name.setText(str(material_name.text()))
        self.sup_id.setText(str(supplier_id))
        self.cost_line.setText(str(cost.text()))
        self.inven_levl.setText(str(inventory_level.text()))

        # Disable QLineEdit widgets
        self.mat_name.setEnabled(False)
        self.sup_id.setEnabled(False)
        self.cost_line.setEnabled(False)
        self.inven_levl.setEnabled(False)

    def view_close(self):
        self.close()

def main():
    app = QApplication(sys.argv)
    window = UI()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()