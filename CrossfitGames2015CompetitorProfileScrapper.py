import csv
import requests
import numpy as np
import itertools



from bs4 import BeautifulSoup

# Retreives Profile data from Crossfit Competitors 2012 - 2015

def CompetitorProfile(list_of_urls):
    
    profile_list = []

    for i in range(0,len(list_of_urls)):
        
        url = list_of_urls[i]
        url = str(url)
        print ' url is: ' + url
        if (url != '#'):
            if (url != 'http://games.crossfit.com/athlete/11451'):
                if (url != 'http://games.crossfit.com/athlete/36154'):
                    if (url != 'http://games.crossfit.com/athlete/11391'):
                        if (url != 'http://games.crossfit.com/athlete/51123'):
                            response = requests.get(url)
                            html= response.content
        
                            soup = BeautifulSoup(html)
                            table = soup.find('div', attrs={'class': 'profile-stats'})
        
                            list_of_rows = []
                            for row in table.findAll('tr')[1:]:
                                list_of_cells = []
                                for cell in row.findAll('td'):
                                    text = cell.text.replace('&nbsp','')
                                    text = text.encode("utf-8","ignore")
                                    list_of_cells.append(text)
                                list_of_rows.append(list_of_cells)
                            profile_list.append(list_of_rows)
                        
        
    
    return profile_list
    

# Retreives Competitor Links from All Crossfit Games Pages
def RetrieveCompetitorLinks(urls):
    
    list_of_links = []
   
    name_of_athlete = []
   
    
    for i in range(0, 1):
        url = str(urls[i])
        response = requests.get(url)
        html= response.content

        soup = BeautifulSoup(html)
        table = soup.find('div', attrs={'class': 'leaderboard-box'})


        # First for-loop retrieving links of competitors profiles
        
        for row in table.findAll('a', href=True):
            #row.text.replace('&nbsp;','')
            list_of_links.append(row['href'])
       
        
    
        # Second for-loop for retreiving athlete names    
        for row in table.findAll('tr')[1:]:
            list_of_cells = []
            for cell in row.findAll('td'):
                #text = cell.text.replace('&nbsp','')
                #text = cell.text.replace("\n", " ").replace("pts", "pts ")
                text = cell.text.replace('&nbsp','')
                text = text.encode("utf-8","ignore")
                list_of_cells.append(text)
            name_of_athlete.append(list_of_cells[1])
                      
    return (list_of_links, name_of_athlete)
    
    
# Retrieves demographics on Athletes
def AthleteDemographics(list_of_urls):
    
    demographics = [] 
    for i in range(0,len(list_of_urls)):
        
        url = list_of_urls[i]
        url = str(url)
        if (url != '#'):
            if (url != 'http://games.crossfit.com/athlete/11451'):
                if (url != 'http://games.crossfit.com/athlete/36154'):
                    if (url != 'http://games.crossfit.com/athlete/11391'):
                        if (url != 'http://games.crossfit.com/athlete/51123'):
                            response = requests.get(url)
                            html= response.content

                            soup = BeautifulSoup(html)
                            table = soup.find('div', attrs={'class': 'profile-details'})
                            list_of_rows = []
                            for cell in table.findAll('dd'):
                                text = cell.text.replace('&nbsp;', '')
                                text = text.encode("utf-8","ignore")
                                list_of_rows.append(text)
                            demographics.append(list_of_rows)
                            print demographics
    return demographics

    
# Holds an Array with Links to all Crossfit Regional Events for 2015    
def AllCompetitorLinks():
    
    
    urls = np.array(['http://games.crossfit.com/scores/leaderboard.php?stage=0&sort=0&division=101&region=0&regional=8&numberperpage=60&page=0&competition=2&frontpage=0&expanded=1&full=1&year=15&showtoggles=0&hidedropdowns=0&showathleteac=1&athletename=&fittest=1&fitSelect=undefined&scaled=0'])

    return (urls)
    
def ConcatenateAllInfo(wod, athletes_info, athlete_demographics):
    
    profile_Info = []
    for i in  itertools.izip(athletes_info, wod, athlete_demographics):
        i = str(i) + ','
        profile_Info.append(i)
       
    return profile_Info
    

    
# Unpack arrays with Competitors URLs and Competitor Names
#all_urls = AllCompetitorLinks()

print 'Retrieving Athlete Links and Names, Please be patient...\n'
links, athletes = RetrieveCompetitorLinks(AllCompetitorLinks())
print 'Retrieving Athlete Demographics, Please be patient...\n'
demographics = AthleteDemographics(links)
print 'Done Retrieving Athlete Demographics'

# Calls function to process athlete profiles
print 'Retrieving Competitor Profile, Please be patient... \n'
workouts = CompetitorProfile(links)

print 'Concantenating Info, Please be patient... \n'
#Calls function to concatenate all information
competitorInfo = ConcatenateAllInfo(workouts,athletes, demographics)

# Writes all the information to an excel spreadsheet
print 'Writing to CSV file'
outfile = open("./crossfitGamesProfileInfo_2015.csv", "wb")
writer = csv.writer(outfile, delimiter='\t')
writer.writerow(["Competitor"])
writer.writerows(competitorInfo)
outfile.close()
print 'Program complete, please see CSV file'

