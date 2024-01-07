/*
INSERT INTO Registrations (password, user_type) VALUES ('password123', 'Employee');
INSERT INTO Registrations (password, user_type) VALUES ('securePass', 'Customer');
INSERT INTO Registrations (password, user_type) VALUES ('letmein', 'Employee');
INSERT INTO Registrations (password, user_type) VALUES ('strongPass', 'Employee');
INSERT INTO Registrations (password, user_type) VALUES ('test123', 'Customer');
INSERT INTO Registrations (password, user_type) VALUES ('userpass', 'Customer');
INSERT INTO Registrations (password, user_type) VALUES ('user999', 'Employee');
INSERT INTO Registrations (password, user_type) VALUES ('user1', 'Customer');
INSERT INTO Registrations (password, user_type) VALUES ('test987', 'Supplier');
INSERT INTO Registrations (password, user_type) VALUES ('user123', 'Supplier');
INSERT INTO Registrations (password, user_type) VALUES ('sup123', 'Supplier');
*/
select * from Registrations;

/*
INSERT INTO Customers (customer_id, customer_name, address, phone_number, email, activity_status)
VALUES (2, 'Ahmed Ali', N'Block-A DHA Phase 8', N'333-1234566', N'ali.ahmed@email.com', 'Active');
INSERT INTO Customers (customer_id, customer_name, address, phone_number, email, activity_status)
VALUES (5, 'Saad Ashar', N'Block-18 FB Area',  N'334-2222567', 'saad.ashar123@email.com', 'Inactive');
INSERT INTO Customers (customer_id, customer_name, address, phone_number, email, activity_status)
VALUES (6, 'Aftab Anwar', N'212-G Emerald Towers',  N'393-1234888', 'anwar.aftab987@email.com', 'Active');
*/
select * from customers;

/*
INSERT INTO Employees (employee_id, employee_name, address, phone_number, email, date_of_birth, designation, department, led_by, salary)
VALUES (1, 'Ali Khan', 'House No. 12, Street 34, Islamabad', N'333-1234567', 'ali.khan@email.com', '1985-08-10', 'Manager', 'IT', NULL, 60000.00);
INSERT INTO Employees (employee_id, employee_name, address, phone_number, email, date_of_birth, designation, department, led_by, salary)
VALUES (3, 'Fatima Ahmed', 'Flat No. 5, Karachi', N'333-9876543', 'fatima.ahmed@email.com', '1990-03-22', 'Team Lead', 'Sales', 1, 50000.00);
INSERT INTO Employees (employee_id, employee_name, address, phone_number, email, date_of_birth, designation, department, led_by, salary)
VALUES (4, 'Sohail Malik', 'Village No. 8, Lahore', N'333-5551212', 'sohail.malik@email.com', '1988-11-15', 'Assistant', 'Sales', 1, 70000.00);
INSERT INTO Employees (employee_id, employee_name, address, phone_number, email, date_of_birth, designation, department, led_by, salary)
VALUES (7, 'Ali Khan', '519 Gulshan-e-Iqbal', N'343-9991212', 'khan.ali@email.com', '2000-10-29', 'Warehouse Manager', 'Warehouse', 3, 20000.00);
*/
SElect * from Employees;

/*
INSERT INTO Category (category_name, category_description)
VALUES ('Infant Formula', 'Specially formulated for infants and young children.');
INSERT INTO Category (category_name, category_description)
VALUES ('Tea Whitener', 'Ideal for making creamy tea with a rich taste.');
INSERT INTO Category (category_name, category_description)
VALUES ('Powdered Milk', 'Versatile and convenient powdered milk for various culinary uses.');
INSERT INTO Category (category_name, category_description)
VALUES ('Yogurt', 'Delicious and nutritious yogurt for a healthy diet.');
*/
Select * from Category;

/*
INSERT INTO Products (product_name, category_id, price, continuity_status)
VALUES ('BabyGrow Premium', 1, 19.99, 'True');
INSERT INTO Products (product_name, category_id, price, continuity_status)
VALUES ('CreamyBlend', 2, 5.99, 'True');
INSERT INTO Products (product_name, category_id, price, continuity_status)
VALUES ('DairyMagic Milk Powder', 3, 12.99, 'False');
INSERT INTO Products (product_name, category_id, price, continuity_status)
VALUES ('NutriBabies Stage 1', 1, 14.99, 'True');
INSERT INTO Products (product_name, category_id, price, continuity_status)
VALUES ('DesiDahi', 4, 19.99, 'True');
INSERT INTO Products (product_name, category_id, price, continuity_status)
VALUES ('EconoMilk', 3, 9.99, 'False');
INSERT INTO Products (product_name, category_id, price, continuity_status)
VALUES ('PureChai', 2, 8.99, 'True');
*/
Select * from products;
/*
INSERT INTO Orders (customer_id, employee_id, order_date, required_date, delivery_status, shipped_date)
VALUES (5, 3, '2023-06-29', '2023-07-15', 'Delivered', '2023-07-16');
INSERT INTO Orders (customer_id, employee_id, order_date, required_date, delivery_status, shipped_date)
VALUES (6, NULL, '2023-01-19', '2023-08-22', 'Pending', NULL);
INSERT INTO Orders (customer_id, employee_id, order_date, required_date, delivery_status, shipped_date)
VALUES (2, 1, '2023-01-07', '2023-03-13', 'Delivered', '2023-02-22');
INSERT INTO Orders (customer_id, employee_id, order_date, required_date, delivery_status, shipped_date)
VALUES (5, 3, '2023-05-08', '2023-05-15', 'Delivered', '2023-05-10');
INSERT INTO Orders (customer_id, employee_id, order_date, required_date, delivery_status, shipped_date)
VALUES (2, NULL, '2023-11-01', '2023-11-10', 'Pending', NULL);
*/
select * from Orders;
/*
INSERT INTO Order_Details (order_id, product_id, quantity, price)
VALUES (1, 1, 2, 39.98),
       (1, 3, 1, 12.99);
INSERT INTO Order_Details (order_id, product_id, quantity, price)
VALUES (2, 5, 3, 59.97),
	   (2, 6, 1, 9.99),
       (2, 7, 5, 44.95);
INSERT INTO Order_Details (order_id, product_id, quantity, price)
VALUES (3, 2, 1, 5.99),
	   (3, 4, 3, 44.97);
INSERT INTO Order_Details (order_id, product_id, quantity, price)
VALUES (4, 1, 7, 139.93),
	   (4, 2, 4, 23.96),
	   (4, 5, 1, 19.99),
	   (4, 6, 1, 9.99),
       (4, 3, 2, 25.98);
INSERT INTO Order_Details (order_id, product_id, quantity, price)
VALUES (5, 4, 1, 14.99);
*/
select * from Order_Details

/*
INSERT INTO Warehouse (warehouse_address, warehouse_city, warehouse_phone_number, warehouse_lead)
VALUES ('123 Storage Street', 'Karachi', N'555-1234567', 7);
INSERT INTO Warehouse (warehouse_address, warehouse_city, warehouse_phone_number, warehouse_lead)
VALUES ('786 Johar Street', 'Islamabad', N'215-1234567', 7);
*/
Select * from Warehouse;
/*
INSERT INTO Product_Inventory (product_id, warehouse_id, product_stock)
VALUES (1, 1, 1000);
INSERT INTO Product_Inventory (product_id, warehouse_id, product_stock)
VALUES (2, 1, 1500);
INSERT INTO Product_Inventory (product_id, warehouse_id, product_stock)
VALUES (3, 2, 1000);
INSERT INTO Product_Inventory (product_id, warehouse_id, product_stock)
VALUES (4, 1, 2000);
INSERT INTO Product_Inventory (product_id, warehouse_id, product_stock)
VALUES (5, 2, 2000);
INSERT INTO Product_Inventory (product_id, warehouse_id, product_stock)
VALUES (6, 2, 1000);
INSERT INTO Product_Inventory (product_id, warehouse_id, product_stock)
VALUES (7, 1, 1500);
*/
Select * from Product_inventory;

/*
INSERT INTO Suppliers (supplier_id, supplier_name, address, phone_number, email, activity_status)
VALUES (9, 'Al Rehman Suppliers', N'123 Main Street', N'555-1234567', N'al.rehman.suppliers@email.com', 'Active');
INSERT INTO Suppliers (supplier_id, supplier_name, address, phone_number, email, activity_status)
VALUES (10, 'Quality Materials .Co', N'456 Oak Avenue', N'555-9876543', N'quality.materials.co@email.com', 'Inactive');
INSERT INTO Suppliers (supplier_id, supplier_name, address, phone_number, email, activity_status)
VALUES (11, 'Mr Suppliers', N'789 Maple Lane', N'555-5678901', N'mr.supplies@email.com', 'Active');
*/
select * from Suppliers;

/*
INSERT INTO Raw_Material (material_name, supplier_id, cost, quality_metric)
VALUES ('Milk', 9, 5.00, 'High Quality');
INSERT INTO Raw_Material (material_name, supplier_id, cost, quality_metric)
VALUES ('Wheat', 10, 7.00, 'Medium Quality');
INSERT INTO Raw_Material (material_name, supplier_id, cost, quality_metric)
VALUES ('Egg', 11, 4.00, 'High Quality');
INSERT INTO Raw_Material (material_name, supplier_id, cost, quality_metric)
VALUES ('Sugar', 9, 10.00, 'High Quality');
*/

select * from Raw_material;
Select * from Warehouse;

/*
INSERT INTO Products_RawMaterial (product_id, material_id, material_used)
VALUES (1, 1, 5), (1, 2, 8), (1, 3, 10);
INSERT INTO Products_RawMaterial (product_id, material_id, material_used)
VALUES (2, 2, 7), (2, 4, 12);
INSERT INTO Products_RawMaterial (product_id, material_id, material_used)
VALUES (3, 1, 3), (3, 3, 6), (3, 4, 9);
INSERT INTO Products_RawMaterial (product_id, material_id, material_used)
VALUES (4, 1, 4), (4, 2, 8), (4, 3, 11), (4, 4, 15);
INSERT INTO Products_RawMaterial (product_id, material_id, material_used)
VALUES (5, 1, 2), (5, 4, 10);
INSERT INTO Products_RawMaterial (product_id, material_id, material_used)
VALUES (6, 1, 5);
INSERT INTO Products_RawMaterial (product_id, material_id, material_used)
VALUES (7, 1, 3), (7, 4, 7);
*/
select * from Products_rawmaterial;

/*
INSERT INTO Material_Inventory (material_id, warehouse_id, material_stock)
VALUES (1, 1, 5000);
INSERT INTO Material_Inventory (material_id, warehouse_id, material_stock)
VALUES (2, 2, 4000);
INSERT INTO Material_Inventory (material_id, warehouse_id, material_stock)
VALUES (3, 1, 5000);
INSERT INTO Material_Inventory (material_id, warehouse_id, material_stock)
VALUES (4, 2, 4500);
*/

select * from Material_inventory;

/*
INSERT INTO Manufacturing (product_id, production_date, expiry_date)
VALUES (1, '2023-01-01', '2023-12-31'),
       (1, '2023-02-01', '2023-12-31'),
       (1, '2023-03-01', '2023-12-31');
INSERT INTO Manufacturing (product_id, production_date, expiry_date)
VALUES (2, '2023-01-15', '2024-01-15'),
       (2, '2023-02-15', '2024-01-15');
INSERT INTO Manufacturing (product_id, production_date, expiry_date)
VALUES (3, '2023-03-10', '2024-03-10');
INSERT INTO Manufacturing (product_id, production_date, expiry_date)
VALUES (4, '2023-02-28', '2024-02-28');
INSERT INTO Manufacturing (product_id, production_date, expiry_date)
VALUES (5, '2023-01-10', '2024-01-10');
INSERT INTO Manufacturing (product_id, production_date, expiry_date)
VALUES (6, '2023-03-05', '2024-03-05');
INSERT INTO Manufacturing (product_id, production_date, expiry_date)
VALUES (7, '2023-01-20', '2023-12-20'),
       (7, '2023-02-20', '2023-12-20');
*/

select * from Manufacturing;