import boto3
from api.view_model.place_data import PlaceData
from api.view_model.place_review import PlaceReview

PLACE_DATA_TABLE_NAME = 'Place-Data'
PLACE_REVIEW_TABLE_NAME = 'Place-Reviews'

client = boto3.resource('dynamodb')

def get_place_table_key(place_name: str):
    return {'name': place_name}

# Get all place objects from dynamoDb and sorts based on rating
# Only return places with a rating stored in dynamoDb
def get_all_ranked_place_data(descending=True):
    table = client.Table(PLACE_DATA_TABLE_NAME)
    response = table.scan()
    places = [PlaceData(**response_item_dict) for response_item_dict in response['Items']]
    ranked_places = [place for place in places if place.rating != None]
    ranked_places.sort(key = lambda place: place.rating, reverse=descending)
    return ranked_places

# Get all place objects from dynamoDb
def get_all_place_data():
    table = client.Table(PLACE_DATA_TABLE_NAME)
    response = table.scan()
    places = [PlaceData(**response_item_dict) for response_item_dict in response['Items']]
    return places

def get_place_data(place_name):
    place_data_dict = get_item_from_table(PLACE_DATA_TABLE_NAME, get_place_table_key(place_name))
    if place_data_dict:
        return PlaceData(**place_data_dict)
    else:
        return None
    
def get_place_review(place_name):
    place_review_dict = get_item_from_table(PLACE_REVIEW_TABLE_NAME, get_place_table_key(place_name))
    if place_review_dict:
        return PlaceReview(**place_review_dict)
    else:
        return None

def get_item_from_table(table_name: str, key: dict):
    table = client.Table(table_name)
    response = table.get_item(Key=key)
    
    if 'Item' in response:
        return response['Item']
    else:
        return None

# Add place object into dynamoDb
def add_place(place_data: PlaceData, place_review: PlaceReview):
    data_response_code = add_place_data(place_data)
    review_response_code = add_place_review(place_review)
    return data_response_code == '200' and review_response_code == '200'

def add_place_data(place_data: PlaceData):
    place_data_dict = place_data.__dict__
    present_attributes = {key: value for key, value in place_data_dict.items() if value is not None and key != 'name'}
    if len(present_attributes) > 0:
        return add_attributes_to_table(PLACE_DATA_TABLE_NAME, get_place_table_key(place_data.name), present_attributes)
    else:
        return '200'

def add_place_review(place_review: PlaceReview):
    place_review_dict = place_review.__dict__
    present_attributes = {key: value for key, value in place_review_dict.items() if value is not None and key != 'name'}
    if len(present_attributes) > 0:
        return add_attributes_to_table(PLACE_REVIEW_TABLE_NAME, get_place_table_key(place_review.name), present_attributes)
    else:
        return '200'

def add_attributes_to_table(table_name: str, key: dict, attributes):
    update_expression = 'SET {}'.format(','.join(f'{attribute_name}=:{attribute_name}' for attribute_name in attributes))
    expression_attribute_values = {f':{attribute_name}': attribute_value for attribute_name , attribute_value in attributes.items()}

    table = client.Table(table_name)
    response = table.update_item(
        Key=key,
        UpdateExpression=update_expression,
        ExpressionAttributeValues=expression_attribute_values
    )

    return response['ResponseMetadata']['HTTPStatusCode']
