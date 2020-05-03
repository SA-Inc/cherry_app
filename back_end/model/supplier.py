insert_supplier = "INSERT INTO supplier (company_name, bank, account_number, phone_number, email, id_wh) VALUES (?, ?, ?, ?, ?, ?);"

select_all_suppliers = "SELECT * FROM supplier"
select_supplier_by_id = "SELECT * FROM supplier WHERE id_sup = ?"
select_supplier_by_warehouse_id = "SELECT * FROM supplier WHERE id_wh = ?"

update_supplier_by_id = "UPDATE supplier SET company_name = ?, bank = ?, account_number = ?, phone_number = ?, email = ?, id_wh = ? WHERE id_sup = ?"

delete_supplier_by_id = "DELETE FROM supplier WHERE id_sup = ?"

count_total_suppliers = "SELECT COUNT(*) AS count FROM supplier"