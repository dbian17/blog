import boto3
from view_model.place import Place


client = boto3.resource('dynamodb')

# Get all place objects from dynamoDb
def get_places():
    table = client.Table('Places')
    response = table.scan()
    places = [Place(**response_item_dict) for response_item_dict in response['Items']]
    return places

# Add place object into dynamoDb
def add_place(place: Place):

    print(place)
    table = client.Table('Places')
    # response = table.put_item(Item=place.__dict__)

    # print(response)

