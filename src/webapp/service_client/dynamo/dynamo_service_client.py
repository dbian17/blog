import boto3
from view_model.place import Place


client = boto3.client('dynamodb')

def add_place(place: Place):
    print(client)
    print(place)
        # response = self.client.put_item(
        #     TableName='Places',
        #     Item={
        #         'string': {
        #             'S': 'string',
        #             'N': 'string',
        #             'B': b'bytes',
        #             'SS': [
        #                 'string',
        #             ],
        #             'NS': [
        #                 'string',
        #             ],
        #             'BS': [
        #                 b'bytes',
        #             ],
        #             'M': {
        #                 'string': {'... recursive ...'}
        #             },
        #             'L': [
        #                 {'... recursive ...'},
        #             ],
        #             'NULL': True|False,
        #             'BOOL': True|False
        #         }
        #     },
        # )

