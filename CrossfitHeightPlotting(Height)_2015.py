import csv
import pygal
import itertools

# Arrays to store Crossfit Regional height height
regional_height = []
regional_competitor_age = []

# Arrays to store Crossfit Regional height height conversion 
# from string to decimal/integers

clean_regional_competitor_age_int = []
clean_regional_height = []

# Arrays to store Crossfit GAmes 2015 height height
games2015_height = []
games2015_competitor_age = []

# Arrays to store Crossfit GAmes 2015 height height conversion 
# from string to decimal/integers
clean_games2015_height = []
clean_games2015_competitor_age = []





all_regional_height = []
all_games2015_height = []

# Opens a clean version of the Crossfit Regional Spreadsheet produced by
# CrossfitRegionalsCompetitorProfileScrapper.py
# Original worksheet is crossfitRegionals_2015
# Clean worksheet is crossfitRegionals_2015(Clean_v4)
f = open('./crossfitRegoinals_2015(Clean_Height).csv')
csv_f = csv.reader(f)

for row in csv_f:
    regional_height.append(row[31])
    regional_competitor_age.append(row[30])
#    regional_height_decimal.append(row[2])

# Opens a clean version of the Crossfit Games 2015 Spreadsheet produced by
# CrossfitGAmes2015CompetitorProfileScrapper.py
# Original worksheet is crossfitGamesProfileInfo_2015
# Clean worksheet is crossfitGamesProfileInfo_2015(Clean)    
f = open('./crossfitGamesProfileInfo_2015(Clean).csv')
csv_f = csv.reader(f)

for row in csv_f:
    games2015_height.append(row[31])
    games2015_competitor_age.append(row[30])

            
#Stores data from Crossfit Regional Spreadsheet
for row in regional_height:
    if(row != 'Height'):
        clean_regional_height.append(int(row))
        
for row in regional_competitor_age:
    if(row != 'Age'):
      clean_regional_competitor_age_int.append(int(row))  
                    
for row in games2015_height:
    if(row != 'Height'):
        clean_games2015_height.append(int(row))
        
for row in games2015_competitor_age:
    if(row != 'Age'):
      clean_games2015_competitor_age.append(int(row)) 
                       


#for i in range(0, len(clean_regional_height)):
# print (dt.datetime.strptime(clean_regional_height[i], '%Y-%m-%d %H:%M:%S'))

#Concantenates all information into a 2D array for plotting
for i in  itertools.izip(clean_regional_height, clean_regional_competitor_age_int):
    i = (i)
    all_regional_height.append(i)
    
for i in  itertools.izip(clean_games2015_height, clean_games2015_competitor_age):
    i = (i)
    all_games2015_height.append(i)


print (clean_regional_height)


xy_chart = pygal.XY(stroke=False, show_x_lables=True, x_label_rotation=45, title='Crossfit Regionals Comeptitors vs Crossfit Games Competitors 2015 \n (Competitor Height)',
                    x_title='Height in Feet/Inches', y_title='Age', dots_size=3)
xy_chart.x_labels = ['5ft 3in', '5ft 5in', '5ft 6in', '5ft 8in', '5ft 9in','5ft 10in', '6ft 0in', '6ft 2in', '6ft 4in', '6ft 5in']
xy_chart.add('Regionals', all_regional_height)
xy_chart.add('Games 2015', all_games2015_height, dot_size=4)
#xy_chart.add('Regionals Correlation', [min(all_regional_height),max(all_regional_height)], stroke=True)
#xy_chart.add('Games Correlation', [min(all_games2015_height),max(all_games2015_height)], stroke=True)
#xy_chart.add('Games 2015', all_games_height)

xy_chart.render_to_file("CrossfitMaleHeight_2015.svg")
