import csv

top_grossing = open('imdb-top-grossing.csv', 'r', encoding='utf-8')
rank_title = []
for line in top_grossing:
    line_list = line.split(',')
    # print just the title of the movie to see what info looks like
    print(line_list[0], line_list[1])
top_grossing.close()


top_grossing.close()

top_casts = open('imdb-top-casts.csv', 'r', encoding='utf-8')
for line in top_casts:
    line_list = line.split(',')
    # print title, director and actor to see what info looks like
    print('Title: {} Dir: {} First Actor: {}'.format(
        line_list[0], line_list[2], line_list[3]))
top_casts.close()
