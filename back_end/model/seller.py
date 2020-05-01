insert_seller = "INSERT INTO seller (code, supplier, receipt_date, value_product, price, first_value) VALUES (?, '?', '?', ?, ?, ?);"

select_all_sellers = "SELECT * FROM seller"
select_seller_by_id = "SELECT * FROM seller WHERE id_wh = ?"
select_seller_id = "SELECT id_wh from seller"

update_seller_by_id = "UPDATE seller SET code = ?, supplier = '?', receipt_date = '?', value_product = ?, price = ?, first_value = ? WHERE id_wh = ?"

delete_seller_by_id = "DELETE FROM seller WHERE id_wh = ?"
