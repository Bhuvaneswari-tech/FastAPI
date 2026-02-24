import json
from datetime import datetime, timedelta

# Sample JSON data
api_response = '''
{
  "order_id": "ORD-2026-001",
  "customer": "Arun Kumar",
  "placed_at": "2026-02-23T09:15:00",
  "items": [
    {"product": "Laptop",  "qty": 1, "price": 55000},
    {"product": "Headset", "qty": 1, "price": 2500}
  ],
  "status": "confirmed"
}
'''
# step1: Parse JSON response
#json.loads()   → JSON string  →  Python dict
order = json.loads(api_response)

#step 2: convert string to datetime object
placed_at = datetime.fromisoformat(order["placed_at"])

#step 3 - Business logic with datetime
estimated_delivery = placed_at + timedelta(days=3)
total = sum(item["qty"] * item["price"] for item in order["items"])
print(total)

#step 4 - Build response dictionary
order_summary = {
    "order_id": order["order_id"],
    "customer": order["customer"],
    "order_date": placed_at.strftime("%Y-%m-%d %H:%M"),
    "estimated_delivery": estimated_delivery.strftime("%Y-%m-%d"),
    "total":             f"₹{total:,}",
    "status": order["status"].upper()
}

#json.dumps()   → Python dict  →  JSON string
print(json.dumps(order_summary, indent=2, ensure_ascii=False))