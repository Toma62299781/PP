# Define a procedure, add_to_index,
# that takes 3 inputs:

# - an index: [[<keyword>,[<url>,...]],...]
# - a keyword: String
# - a url: String

# If the keyword is already
# in the index, add the url
# to the list of urls associated
# with that keyword.

# If the keyword is not in the index,
# add an entry to the index: [keyword,[url]]

index = []


def add_to_index(p,keyword,url):
    # check = 0
    for element in p:
        if keyword in element:
            p[p.index(element)][1].append(url)
            # check = 1
            return # Using return to break the procedure, this will not using check

    # if check == 0:
            # p.append([keyword, [url]]) This is the method uses check to check whether should append new entry to index
    p.append([keyword, [url]])










add_to_index(index,'udacity','http://udacity.com')
add_to_index(index,'computing','http://acm.org')
add_to_index(index,'udacity','http://npr.org')
print index
#>>> [['udacity', ['http://udacity.com', 'http://npr.org']],
#>>> ['computing', ['http://acm.org']]]
