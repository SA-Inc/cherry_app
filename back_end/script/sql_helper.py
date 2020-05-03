from decimal import Decimal
from datetime import date, datetime

def get_columns_from_result(result_description):
	return [column[0] for column in result_description]

def sql_select_result_to_json(columns, data):
	if len(data) == 1:
		return [dict(zip(columns, row)) for row in data][0]
	else:
		return [dict(zip(columns, row)) for row in data]

def default(obj):
    if isinstance(obj, Decimal):
        return str(obj)
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError("Object of type '%s' is not JSON serializable" % type(obj).__name__)
