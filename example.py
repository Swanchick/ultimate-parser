import parser

url = "https://swanchick.github.io/Swanchick-s-Software/index.html"

parse = parser.Parse(url)

# Get title from page
print(parse.get_title())

# Update parse
parse.update()

# Get all elements by name
for el in parse.find_element("img"):
    print(el.options)

# Update parse
parse.update()

# Find html elemnt by class
for el in parse.find_by_class("description"):
    print(el.name)
    print(el.options)


# Find html elemnt by id
# ps: This page don't have element, which have id option inside.
# for el in parse.find_by_id("sample-id"):
#     print(el.name)
#     print(el.options)

