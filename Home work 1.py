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
    j = 0
    index = []
    ans_val = []

    for i in X1:
        if word in i:
            index.append(j)
            ans = ans + 1
            ans_val.append(i)
        j = j + 1

    return ans, ans_val, index


irrelevant_words = {".", ',', '"\"', ";", ":", " "}
cleanData = clean(movie, irrelevant_words)

document = cleanData.splitlines()
words_split = []

for i in range(len(document)):
    a = document[i].split()
    words_split.append(a)

word = input("Enter your search : ")


No_of_result, result_val, index = search(document, word)

for x in result_val:
    print('\n', '================================== New result =================================', '\n')
    print(x)

print()
print('No_of_result = ', No_of_result, end=" ")
print('Document INDEX : ', index, end=" ")
print(" ")
print(' THE END ',end=" ")