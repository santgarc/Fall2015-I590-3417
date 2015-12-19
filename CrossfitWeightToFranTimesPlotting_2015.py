import csv
import pygal
import itertools

# Arrays to store Crossfit Regional Fran Times
regional_fran_times = []
regional_fran_times_decimal = []
regional_competitor_weight = []

# Arrays to store Crossfit Regional Fran Times conversion 
# from string to decimal/integers
clean_regional_fran_times_decimal = []
clean_regional_competitor_weight_int = []
clean_regional_fran_times = []

# Arrays to store Crossfit GAmes 2015 Fran Times
games2015_fran_times = []
games2015_fran_times_decimal = []
games2015_competitor_weight = []

# Arrays to store Crossfit GAmes 2015 Fran Times conversion 
# from string to decimal/integers
clean_games2015_fran_times_decimal = []
clean_games2015_competitor_weight = []





all_regional_times = []
all_games2015_times = []

# Opens a clean version of the Crossfit Regional Spreadsheet produced by
# CrossfitRegionalsCompetitorProfileScrapper.py
# Original worksheet is crossfitRegionals_2015
# Clean worksheet is crossfitRegionals_2015(Clean_v4)
f = open('./crossfitRegoinals_2015(Clean).csv')
csv_f = csv.reader(f)

for row in csv_f:
    regional_fran_times.append(row[3])
    regional_competitor_weight.append(row[32])
    regional_fran_times_decimal.append(row[2])

# Opens a clean version of the Crossfit Games 2015 Spreadsheet produced by
# CrossfitGAmes2015CompetitorProfileScrapper.py
# Original worksheet is crossfitGamesProfileInfo_2015
# Clean worksheet is crossfitGamesProfileInfo_2015(Clean)    
f = open('./crossfitGamesProfileInfo_2015(Clean).csv')
csv_f = csv.reader(f)

for row in csv_f:
    games2015_fran_times.append(row[3])
    games2015_competitor_weight.append(row[32])

for row in regional_fran_times_decimal:
    if(row != 'Fran Times'):
#        clean_regional_fran_times.append('2015-12-12 ' + row)
            clean_regional_fran_times.append(row)
            
#Stores data from Crossfit Regional Spreadsheet
for row in regional_fran_times:
    if(row != 'Fran Times (Decimal)'):
#        clean_regional_fran_times.append('2015-12-12 ' + row)
            clean_regional_fran_times_decimal.append(float(row))
            
for row in regional_competitor_weight:
    if(row != 'Weight'):
      clean_regional_competitor_weight_int.append(int(row))  
                    
for row in games2015_fran_times:
    if(row != 'Fran Times (Decimal)'):
        clean_games2015_fran_times_decimal.append(float(row))
        
for row in games2015_competitor_weight:
    if(row != 'Weight'):
      clean_games2015_competitor_weight.append(int(row)) 
                       


#for i in range(0, len(clean_regional_fran_times)):
# print (dt.datetime.strptime(clean_regional_fran_times[i], '%Y-%m-%d %H:%M:%S'))

#Concantenates all information into a 2D array for plotting
for i in  itertools.izip(clean_regional_fran_times_decimal, clean_regional_competitor_weight_int):
    i = (i)
    all_regional_times.append(i)
    
for i in  itertools.izip(clean_games2015_fran_times_decimal, clean_games2015_competitor_weight):
    i = (i)
    all_games2015_times.append(i)




xy_chart = pygal.XY(stroke=False, show_x_lables=True, x_label_rotation=45, title='Crossfit Regionals Comeptitors vs Crossfit Games Competitors 2015',
                    x_title='Minutes & Seconds', y_title='weight', dots_size=3)
xy_chart.x_labels = ['0:02:06', '0:02:13', '0:02:25', '0:02:30', '0:02:47','0:02:58', '0:03:00', '03:00:02']
xy_chart.add('Regionals Fran', all_regional_times)
xy_chart.add('Games 2015 Fran', all_games2015_times, dot_size=4)
#xy_chart.add('Regionals Correlation', [min(all_regional_times),max(all_regional_times)], stroke=True)
#xy_chart.add('Games Correlation', [min(all_games2015_times),max(all_games2015_times)], stroke=True)
#xy_chart.add('Games 2015', all_games_fran_times)

xy_chart.render_to_file("CrossfitMaleWeightToFran_2015.svg")


        

