movies = open('movies.txt')
movie = movies.read()
movie = movie.lower()


def clean(data, irrelevant):
    for word in irrelevant:
        if word in data:
            data = data.replace(word, ' ')
    return data


def search(X1, word):
    ans = 0
    ans_val = []

    for i in X1:
        if word in i:
            ans = ans + 1
            ans_val.append(i)

    return ans, ans_val


irrelevant_words = {".", ',', '"\"', ";", ":", " "}
cleanData = clean(movie, irrelevant_words)


document = cleanData.splitlines()


def split_line(document):
    document = document.split()
    for word in document:
        print(document)

document = split_line(document)
#for terms in document:
    #term = terms.split()


# print(docId[0])
# print(docId)

#for docId in range(len(document)):
    #print(document, end=str(docId))
    #print(" ")

word = input("Enter your search : ")
# Assume this is a document

# print(data, '\n', word)

No_of_result, result_val = search(document, word)

for x in result_val:
    print('\n', '================================== New result =================================', '\n')
    print(x)
#
print('No_of_result = ', No_of_result)


