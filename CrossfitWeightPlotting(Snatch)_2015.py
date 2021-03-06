import csv
import pygal
import itertools

# Arrays to store Crossfit Regional snatch weight
regional_snatch_weight = []
regional_competitor_age = []

# Arrays to store Crossfit Regional snatch weight conversion 
# from string to decimal/integers

clean_regional_competitor_age_int = []
clean_regional_snatch_weight = []

# Arrays to store Crossfit GAmes 2015 snatch weight
games2015_snatch_weight = []
games2015_competitor_age = []

# Arrays to store Crossfit GAmes 2015 snatch weight conversion 
# from string to decimal/integers
clean_games2015_snatch_weight = []
clean_games2015_competitor_age = []





all_regional_weight = []
all_games2015_weight = []

# Opens a clean version of the Crossfit Regional Spreadsheet produced by
# CrossfitRegionalsCompetitorProfileScrapper.py
# Original worksheet is crossfitRegionals_2015
# Clean worksheet is crossfitRegionals_2015(Clean_v4)
f = open('./crossfitRegoinals_2015(Clean_Snatch).csv')
csv_f = csv.reader(f)

for row in csv_f:
    regional_snatch_weight.append(row[20])
    regional_competitor_age.append(row[30])
#    regional_snatch_weight_decimal.append(row[2])

# Opens a clean version of the Crossfit Games 2015 Spreadsheet produced by
# CrossfitGAmes2015CompetitorProfileScrapper.py
# Original worksheet is crossfitGamesProfileInfo_2015
# Clean worksheet is crossfitGamesProfileInfo_2015(Clean)    
f = open('./crossfitGamesProfileInfo_2015(Clean).csv')
csv_f = csv.reader(f)

for row in csv_f:
    games2015_snatch_weight.append(row[20])
    games2015_competitor_age.append(row[30])

            
#Stores data from Crossfit Regional Spreadsheet
for row in regional_snatch_weight:
    if(row != 'Snatch'):
        clean_regional_snatch_weight.append(int(row))
        
for row in regional_competitor_age:
    if(row != 'Age'):
      clean_regional_competitor_age_int.append(int(row))  
                    
for row in games2015_snatch_weight:
    if(row != 'Snatch'):
        clean_games2015_snatch_weight.append(int(row))
        
for row in games2015_competitor_age:
    if(row != 'Age'):
      clean_games2015_competitor_age.append(int(row)) 
                       


#for i in range(0, len(clean_regional_snatch_weight)):
# print (dt.datetime.strptime(clean_regional_snatch_weight[i], '%Y-%m-%d %H:%M:%S'))

#Concantenates all information into a 2D array for plotting
for i in  itertools.izip(clean_regional_snatch_weight, clean_regional_competitor_age_int):
    i = (i)
    all_regional_weight.append(i)
    
for i in  itertools.izip(clean_games2015_snatch_weight, clean_games2015_competitor_age):
    i = (i)
    all_games2015_weight.append(i)


print (clean_regional_snatch_weight)


xy_chart = pygal.XY(stroke=False, show_x_lables=True, x_label_rotation=45, title='Crossfit Regionals Comeptitors vs Crossfit Games Competitors 2015 \n (Snatch)',
                    x_title='Weight in Pounds', y_title='Age', dots_size=3)
#xy_chart.x_labels = ['0:02:06', '0:02:13', '0:02:25', '0:02:30', '0:02:47','0:02:58', '0:03:00', '03:00:02']
xy_chart.add('Regionals', all_regional_weight)
xy_chart.add('Games 2015', all_games2015_weight, dot_size=4)
#xy_chart.add('Regionals Correlation', [min(all_regional_weight),max(all_regional_weight)], stroke=True)
#xy_chart.add('Games Correlation', [min(all_games2015_weight),max(all_games2015_weight)], stroke=True)
#xy_chart.add('Games 2015', all_games_snatch_weight)

xy_chart.render_to_file("CrossfitMaleSnatch_2015.svg")
