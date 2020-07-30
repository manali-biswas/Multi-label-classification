import re
def clean(query):
    
    words = ['hi','hello','i','hey','we','you','they','the','a','an','it','am']

    string = (" ".join([i.lower() for i in re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",query).split() if i.lower() not in words ]).lower())
    return string