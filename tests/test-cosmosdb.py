from azure.cosmos import CosmosClient
import os

url = os.environ['DASHBOARD_COSMOS_ACCOUNT_URI']
key = os.environ['DASHBOARD_PRIMARY_KEY']

client = CosmosClient(url, key)

database_name = 'stock-data'
database = client.create_database_if_not_exists(id=database_name)

container_name = 'overall-data'
container = database.create_container_if_not_exists(
    id=container_name, 
    partition_key=PartitionKey(path="/sector"),
    offer_throughput=400
)

query = "SELECT * FROM c WHERE c.symbol IN ('TWTR', 'PTR')"

items = list(container.query_items(
    query=query,
    enable_cross_partition_query=True
))

request_charge = container.client_connection.last_response_headers['x-ms-request-charge']

print(f'Query returned {len(items)} items. Operation consumed {request_charge} request units')
print(items)