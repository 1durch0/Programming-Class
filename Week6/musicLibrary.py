songs = []
genreCount = {}

while True:
    title = input("Put your new song here:\n")
    genre = input("... and put your song's genre here:\n")
    if title.lower() == "exit" or genre.lower() == "exit":
        break

    songs.append((title, genre))
    genreCount[genre] = genreCount.get(genre, 0) + 1
    print(f"Current genre counts: {genreCount}")

    another = input("\nDo you want to add another song? (yes/no)\n").lower()
    if another not in ("yes", "y"):
        print("\n===YOUR MUSIC LIBRARY ===")
        for i, song in enumerate(songs, start=1):
            print(f"{i}. Title: {song[0]}, Genre: {song[1]}")
        print("\n===YOUR GENRES===\n")
        for genre in genreCount:
            print({genreCount[genre]}, f"songs of genre: {genre}")

        break
