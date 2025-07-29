wifi_client = SearchClient(
    endpoint=endpoint,
    index_name="wifi-index",
    credential=AzureKeyCredential(key)
)

wifi_docs = [
    {
      "docId": "1",
      "content": "Complimentary free wifi and high-speed internet throughout the building."
    },
    {
      "docId": "2",
      "content": "Business center offers wired internet and wi-fi access 24/7."
    },
    {
      "docId": "3",
      "content": "All rooms include ultra-fast wi fi for streaming and gaming."
    }
]

result = wifi_client.upload_documents(documents=wifi_docs)
print("Wi-Fi docs upload:", result[0].status_code == 201)
