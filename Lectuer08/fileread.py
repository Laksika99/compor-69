def main():
    infile = open('philosophers.txt', 'r') #open a file for reading
    file_contents = infile.read() #read the contents of the file
    infile.close() #close the file

    print(file_contents) #print the contents of the file

main()