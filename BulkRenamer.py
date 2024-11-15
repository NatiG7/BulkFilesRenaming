# Bulk renaming files with different flags options
# Interactive mode
# Categorizing into selections
# Recursive option and regex capture


# Code for rework

import os


def bulk_rename(folder_path, old_name_part, new_name_part):
    '''
    This function receives a path variable, a part of an existing name of file(s)
    and the new name that will replace all found name parts.
    '''
    # Array for replacement matches
    matches = []

    # First run, scan for matches (like a regex)
    for filename in os.listdir(folder_path):
        try:
            # if a match found, name is added to the array
            if old_name_part in filename:
                matches.append(filename)

            # Report on found matches
            print("\n~~~ Match Report ~~~")
            print(f"Files found: {len(matches)}")

            if matches:
                print("Matching files:")
                for file in matches:
                    print(f"  - {file}")
            else:
                print("No files found matching the criteria.")
        except Exception as e:
            print (f"An error has occured : {e}")
            
    
    
folder = '../../Sandbox/Pit 1 (BulkRenamer)'
bulk_rename(folder, 'New', 'File')