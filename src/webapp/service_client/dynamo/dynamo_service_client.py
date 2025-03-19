import boto3
from view_model.place import Place


client = boto3.resource('dynamodb')

def add_place(place: Place):

    table = client.Table('Places')
    response = table.put_item(Item=place.__dict__)

    print(response)

