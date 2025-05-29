def file_word_count(filename):
    #Instance words variable with value 0 so it can be used later
    word_count = 0
    #Try block for the exception and main code of the function
    try:
        #Opens the file
        with open(filename, "r") as file:
            #Create a text object with the contents of the file
            text = file.read()
            #Create a list of words within the text object
            words = text.split()
            #Counts the number of words in the list an sets word_count to the value
            word_count = word_count + len(words)  
            return word_count
    #Handle FileNotFound Error
    except FileNotFoundError:
        print("File Not Found")

def make_output_txt(*args):
    #Opens a new output.txt file to write, truncates said file if it already exists
    output_txt = open("output.txt", "w")
    #For every string parameter given to make_output_txt, writes it to a line and ensure the next string is written to a new line
    for num in args:
        output_txt.write(num + "\n")
    #Closes the file
    output_txt.close()

