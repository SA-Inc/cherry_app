insert_classifier = 'INSERT INTO classifer (code) VALUES (?)'

select_all_classifiers = 'SELECT code FROM classifer'
select_classifier_by_code = 'SELECT code FROM classifer WHERE code = ?'

update_classifier_by_code = 'UPDATE classifer SET code = ? WHERE code = ?'

delete_classifier_by_code = 'DELETE FROM classifer WHERE code = ?'
