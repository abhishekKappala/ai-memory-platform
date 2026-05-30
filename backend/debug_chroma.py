from app.services.vector_service import get_collection

data = get_collection().get()

print("TOTAL VECTORS:")
print(len(data["ids"]))

print(data)