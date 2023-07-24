from googlesearch import search #importing package

data = input("search: ")#data input
num_results = 5#number of possible results

# Store the search results as objects in a list using list comprehension
search_results = [{'url': i, 'title': i.split('/')[-1], 'description': ''} for i in search(data, num_results=num_results)]

for result in search_results:#printing outputs
    print(result['url'])#getting url
    print(result['title'])#getting title
    print(result['description'])#getting description
