count_total = """SELECT 'classifier' AS table_name, COUNT(*) AS row_count FROM classifier
	UNION
	SELECT 'product' AS table_name, COUNT(*) AS row_count FROM product
	UNION
	SELECT 'seller' AS table_name, COUNT(*) AS row_count FROM seller
	UNION
	SELECT 'supplier' AS table_name, COUNT(*) AS row_count FROM supplier
	UNION
	SELECT 'warehouse' AS table_name, COUNT(*) AS row_count FROM warehouse"""