from fuzzywuzzy import fuzz


def handler(event, context):
    print("Hello, World!")
    print(fuzz.ratio("this is a test", "this is a test!"))
