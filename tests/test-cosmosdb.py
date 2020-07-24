import os
from azure.cosmos import CosmosClient
import azure.cosmos.exceptions as Exceptions
import azure_config

url = azure_config.url
key = azure_config.key

client = CosmosClient(url, key)

databases = list(client.list_databases())

for database in databases:
    print(database['id'])

database = client.get_database_client(database="stock-data")
container = database.get_container_client(container="overall-data")

query = "SELECT * FROM c WHERE c.symbol IN ('TWTR', 'PTR')"

items = list(container.query_items(
    query=query,
    enable_cross_partition_query=True))

request_charge = container.client_connection.last_response_headers['x-ms-request-charge']

print(f'Query returned {len(items)} items. Operation consumed {request_charge} request units')