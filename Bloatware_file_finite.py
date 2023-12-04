import os, random
def bloatware_program():
    files_to_bloat = ["file1.txt", "file2.txt", "file3.txt", "file4.txt"]
    for file_name in files_to_bloat:
        spam_string = "(random characters)"
        with open(file_name, "w") as bloatware_file_stream:
            bloatware_file_stream.write((spam_string))
        spam_string = "(more random characters)"
        bloatware_file_stream.write((spam_string))
