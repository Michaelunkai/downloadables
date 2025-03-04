import os

# Directory containing the videos
video_directory = "C:\\Users\\micha\\Videos"

# List all files in the directory
video_files = os.listdir(video_directory)

# Filter out only video files
video_files = [file for file in video_files if file.endswith(".mp4")]

# Rename files to replace spaces with underscores
for video_file in video_files:
    old_path = os.path.join(video_directory, video_file)
    new_file = video_file.replace(" ", "_")
    new_path = os.path.join(video_directory, new_file)
    os.rename(old_path, new_path)

# Command template
command_template = 'python a.py --file="{file_path}" --title="{title}" --description="" --keywords="docker, kubernetes" --category="22" --privacyStatus="public"'

# Run the command for each video file
for i, video_file in enumerate(video_files[:5]):  # Run for the first 5 files
    title = os.path.splitext(video_file)[0].replace("_", " ")  # Get title from file name with spaces
    file_path = os.path.join(video_directory, video_file)
    command = command_template.format(file_path=file_path, title=title)
    os.system(command)
