from graph import Graph
import sys

start_word = 'hit'
end_word = 'cog'
first = [start_word[0], end_word[0]]
last = [start_word[-1], end_word[-1]]
length = len(start_word)
f = open("words.txt", 'r')
all_words_length = [word for word in f.read().splitlines()
                    if len(word) == length and word.islower()]
f.close()

gr = Graph()
for word in all_words_length:
    if word[0] in first and word[-1] in last:
        gr.add_vertex(word)
# queue to keep track
# compare current vertex against rest of vertices to find word one letter different from end_word
for v1 in gr.vertices:
    for v2 in gr.vertices:
        oneOff = 0
        for i in range(0, len(v1)):
            if v1[i] == v2[i]:
                oneOff += 1
        if oneOff == len(v1) - 1:
            gr.add_edge(v1, v2)

print(gr.bfs(start_word, end_word))
