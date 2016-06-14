import csv
from operator import itemgetter
from math import sqrt


def read_sample_data(input_file):
    read_samples = []
    with open(input_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=";", quotechar="\"")
        reader = csv_reader
        next(reader)  # skip the header
        for row in reader:
            read_samples.append(tuple(row))  # add one tuple for each row
    return tuple(read_samples)


def get_max_values(sample_data):
    max_values = []
    # exclude the last value (because it's the score)
    for i in range(len(sample_data[0]) - 1):
        max_values.append(max(sample_data, key=lambda x: float(x[i]))[i])
    return tuple(max_values)


def get_min_values(sample_data):
    min_values = []
    # exclude the last value (because it's the score)
    for i in range(len(sample_data[0]) - 1):
        min_values.append(min(sample_data, key=lambda x: float(x[i]))[i])
    return tuple(min_values)


def normalize(sample, min_values, max_values):
    normalized_sample = []
    for i in range(len(sample) - 1):
        normalized_sample.append(
            (float(sample[i]) - float(min_values[i])) / float(max_values[i])
        )

    # copy the original score
    normalized_sample.append(int(sample[-1]))
    return tuple(normalized_sample)


def normalize_sample_data(sample_data):
    max_values = get_max_values(sample_data)
    min_values = get_min_values(sample_data)

    debug_print("Max values: {}".format(max_values))
    debug_print("Min values: {}\n".format(min_values))

    normalized_samples = []

    for sample in sample_data:
        normalized_samples.append(normalize(sample, min_values, max_values))

    return tuple(normalized_samples)


def calc_sqrt_distance(sample, w2bc):
    result = 0

    # exclude the last value (because it's the score)
    for i in range(len(sample) - 1):
        result += (float(sample[i]) - float(w2bc[i])) ** 2

    return (sample, sqrt(result))  # return a tuple


def get_nearest(candidates):
    # create an empty directory:
    score_count = {}

    # count the different scores
    for elem in candidates:
        score = int(elem[-1])
        if score not in score_count:
            score_count[score] = 1
        else:
            score_count[score] += 1

    debug_print("This is the score count:")
    if DEBUG:
        for key, value in score_count.items():
            debug_print("{} -> {}".format(key, value))
        print()

    return max(score_count, key=lambda i: score_count[i])


def debug_print(message):
    if DEBUG:
        print("[DEBUG] " + message)


# ------------------------------------ main --------------------------------- #

INPUT_FILE = "winequality-red.csv"
EXPECTED_SCORE = 6
NORMALIZE = False
DEBUG = True
FIND_SMALLEST_K = True

# Define a k (the k from KNN). k should be smaller than the sample size
# to kick out outliers. But big enough to get a good vote!
K = 500

# print some general information
print("# ------------------------------------------------------")
print("#  File = {}".format(INPUT_FILE))
print("#  K = {}".format(K))
print("#  Expected result = {}".format(EXPECTED_SCORE))
print("#  FIND_SMALLEST_K = {}".format(FIND_SMALLEST_K))
print("#  NORMALIZE = {}".format(NORMALIZE))
print("#  DEBUG = {}".format(DEBUG))
print("# ------------------------------------------------------\n")

# wine to be classified (original score: 6)
w2bc = (6, 0.31, 0.47, 3.6, 0.067, 18, 42, 0.99549, 3.39, 0.66, 11, "?")
debug_print("The wine to be classified: {}".format(w2bc))

# ...
sample_data = read_sample_data(INPUT_FILE)
debug_print("CSV file read! Size of the sample data set: {} rows\n".
            format(len(sample_data)))

# normalize the sample data if wanted
if NORMALIZE:
    sample_data = normalize_sample_data(sample_data)

# create an empty list to store the distances
distances = []

# calculate the distance between the known wines and the one
#   to be classified
for sample_wine in sample_data:
    distances.append(calc_sqrt_distance(sample_wine, w2bc))

# sort the list by the previously calculated distance
sorted_distances = sorted(distances, key=itemgetter(1))

debug_print("These are the top 10 candidates (this is just to show that "
            "sorting is working!):")

if DEBUG:
    for elem in sorted_distances[:10]:
        debug_print("{} -> {}".format(elem[0][len(elem) - 1], elem[1]))
    print("")

# get the K most likely candidates:
candidates = list(map(itemgetter(0), sorted_distances[:K]))

# find the smallest possible k or just get the score using the predefined K
nearest_score = -1
if FIND_SMALLEST_K:
    k = 0
    while k <= len(sample_data) and int(nearest_score) != EXPECTED_SCORE:
        k += 1
        # rewrite the candidate list, starting with k entries
        candidates = list(map(itemgetter(0), sorted_distances[:k]))
        # count the scores and derive a vote
        nearest_score = get_nearest(candidates)

    print("--------------------------------------------------------")
    if k <= len(sample_data):
        print("Smallest possible K = {}".format(k))
    else:
        print("Could not find a K between 0 and {}"
              " to  :-/".format(len(sample_data)))
else:
    nearest_score = get_nearest(candidates)

    print("--------------------------------------------------------")
    print("Nearest Score = " + str(nearest_score))

    if int(nearest_score) != EXPECTED_SCORE:
        print("... but this seems to be wrong :-/")
    else:
        print("Nearest score and expected score are matching!")

# -----------------------------------------------------------------------------
