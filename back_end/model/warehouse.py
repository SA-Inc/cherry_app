insert_warehouse = "INSERT INTO warehouse (code, supplier, receipt_date, value_product, price, first_value) VALUES (?, '?', '?', ?, ?, ?);"

select_all_warehouses = "SELECT * FROM warehouse"
select_warehouse_by_id = "SELECT * FROM warehouse WHERE id_wh = ?"
select_warehouse_id = "SELECT id_wh from warehouse"

update_warehouse_by_id = "UPDATE warehouse SET code = ?, supplier = '?', receipt_date = '?', value_product = ?, price = ?, first_value = ? WHERE id_wh = ?"

delete_warehouse_by_id = "DELETE FROM warehouse WHERE id_wh = ?"
