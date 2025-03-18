import boto3
from webapp.view_model.place import Place


class DynamoServiceClient:
    client = boto3.client('dynamodb')

    def add_place(self, place: Place):
        print(place.asDict())
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

