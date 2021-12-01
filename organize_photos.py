import os


def extract_place(file_name):
    place_name = file_name.split('_')
    return place_name[1]


def make_place_directory(places_list):
    for plc in places_list:
        os.mkdir(plc)


def organize_photos(directory):
    os.chdir(directory)
    originals = os.listdir()
    places = list()
    for filename in originals:
        place = extract_place(filename)
        if place not in places:
            places.append(place)

    make_place_directory(places)  # creates the directory
    for filename in originals:
        place = extract_place(filename)
        os.rename(filename, os.path.join(place, filename))  # moves the files by renaming them


if __name__ == '__main__':
    organize_photos("/Users/decagon/data_structure_and_algo/Photos")
