import os
import shutil
from datetime import datetime

def check_directory_path(directory_path):
    """  # Opens the docstring

    Verify if the given directory path exists and is accessible.

    Args: 
        directory_path (str): Path to the directory to be organized 
    
    Returns:
        bool: True if directory exists and is accessible, False otherwise

    """
    try: 
        # First we check if the path exists at all
        if os.path.exists(directory_path):
        # Then check if it's actually a directory (not a file)
            if os.path.isdir(directory_path):
                print(f"Successfully found directory: {directory_path}")
                return True
            else: 
                print(f"Error: {directory_path} is not a directory")
                return False
        else: 
                print(f"Error: {directory_path} does note exist")
                return False
    except Exception as e: 
         # If any other error occurs, catch it and show the error message
         print(f"Error accessing directory: {str(e)}")
         return False


def get_files_in_directory(directory_path):
    """
    Get a list of all files in the specified directory.
    
    Args:
        directory_path (str): Path to the directory to scan
        
    Returns:
        list: List of file paths found in the directory, or empty list if none found
    """
    # Create an empty list to store our file paths
    files_list = []
    
    # First check if the directory is valid using previous function
    if not check_directory_path(directory_path):
        print("Could not access directory")
        return files_list  # Return empty list if directory invalid
    
    try:
        # os.listdir() returns a list of everything in the directory
        for item in os.listdir(directory_path):
            # Create the full path by joining directory path and item name
            full_path = os.path.join(directory_path, item)
            
            # Check if this item is a file (not a directory)
            if os.path.isfile(full_path):
                files_list.append(full_path)
                
        # If we found any files, print the count
        if files_list:
            print(f"Found {len(files_list)} files in directory")
        else:
            print("No files found in directory")
            
        return files_list
        
    except Exception as e:
        print(f"Error while scanning directory: {str(e)}")
        return files_list

def analyze_file(file_path):
    """
    Analyze a file to determine its type, creation date, and other properties.
    
    Args:
        file_path (str): Path to the file to analyze
        
    Returns:
        dict: Dictionary containing file information (extension, creation date, etc.)
        None: If file analysis fails
    """
    try:
        # Get file information using os.path
        file_info = {
            'full_path': file_path,
            'name': os.path.basename(file_path),  # Gets just the filename
            'extension': os.path.splitext(file_path)[1].lower(),  # Gets extension (.txt, .pdf, etc)
            'creation_time': datetime.fromtimestamp(os.path.getctime(file_path)),
            'modification_time': datetime.fromtimestamp(os.path.getmtime(file_path))
        }
        
        # Handle files with no extension
        if file_info['extension'] == '':
            file_info['extension'] = 'no_extension'
            
        print(f"Analyzed file: {file_info['name']}")
        return file_info
        
    except Exception as e:
        print(f"Error analyzing file {file_path}: {str(e)}")
        return None
    

def organize_files(source_directory, organization_type="extension"):
    """
    Organize files from source directory based on specified organization type.
    
    Args:
        source_directory (str): Path to directory containing files to organize
        organization_type (str): How to organize files ('extension', 'date', or 'name')
        
    Returns:
        bool: True if organization successful, False otherwise
    """
    try:
        # First, verify source directory and get files
        files = get_files_in_directory(source_directory)
        if not files:
            print("No files to organize!")
            return False
            
        # Create main output directory for organized files
        output_dir = os.path.join(source_directory, "organized_files")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            print(f"Created output directory: {output_dir}")
            
        # Process each file
        for file_path in files:
            # Get file information
            file_info = analyze_file(file_path)
            if not file_info:
                continue
                
            # Determine destination folder based on organization type
            if organization_type == "extension":
                # Remove the dot from extension
                folder_name = file_info['extension'].replace('.', '') or 'no_extension'
            elif organization_type == "date":
                folder_name = file_info['creation_time'].strftime('%Y-%m')  # Year-Month format
            else:  # by name
                folder_name = file_info['name'][0].upper()  # First letter of filename
                
            # Create destination folder
            destination_folder = os.path.join(output_dir, folder_name)
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)
                
            # Move the file
            destination_path = os.path.join(destination_folder, file_info['name'])
            shutil.move(file_path, destination_path)
            print(f"Moved: {file_info['name']} -> {folder_name}/")
            
        print("Organization complete!")
        return True
        
    except Exception as e:
        print(f"Error organizing files: {str(e)}")
        return False

    