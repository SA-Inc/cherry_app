insert_product = "INSERT INTO product (value_product, date_sell, price_prod, id_sell, id_wh, code) VALUES(?, ?, ?, ?, ?, ?)"

select_all_products = "SELECT * FROM product"
select_product_by_id = "SELECT * FROM product WHERE id_prod = ?"

update_product_by_id = "UPDATE product SET value_product = ?, date_sell = ?, price_prod = ?, id_sell = ?, id_wh = ?, code = ? WHERE id_prod = ?"

delete_product_by_id = "DELETE FROM product WHERE id_prod = ?"