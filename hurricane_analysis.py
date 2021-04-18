# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# Update Recorded Damages
updated_damages = []
def update_damages():
  for damage in damages:
    if damage == "Damages not recorded":
      updated_damages.append(damage)
    if damage[-1] == 'M':
      updated_damages.append(float(damage.strip('M'))*1000000)
    if damage[-1] == 'B':
      updated_damages.append(float(damage.strip('B'))*1000000000)

# test function by updating damages  
update_damages()

# Create a Table
# Create and view the hurricanes dictionary
hurricane_dictionary = {}
def build_hurricane_dictionary():
  index = 0
  for name in names:
    hurricane_dictionary[name] = {"Name":names[index],"Month":months[index], "Year":years[index], "Max Sustained Winds": max_sustained_winds[index], "Areas Affected":areas_affected[index], "Damage":updated_damages[index], "Deaths":deaths[index]}
    index += 1

build_hurricane_dictionary()

print(hurricane_dictionary)

# Organizing by Year
# create a new dictionary of hurricanes with year and key
hurricanes_by_year = {}

def organize_hurricanes_by_year():
  current_year = 0
  current_cane = []
  for key in hurricane_dictionary:
    current_year = hurricane_dictionary[key]["Year"]
    current_cane = hurricane_dictionary[key]
    if current_year not in hurricanes_by_year.keys():
      hurricanes_by_year[current_year] = current_cane
    elif current_year in hurricanes_by_year.keys():       
      hurricanes_by_year[current_year] = [hurricanes_by_year[current_year],current_cane]
      
organize_hurricanes_by_year()
print(hurricanes_by_year)

# Counting Damaged Areas
# create dictionary of areas to store the number of hurricanes involved in
damaged_areas = {}

def count_damaged_areas():
  for key in hurricane_dictionary:
    for place in hurricane_dictionary[key]["Areas Affected"]:
      if place not in damaged_areas.keys():
        damaged_areas[place] = 1
      elif place in damaged_areas.keys():
        damaged_areas[place] += 1
  print(damaged_areas)
  
count_damaged_areas()

# Calculating Maximum Hurricane Count
# find most frequently affected area and the number of hurricanes involved in

def max_hurricane_count():
  count = 0
  most_impacted = {}
  for key in damaged_areas:
    if damaged_areas[key] > count:
      count = damaged_areas[key]
  for key in damaged_areas:
    if damaged_areas[key] == count:
      most_impacted[key] = count
    else:
      continue 
  print(most_impacted)
    
max_hurricane_count()

# Calculating the Deadliest Hurricane
# find highest mortality hurricane and the number of deaths

def find_deadliest_hurricane():
  current_max = 0
  highest_deaths = {}
  for key in hurricane_dictionary:
    if hurricane_dictionary[key]["Deaths"] > current_max:
      current_max = hurricane_dictionary[key]["Deaths"]
  for key in hurricane_dictionary:
    if hurricane_dictionary[key]["Deaths"] == current_max:
      highest_deaths[key] = current_max
    else:
      continue
  print(highest_deaths)

find_deadliest_hurricane()

# Rating Hurricanes by Mortality
# categorize hurricanes in new dictionary with mortality severity as key
hurricane_mortality = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [] }
def organize_hurricanes_by_mortality():
  for key in hurricane_dictionary:
    if hurricane_dictionary[key]["Deaths"] == 0:
      hurricane_mortality[0].append(hurricane_dictionary[key])
    elif hurricane_dictionary[key]["Deaths"] > 0 and hurricane_dictionary[key]["Deaths"] < 100:
      hurricane_mortality[1].append(hurricane_dictionary[key])
    elif hurricane_dictionary[key]["Deaths"] > 100 and hurricane_dictionary[key]["Deaths"] < 500:
      hurricane_mortality[2].append(hurricane_dictionary[key])
    elif hurricane_dictionary[key]["Deaths"] > 500 and hurricane_dictionary[key]["Deaths"] < 1000:
      hurricane_mortality[3].append(hurricane_dictionary[key])
    elif hurricane_dictionary[key]["Deaths"] > 1000 and hurricane_dictionary[key]["Deaths"] < 10000:
      hurricane_mortality[4].append(hurricane_dictionary[key])
    else:
      hurricane_mortality[5].append(hurricane_dictionary[key])
  print(hurricane_mortality)

organize_hurricanes_by_mortality()
# 8 Calculating Hurricane Maximum Damage
# find highest damage inducing hurricane and its total cost

def find_highest_cost_hurricane():
  current_max = 0
  current_hurricane = ""
  highest_cost = {}
  for key in hurricane_dictionary:
    if hurricane_dictionary[key]["Damage"] == "Damages not recorded":
      continue
    elif hurricane_dictionary[key]["Damage"] < current_max:
      continue
    elif hurricane_dictionary[key]["Damage"] > current_max:
      current_hurricane = key
      current_max = hurricane_dictionary[key]["Damage"]
  highest_cost[current_hurricane] = current_max
  print(highest_cost)
      
find_highest_cost_hurricane()

# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  
# categorize hurricanes in new dictionary with damage severity as key
hurricane_damages = {0: [], 1: [], 2: [], 3: [], 4: []}

def organize_hurricanes_by_damages():
  for key in hurricane_dictionary:
    if hurricane_dictionary[key]["Damage"] == "Damages not recorded":
      continue
    elif hurricane_dictionary[key]["Damage"] == 0:
      hurricane_damages[0].append(hurricane_dictionary[key])
    elif hurricane_dictionary[key]["Damage"] > 0 and hurricane_dictionary[key]["Damage"] < 100000000:
      hurricane_damages[1].append(hurricane_dictionary[key])
    elif hurricane_dictionary[key]["Damage"] > 100000000 and hurricane_dictionary[key]["Damage"] < 1000000000:
      hurricane_damages[2].append(hurricane_dictionary[key])
    elif hurricane_dictionary[key]["Damage"] > 1000000000 and hurricane_dictionary[key]["Damage"] < 50000000000:
      hurricane_damages[3].append(hurricane_dictionary[key])
    elif hurricane_dictionary[key]["Damage"] > 50000000000:
      hurricane_damages[4].append(hurricane_dictionary[key])
    
  print(hurricane_damages)

organize_hurricanes_by_damages()

	
