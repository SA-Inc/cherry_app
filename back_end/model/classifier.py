insert_classifier = 'INSERT INTO classifier (code, name_prod) VALUES (?, ?)'

select_all_classifiers = 'SELECT * FROM classifier'
select_classifier_by_code = 'SELECT * FROM classifier WHERE code = ?'

update_classifier_by_code = 'UPDATE classifier SET code = ?, name_prod = ? WHERE code = ?'

delete_classifier_by_code = 'DELETE FROM classifier WHERE code = ?'
