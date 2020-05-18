# # TOP_CATEGORIES = [{"id": 3}]

# # items = set({"id": 3})


# # result = set(filter(lambda category: category['id'] in TOP_CATEGORIES, items))
# # print(f"first tops: {result}")

# # remaining = set(filter(lambda category: category['id'] not in TOP_CATEGORIES, items))
# # print(f"remaining tops: {remaining}")

# TOP_CATEGORIES = [{"id": 3}, {"id": 7}, {"id": 1}]
# items = [{"id": 2}, {"id": 1}]
# top = 2

# def find_category(top_category, items):
#     for item in items:
#         if top_category["id"] == item["id"]:
#             return item

# result = []
# for top_category in TOP_CATEGORIES:
#     category = find_category(top_category, items)
#     if category:
#         result.append(category) 

# # list the remaining
# for remaining_category in items:
#     category = find_category(remaining_category, result)
#     if category is None:
#         result.append(remaining_category)

# print(f"result: {result}")

# # keys = {"id"}

# # l = list(map(lambda category: {key:value for key, value in category.items() if key in keys}, TOP_CATEGORIES))
# # print(l)

from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

ratio = similar("Bruno", "Brunos")
print(f"similar: {ratio}")