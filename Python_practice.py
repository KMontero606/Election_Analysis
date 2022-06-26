print("Hello World!")

#For loops
counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

if "El Paso" in counties:
    print("El Paso is in the list of counties")

else:
    print("El Paso is not the list of counties")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso are in the list of counties.")
else:
    print("Arapahoe and El Paso is not in the list of counties.")

if "Arapahoe" in counties and "El Paso" not in counties:
   print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

#Iterate through lists and tuples
for county in counties:
    print(county)

for i in range(len(counties)):
    print(counties[i])

#Iterate through a dictionary    
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

#Get the Values of a Dictionary
for county in counties_dict.keys():
    print(county)

#Get the values of a dictionary
for voters in counties_dict.values():
    print(voters)

for county in counties_dict:
    print(counties_dict.get(county))

#Get the key-value pairs of a dictionary
#for key, value in dictionary_name.items():
    #print(key, value)
#for county, voters in counties_dict.items():
    #print(county + " county has " + str(voters) + " registered voters.")
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

#Iterate through a list of dictionaries
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353}, 
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

#Get the values from a list of dictionaries
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

for county_dict in voting_data:
    print(county_dict['county'])

#f-string print format
#my_votes = int(input("How many votes did you get in the election? "))
#total_votes = int(input("What is the total votes in the election? "))
#print(f"I received {my_votes / total_votes * 100}% of the total votes.")

#Multiline F-strings
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)

#Format floating-point decimals
#f'{value:{width},.{precision}}'
