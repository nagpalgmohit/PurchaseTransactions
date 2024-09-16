import re
from jsonschema import validate, ValidationError, SchemaError

class TransactionValidator:
    @staticmethod
    def validate_item_id(item_id):
        if not item_id or item_id == 0:
            return False, "Item id cannot be empty or zero."
        elif not str(item_id).isdecimal():
            return False, "The item id must adhere to the following criteria: It can consist of only positive digits. It cannot consist of decimals, negatives or zero."
        return True, None

    @staticmethod
    def validate_username(username):
        if not username:
            return False, "Username cannot be empty."
        pattern_check_username = r"^(?!^\d+$)([A-Za-z][A-Za-z0-9._%+-]*@[A-Za-z0-9.-]+\.[A-Za-z]{2,}|[A-Za-z][A-Za-z0-9._%+-]*)$"
        if re.match(pattern_check_username, username):
            return True, None
        else:
            return False, "The username must adhere to the following criteria: It can consist of alphanumeric characters, alphabets, or be in email format. It cannot consist solely of digits or spaces."

    @staticmethod
    def validate_purchase_price(purchase_price):
        if not purchase_price:
            return False, "Purchase price cannot be empty or zero."
        pattern = r"^(?!0\.0$)\d+\.\d{2}$"
        if re.match(pattern, str("{:.2f}".format(float(purchase_price)))):
            return True, None
        else:
            return False, "The purchase price must adhere to the following criteria: It can consist of only positive digits with decimals. It cannot consist of negatives or zero."
    
    @staticmethod
    def validate_json(data, error_messages,schema):
        try:
            validate(instance=data, schema=schema)
        except ValidationError as e:
        # Handle specific validation errors
            field = e.path[0] if e.path else 'unknown'
            error_type = e.validator

            if error_type == 'required':
                return False, error_messages['required'].format(field=e.message.split("'")[1])
            elif error_type == 'type':
                return False, error_messages['type'].format(field=field, type=schema['properties'][field]['type'])
            elif error_type == 'additionalProperties':
                return False, error_messages['additionalProperties'].format(field=e.message.split("'")[1])
            else:
                return False, str(e)
        except SchemaError as e:
            return False, f"Invalid schema: {str(e)}"
        return True, None
