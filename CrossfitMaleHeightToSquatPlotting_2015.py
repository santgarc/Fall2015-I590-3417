import csv
import pygal
import itertools

# Arrays to store Crossfit Regional backsquat weight
regional_backsquat_weight = []
regional_competitor_height = []

# Arrays to store Crossfit Regional backsquat weight conversion 
# from string to decimal/integers

clean_regional_competitor_height_int = []
clean_regional_backsquat_weight = []

# Arrays to store Crossfit GAmes 2015 backsquat weight
games2015_backsquat_weight = []
games2015_competitor_height = []

# Arrays to store Crossfit GAmes 2015 backsquat weight conversion 
# from string to decimal/integers
clean_games2015_backsquat_weight = []
clean_games2015_competitor_height = []





all_regional_weight = []
all_games2015_weight = []

# Opens a clean version of the Crossfit Regional Spreadsheet produced by
# CrossfitRegionalsCompetitorProfileScrapper.py
# Original worksheet is crossfitRegionals_2015
# Clean worksheet is crossfitRegionals_2015(Clean_v4)
f = open('./crossfitRegoinals_2015(Clean).csv')
csv_f = csv.reader(f)

for row in csv_f:
    regional_backsquat_weight.append(row[24])
    regional_competitor_height.append(row[31])
#    regional_backsquat_weight_decimal.append(row[2])

# Opens a clean version of the Crossfit Games 2015 Spreadsheet produced by
# CrossfitGAmes2015CompetitorProfileScrapper.py
# Original worksheet is crossfitGamesProfileInfo_2015
# Clean worksheet is crossfitGamesProfileInfo_2015(Clean)    
f = open('./crossfitGamesProfileInfo_2015(Clean).csv')
csv_f = csv.reader(f)

for row in csv_f:
    games2015_backsquat_weight.append(row[24])
    games2015_competitor_height.append(row[31])

            
#Stores data from Crossfit Regional Spreadsheet
for row in regional_backsquat_weight:
    if(row != 'Back Squat'):
        clean_regional_backsquat_weight.append(int(row))
        
for row in regional_competitor_height:
    if(row != 'Height'):
      clean_regional_competitor_height_int.append(int(row))  
                    
for row in games2015_backsquat_weight:
    if(row != 'Back Squat'):
        clean_games2015_backsquat_weight.append(int(row))
        
for row in games2015_competitor_height:
    if(row != 'Height'):
      clean_games2015_competitor_height.append(int(row)) 
                       


#for i in range(0, len(clean_regional_backsquat_weight)):
# print (dt.datetime.strptime(clean_regional_backsquat_weight[i], '%Y-%m-%d %H:%M:%S'))

#Concantenates all information into a 2D array for plotting
for i in  itertools.izip(clean_regional_backsquat_weight, clean_regional_competitor_height_int):
    i = (i)
    all_regional_weight.append(i)
    
for i in  itertools.izip(clean_games2015_backsquat_weight, clean_games2015_competitor_height):
    i = (i)
    all_games2015_weight.append(i)


print (clean_regional_backsquat_weight)


xy_chart = pygal.XY(stroke=False, show_x_lables=True, x_label_rotation=45, title='Crossfit Regionals Comeptitors vs Crossfit Games Competitors 2015\n (Back Squat)',
                    x_title='Weight in Pounds', y_title='height', dots_size=3)
#xy_chart.x_labels = ['0:02:06', '0:02:13', '0:02:25', '0:02:30', '0:02:47','0:02:58', '0:03:00', '03:00:02']
xy_chart.y_labels = ['5ft 3in', '5ft 5in', '5ft 6in', '5ft 8in', '5ft 9in','5ft 10in', '6ft 0in', '6ft 2in', '6ft 4in', '6ft 5in']
xy_chart.add('Regionals', all_regional_weight)
xy_chart.add('Games 2015', all_games2015_weight, dot_size=4)
#xy_chart.add('Regionals Correlation', [min(all_regional_weight),max(all_regional_weight)], stroke=True)
#xy_chart.add('Games Correlation', [min(all_games2015_weight),max(all_games2015_weight)], stroke=True)
#xy_chart.add('Games 2015', all_games_backsquat_weight)

xy_chart.render_to_file("CrossfitMaleHeightToBackSquat_2015.svg")
