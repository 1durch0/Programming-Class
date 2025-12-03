import csv
import json

items = []

# reading an seperating file --> only works with correctly formatted files --> formatting files would be a sepperate task
with open("/Users/1durch0/Studium/HTW Cyber Security & Business/1. Semester/Programming/Programming-Class/Week7/prices.txt", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        name = row[0].strip()
        price = float(row[1])
        category = row[2].strip()
        quality = row[3].strip()

        items.append({
            "name": name,
            "price": price,
            "category": category,
            "quality": quality
        })

def calculateFinalPrices():
    output = []
    
    for item in items:
        basePrice = item["price"]
        category = item["category"]
        quality = item["quality"]

        priceAfterCatDiscount = checkCatDiscount(basePrice, category)
        finalPrice = TierDiscount(priceAfterCatDiscount, quality)

        output.append({
            "name": item["name"],
            "original_price": round(basePrice, 2),
            "final_price": round(finalPrice, 2),
            "category": category,
            "quality": quality
        })

    # write to json file
    with open("/Users/1durch0/Studium/HTW Cyber Security & Business/1. Semester/Programming/Programming-Class/Week7/output.json", "w") as json_file:
        json.dump(output, json_file, indent=4)

    print("JSON file 'output.json' successfully created!")

def checkCatDiscount(price, category):    
    match category.lower():
        case "electronics":
            newPrice = price * 0.90
            return newPrice  # 10% discount
        case "clothing":
            newPrice = price * 0.85
            return newPrice  # 15% discount
        case "groceries":
            newPrice = price * 0.95
            return newPrice  # 5% discount
        case _:
            newPrice = price * 1.0
            return newPrice  # No discount
        
def TierDiscount(price, tier):
    match tier.lower():
        case "premium":
            finalPrice = price * 0.95
            return finalPrice  # 5% additional discount
        case "standard":
            finalPrice = price * 1.00
            return finalPrice  # no discount, still here for later use
        case "basic":
            finalPrice = price * 0.98
            return finalPrice  # 2% additional discount
        case _:
            finalPrice = price * 1.0
            return finalPrice  # No discount
        
calculateFinalPrices()