# Python 3 code to delete multiple files in a directory or folder

# importing os module
import os

# Function to delete multiple files
def main():
    folder = "F:\\test\\Pair"
    # loop through all the files in the directory
    for count, filename in enumerate(os.listdir(folder)):
        # delete file if filename contains "Copy" 
        if "Copy" in filename:
            os.remove(folder + "\\" + filename)

# Driver Code
if __name__ == '__main__':
	
	# Calling main() function
	main()
