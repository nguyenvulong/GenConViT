import os
import csv

# Define filenames for the input and the three output CSV files
csv_dir = "../../full_datasets/prediction_results/genconvit"
input_filename = 'result/scores.txt'
real_csv_filename = os.path.join(csv_dir, "prediction_real.csv")
fake_csv_filename = os.path.join(csv_dir, "prediction_fake.csv")
fake_custom_csv_filename = os.path.join(csv_dir, "prediction_fake_custom.csv")

# Initialize the lists to hold categorized scores
real_scores = []
fake_scores = []
fake_custom_scores = []

# Function to process line and categorize scores into appropriate lists
def categorize_and_store(line):
    video, score = line.split()
    vid_type, vid_id = video.split('_')
    vid_id = int(vid_id.split('.')[0])  # Extract id as an integer
    score = float(score)

    if vid_type == 'real' and 0 <= vid_id <= 250:
        real_scores.append([vid_id, score, score])
    elif vid_type == 'fake' and 0 <= vid_id <= 250:
        fake_scores.append([vid_id, score, score])
    elif vid_type == 'fake' and 251 <= vid_id <= 266:
        fake_custom_scores.append([vid_id, score, score])

# Read the input file and process each line
with open(input_filename, 'r') as file:
    for line in file:
        categorize_and_store(line.strip())

# Function to write to CSV file
def write_to_csv(filename, data):
    data.sort()  # Sort by 'id' before writing
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)


# Write categorized scores to the respective CSV files
write_to_csv(real_csv_filename, real_scores)
write_to_csv(fake_csv_filename, fake_scores)
write_to_csv(fake_custom_csv_filename, fake_custom_scores)
