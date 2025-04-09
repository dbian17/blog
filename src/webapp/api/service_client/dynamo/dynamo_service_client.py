import boto3
from api.view_model.place import Place

client = boto3.resource('dynamodb')

# Get all place objects from dynamoDb
def get_places():
    table = client.Table('Places')
    response = table.scan()
    places = [Place(**response_item_dict) for response_item_dict in response['Items']]
    return places

def get_place(place_name):

    table = client.Table('Places')
    key = {'name': place_name}
    response = table.get_item(Key=key)
    
    if 'Item' in response:
        response_item_dict = response['Item']
        return Place(**response_item_dict)
    else:
        return None

# Add place object into dynamoDb
def add_place(place: Place):
    place_dict = place.__dict__
    present_attributes = {key: value for key, value in place_dict.items() if value is not None and key != 'name'}

    update_expression = 'SET {}'.format(','.join(f'{attribute_name}=:{attribute_name}' for attribute_name in present_attributes))
    expression_attribute_values = {f':{attribute_name}': attribute_value for attribute_name , attribute_value in present_attributes.items()}

    table = client.Table('Places')
    response = table.update_item(
        Key={'name': place.name},
        UpdateExpression=update_expression,
        ExpressionAttributeValues=expression_attribute_values
    )

    return response['ResponseMetadata']['HTTPStatusCode']
