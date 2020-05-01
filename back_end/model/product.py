insert_product = "INSERT INTO Product(name, description, price) VALUES(?, ?, ?)"

select_all_products = "SELECT * FROM Product"
select_product_by_id = "SELECT * FROM Product WHERE id = ?"

update_product_by_id = "UPDATE Product SET name = ?, description = ?, price = ? WHERE id = ?"

delete_product_by_id = "DELETE FROM Product WHERE id = ?"
