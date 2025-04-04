from api.view_model.place import Place
from api.service_client.dynamo import dynamo_service_client

# Load view for all places
def load_places():
    # return dynamo_service_client.get_places()
    return []
    

# Load view structure
def load(name: str):
    return Place(name, 6.5, ["sha"], "mid")
