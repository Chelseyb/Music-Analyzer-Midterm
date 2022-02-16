#Python class Midterm Project Clbwc2 (Music Analyzer)
import csv

"""
The playlist data is formatted like the provided data files.
The columns of data are labeled in the first row.
You need to determine the data element separator and appropriately handle it.
You need to handle that there are labels in the first row.
E.g. you must handle the data file as provided.
"""
songByYear = {}
songByGenre = {}
longestName = list()
shortestName = list()
longestArtist = list()
shortArtist = list()
nameList = list()
minMax = list()
allLists = list()

def get_stats(filename):
    timeTrue = False
    
    artistList = list()
    yearList = list()
    timeList = list()
    
    try:
        music_file = open(filename, "r")
        """
        for element in music_file:
            x = element.split()
            musicInfo.append(x)
            print(x)
        """
        setMax = -1
        setmin = 1000
        
        for line in music_file:
           
            if timeTrue == False:
                timeTrue = True
                continue
            string = line.split("\t") #(" ",1) this splits on first whitespace so track number is a catergory now. i think Dale used tabs for categories and just spaces for columns with a compound name
            nameList.append(string[0])
            allLists.append(string)
            #check to make sure it is empty
            if string[16] == "":
                continue 
            artistList.append(string[1])

           
            if string[16] in songByYear:
                songByYear[string[16]]+=1
            else:
                songByYear[string[16]]=1
            #questions 3 and 4 
            if int(string[11]) >= setMax:
                longestName.append((string[0],string[1]))
                setMax = int(string[11])
            if int(string[11]) < setmin:
                shortestName.append((string[0],string[1]))
                setmin = int(string[11])
            #song by genre, check if the genre exists and add increments if it does
            if string[9] in songByGenre:
                songByGenre[string[9]]+=1
            else:
                songByGenre[string[9]]=1
    #THIS THAT I HAVE TRIED
           # yearList.append(string[2]) #when i add this is stays its out of range
           #!!! i still don't have the list split by category
          # BACK UP
             
                                #for row in gradebook:
                                  #  string = line.split("\t",1) #(" ",1)
                                    #for element in row:
                                                  # print(element)
                 

                    #i have split rows now i need to slip colums [row][column] it can't see columns
                    #keep appending for the columns
                    #print(nameList)
               #KEEP print(len(nameList)-1)
                #KEPP{ print(nameList)
                #print(musicInfo[1])
                #num_count = len(musicInfo[49]) #there should be 229 songs
                #print(num_count)
                #print(musicInfo[0][4])
                #print(fullList)
                #print(len(fullList[0])-1)
           
    except Exception as err:
        print ("ERROR: An error occurred loading", filename)
        print ("ERROR: The error returned was", err)
        return
    
    music_file.close()


def getMinMaxGenre(genres):
    longest = list()
    shortest = list()
    maximum = -1
    minimum = 1000
    headers = True
            
    for i in allLists:
        if headers:
            headers = False
            continue

        if i[11] =='':
            continue
        if i[9] == genres:
            if int(i[11]) >= maximum:
                longest.append((i[0],i[1]))
        if int(i[11]) <= minimum:
            shortest.append((i[0],i[1]))
    print("Longest Songs :",longest)
    print("Shortest Songs: ",shortest)
            








def main():
 
    do_evaluate = True
    while(do_evaluate):
        filename = input('\nWhat is the file you would like to evaluate? ')


        get_stats(filename)
        #print(len(fullList)-1)
    
        
        print("\n-----Music Analyzer-----")
#Q1:Total number of songs in the playlist
        print("Question 1: Total number of songs in the playlist:", len(nameList))
      #should be 228
      
#Q2:The number of songs that were released each year in the playlist

        print("\n Question 2: Songs by Year",songByYear)




#Q3
        print("\n Question 3: For each genre LONGEST song and artist:",longestName)

#Q4
        print("\n Questtion 4: FOr each genre SHORTEST song and artist:",shortestName)
        
        

#5Q5:For each genre, provide: the number of songs,
#the longest song by Name and Artist (list multiple if more than one),
#the shortest song by Name and Artist (list multiple if more than one).
        print("\n",songByGenre)
        for i in songByGenre:
            print(i)
            getMinMaxGenre(i)
        
#Q6:The number of songs that have been played.
        played = 0
        notPlayed = 0
        for i in allLists:
            if i[25] == '': #some song have not a zero but an empty string
                notPlayed +=1
            else:
                played +=1
        print("\nQuestion 6: Songs played:",played)

#Q7:The number of songs that have not been played.
        print("\nQuestion 7: Songs not played:", notPlayed)


        check_evaluate = input('\nWould you like to evaluate another file? (y/n) ')
        if (check_evaluate != 'y'):
            do_evaluate = False

main()



#The program is to load and analyze the data and provide the following summary values.
"""FIRST ROW LABEELS :Name	Artist, Composer, Album, Grouping, Work, Movement Number, Movement Count, Movement Name, Genre, Size, Time, Disc Number,
Disc Count,Track Number,Track Count, Year, Date Modified, Date, Added, Bit Rate, Sample Rate, Volume Adjustment, Kind, Equalizer,
Comments, Plays, Last Played, Skips , Last Skipped, My Rating, Location

2. The number of songs that were released each year in the playlist.
3. The song by Name and Artist for the longest song (based on Time) in the playlist. Display all if
there is more than one longest with the same time.
4. The song by Name and Artist for the shortest song (based on Time) in the playlist. Display all if
there is more than one shortest with the same time.
5. For each genre, provide: the number of songs, the longest song by Name and Artist (list multiple if
more than one), the shortest song by Name and Artist (list multiple if more than one).
6. The number of songs that have been played.
7. The number of songs that have not been played.

"""
