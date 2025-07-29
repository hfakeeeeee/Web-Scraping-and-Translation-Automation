from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential

endpoint = "https://<your-search-service>.search.windows.net"
key = "<your-admin-key>"

hotel_client = SearchClient(
    endpoint=endpoint,
    index_name="hotels-index",
    credential=AzureKeyCredential(key)
)

hotels = [
    {
      "hotelId": "1",
      "hotelName": "Puppy Paradise",
      "description": "A dog-friendly hotel with puppy play areas and canine concierge.",
      "address": {
        "streetAddress": "101 Barker St",
        "city": "Seattle",
        "stateProvince": "WA",
        "country": "USA"
      }
    },
    {
      "hotelId": "2",
      "hotelName": "Urban Retreat",
      "description": "Modern rooms in downtown with free coffee and latte bar.",
      "address": {
        "streetAddress": "202 Center Ave",
        "city": "Portland",
        "stateProvince": "OR",
        "country": "United States"
      }
    },
    {
      "hotelId": "3",
      "hotelName": "Mountain Lodge",
      "description": "Cozy cabin near trails. Great for hikers and nature lovers.",
      "address": {
        "streetAddress": "303 Pine Rd",
        "city": "Denver",
        "stateProvince": "CO",
        "country": "United States of America"
      }
    }
]

result = hotel_client.upload_documents(documents=hotels)
print("Hotels upload:", result[0].status_code == 201)
