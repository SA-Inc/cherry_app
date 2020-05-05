insert_seller = "INSERT INTO seller (status, FIO, value_product) VALUES (?, ?, ?);"

select_all_sellers = "SELECT * FROM seller"
select_seller_by_id = "SELECT * FROM seller WHERE id_sell = ?"
select_seller_id = "SELECT id_sell FROM seller"

update_seller_by_id = "UPDATE seller SET status = ?, FIO = ?, value_product = ? WHERE id_sell = ?"

delete_seller_by_id = "DELETE FROM seller WHERE id_sell = ?"