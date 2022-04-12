from http import HTTPStatus


def serialize_number(data):

    phone_number = data["phone"]
    
    not_number = ''.join([i for i in phone_number if not i.isdigit()])

    if phone_number[0] != "(" or phone_number[3] != ")" or phone_number[9] != "-" or len(phone_number) != 14 or not_number != "()-":

        return {
            "Error": {"Message":"Incorrect format phone number"},
            "Example of current number format": {"phone": "(00)00000-0000"}
        }, HTTPStatus.BAD_REQUEST

    return False

def possible_key_error(data):
    return {
            "Error": {"Message":"Incorrect format key"},
            "Example of current key format": {
                "name": "John Doe",
                "email": "john@email.com",
                "phone": "(41)90000-0000"
            }
        }, HTTPStatus.BAD_REQUEST
    