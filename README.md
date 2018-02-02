# Anti-Duplicator

This program prints to the console duplicate files in the specified folder.

# Quickstart

The program must be run using the console, the required argument is the folder.

How to run:
```bash
$ python3 pprint_json.py <folder_path>
```
Example of script launch on Linux, Python 3.5:
```bash
$ python3 duplicates.py ./
Same files:
File name: same_file
File size: [5] bytes
File paths:
./test/folder/same_file.txt
./test/folder/myfolder/Games/same_file.txt

File name: test_file1.html
File size: [124] bytes
File paths:
./test/test_file1.html
./test/xxxfolder/test_file1.html

File name: SampleAudio_0.7mb.mp3
File size: [725240] bytes
File paths:
./test/SampleAudio_0.7mb.mp3
./test/folder/SampleAudio_0.7mb.mp3
./test/folder/myfolder/SampleAudio_0.7mb.mp3
./test/folder/myfolder/Games/SampleAudio_0.7mb.mp3
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
