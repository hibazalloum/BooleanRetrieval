movies = open('movies.txt')
movie = movies.read()
movie = movie.lower()


def clean(data, irrelevant):
    for word in irrelevant:
        if word in data:
            data = data.replace(word, ' ')
    return data


irrelevant_words = {".", ',', '"\"', ";", ":", " "}
cleanData = clean(movie, irrelevant_words)

document = cleanData.splitlines()
# print(docId[0])
# print(docId)

for docId in range(len(document)):
     #print(document, end=str(docId))
    print(" ")


def intersect(p1, p2):
    ans = 0
    ans_val = []
    for i in p1:
        for j in p2:
            if i == j:
                ans = ans + 1
                ans_val.append(i)
    return ans, ans_val
