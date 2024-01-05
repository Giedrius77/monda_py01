""" Komandinio/individualaus darbo užduotis
===[ Muzikos Albumas ]===

Reikalavimai:

* Žodynas albumas turi turėti atlikėją ir pavadinimą, gali turėti ir kitų atributų
* Albumo žodyne sukurkite takelių (dainų) sąrašą, kur kiekvienas takelis yra žodynas, talpinantis eilės numerį, pavadinimą ir trukmę sekundėmis. 
** Bonus: trukmės įvedimas "minutės:sekundės" formatu (žmogui suprantamu).
* Programa turi leisti vartotojui užpildyti/pakeisti albumo informaciją (pavadinimą, atlikėją, ...)
* Programa turi leisti vartotojui sukurti/ištrinti takelį, užpildant takelio informaciją (pavadinimą, trukmę)
* Galimybė peržiūrėti albumą, išspausdinant takelių kiekį ir bendrą jų trukmę šalia kitų atributų.
* Peržiūrėti albumo dainas. Bonus: išrūšiuotas pagal eilės numerį. Takelio trukmė turi būti pateikta žmogui suprantama laiko išraiška.

Pastabos:
* Stenkitės nekartoti kodo - funkcionalumui, kuriam kodas kartotųsi, parašykite atskiras funkcijas ir jas panaudokite kelis kartus kur reikia.
"""

def create_album():
    album = {}

    # Get album information from the user
    artist = input("Enter the artist name: ")
    title = input("Enter the album title: ")

    # Create a list to store the tracks
    tracks = []

    # Get track information from the user
    num_tracks = int(input("Enter the number of tracks: "))
    for i in range(num_tracks):
        track = {}
        track["sequence"] = i + 1
        track["title"] = input("Enter track title: ")
        track["duration"] = input("Enter track duration: ")
        tracks.append(track)

    # Add artist, title, and tracks to the album dictionary
    album["artist"] = artist
    album["title"] = title
    album["tracks"] = tracks

    return album

# Create an album
album = create_album()

# Print the album information
print("\nAlbum Information:")
print("Artist:", album["artist"])
print("Title:", album["title"])
print("Tracks:")
for track in album["tracks"]:
    print("Sequence:", track["sequence"])
    print("Title:", track["title"])
    print("Duration:", track["duration"])
    print()

