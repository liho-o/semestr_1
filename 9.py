playlist = []
print("Введите плей-лист папы:")
for song in range(5):
    song = input()
    playlist.append(song)
print('Плей-лист мамы:')
for song in range(5):
    print(playlist.pop())