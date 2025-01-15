File Organizer

A Python script that automatically organizes files in a directory based on different criteria like file type, date, or name. Perfect for cleaning up messy directories and maintaining an organized file system.
Features

Organizes files by:

File extension (e.g., .pdf, .txt, .jpg)
Creation date (Year-Month format)
First letter of filename


Creates a separate output directory to preserve original file structure
Handles files without extensions
Provides detailed console feedback during organization process

Requirements

Python 3.x
No external dependencies (uses only standard library modules)

Usage
Basic usage - organize by file extension
organize_files("path/to/your/directory", "extension")

# Organize by creation date
organize_files("path/to/your/directory", "date")

# Organize by filename
organize_files("path/to/your/directory", "name")
Project Structure
Copyfile_organizer/
    ├── organizer.py      # Main script
    └── test_files/       # Directory for testing
Core Functions

check_directory_path(): Validates directory existence and accessibility
get_files_in_directory(): Retrieves list of files from specified directory
analyze_file(): Extracts file information (type, dates, name)
organize_files(): Main function that handles file organization

Future Improvements

Add support for handling duplicate filenames
Implement file copying option instead of moving
Add more organization criteria (file size, last modified date)
Create undo functionality
Add GUI interface
