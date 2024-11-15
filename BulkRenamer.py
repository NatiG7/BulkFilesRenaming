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
            # if a match found, name is added to the array
            if old_name_part in filename:
                matches.append(filename)

    # Report on found matches
    print("\n~~~ Match Report ~~~")
    print(f"Files found: {len(matches)}\n")

    if matches:
        print("Matching files:\n")
        for file in matches:
            print(f"\t  - {file}")
    else:
        print("No files found matching the criteria.")
        return # exzzzit
    # End report, ask user if replace

    if matches:
        user_answer = input("\nWould you like to proceed with renaming ? [yes] \\ [no]\n").strip().lower()
        if user_answer == 'yes':
            print("\n")
            # Renaming all matches
            for filename in matches:
                try:
                    new_filename = filename.replace(old_name_part,new_name_part)
                    old_path = os.path.join(folder_path, filename)
                    new_path = os.path.join(folder_path, new_filename)
                    os.rename(old_path, new_path)
                    print(f"Renamed '{filename}' ---> '{new_filename}'\n")
                except Exception as e:
                    print(f"\nError occured while renaming '{filename}' :\n\t\t'{e}'")
        else:
            print("\nOperation canceled by user.")
    print("\n~~~~~ Proccess Completed ~~~~~")

folder = '../../Sandbox/Pit 1 (BulkRenamer)'
number = 0
bulk_rename(folder,'1','REDACTED')