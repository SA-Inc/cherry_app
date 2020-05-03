insert_classifier = 'INSERT INTO classifier (code) VALUES (?)'

select_all_classifiers = 'SELECT code FROM classifier'
select_classifier_by_code = 'SELECT code FROM classifier WHERE code = ?'

update_classifier_by_code = 'UPDATE classifier SET code = ? WHERE code = ?'

delete_classifier_by_code = 'DELETE FROM classifier WHERE code = ?'

count_total_classifiers = "SELECT COUNT(*) AS count FROM classifier"