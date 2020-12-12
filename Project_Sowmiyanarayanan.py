#Mehdi Daoudi and Supraja Sowmiyanarayanan

import pandas
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px

df = pandas.read_csv("1976-2016-president.csv")
data = pandas.DataFrame(df)
# Question One

total = 0
#Reading data from the year 2000
data2000_2016 = list(df.loc[:,'year'] >= 2000)
candidatevotes = list(df.loc[:,'candidatevotes'])
#adding up the total candidate votes from the year 2000 and above
for iteration, i in enumerate(data2000_2016):
    if i == True:
        total += candidatevotes[iteration]
print(total, "votes for all elections from 2000 to 2016")

#Reading data from the years underneath not including 2000 for comparison on the pie chart
data1976_1996 = list(df.loc[:, 'year'] < 2000)
total2 = 0

#Adding up the total number of votes from the year specified
for iteration, i in enumerate(data1976_1996):
    if i == True:
        total2 += candidatevotes[iteration]
# print(total2, "votes for all elections from 1976 to 1996")
list1 = [total, total2]
print(list1)
names = ["2000-2016", "1976-1996"]
colors = ["b","r"]
# Pie chart, comparing 1996 and below data to 2000 and above data. We differentiated colors.
ypos = np.arange(len(names))
plt.xticks(ypos, names)
plt.title("Total Votes Comparison")
plt.pie(list1, labels = names, colors = colors)
plt.show()






# # Question Two
#Gathering applicable data from the years above 2000
data2000_2016 = list(df.loc[:,'year'] >= 2000)
#gathering Vermont data for cross-checking
stateVT = list(df.loc[:,'state_po'] == 'VT')
#gathering totalvotes data
totalvotes = list(df.loc[:, 'candidatevotes'])
#gathering republican data
repTotal = list(df.loc[:,'party'] == 'republican')
#gathering democratic data
demTotal = list(df.loc[:,'party'] == 'democrat')
#gathering all votes data for adding later on
candidatevotes = list(df.loc[:,'candidatevotes'])

vt_vote = 0
stateVTlist = []
replistTotal = []
demlistTotal = []
#making a list for where republican data is in the excel sheet
for iteration, i in enumerate(repTotal):
    if i == True:
        replistTotal.append(iteration)
#making a list for where democratic data is in the excel sheet
for iteration, i in enumerate(demTotal):
    if i == True:
        demlistTotal.append(iteration)
#making a list of where all of the data above 2000 is in the excel sheet
above2000 = []
for iteration, i in enumerate(data2000_2016):
     if i == True:
         above2000.append(iteration)

#making a list of where all of the data for Vermont is in the excel sheet
for iteration, i in enumerate(stateVT):
    if iteration > above2000[0]:
        if i == True:
            stateVTlist.append(iteration)
            vt_vote += totalvotes[iteration]
#Cross checking republican data with Vermont data and finding all of the data above the year 2000
#Then adding it to a list of our votes applicable for the problem
replistVT = []
for i in replistTotal:
    for j in stateVTlist:
        if i ==j:
            if (i > above2000[0]):
                replistVT.append(i)

#cross checking democratic data with the Vermont data and finding all of the data above the year 2000
#Then adding it to a list of our votes applicable for the problem
demlistVT = []
for i in demlistTotal:
    for j in stateVTlist:
        if i == j:
            if(i > above2000[0]):
                demlistVT.append(i)
#Adding all of the Democratic data we just found to create one total number
totalDemVote = 0
for i in demlistVT:
    totalDemVote += candidatevotes[i]
#Adding all of the Republican data we just found to create one total number
totalRepVote = 0
for i in replistVT:
    totalRepVote += candidatevotes[i]


#Printing our answers
print(totalDemVote, "democratic votes in Vermont from 2000 to 2016")
print(totalRepVote, "republican votes in Vermont from 2000 to 2016")
#Finding our Percentages
x = round((totalDemVote/vt_vote)*100,2)
y = round((totalRepVote/vt_vote)*100,2)
#Creating a list for the pie chart
list1 = [x,y]
#printing our data
print("Percentage Dem for VT from 2000 to 2016: ", x ,"%")
print("Percentage Rep for VT from 2000 to 2016: ", y,"%")
#Labels
names = ["2000-2016", "1976-1996"]
#colors
colors = ["b","r"]
# Pie chart making with the names of each side of the pie chart and title
ypos = np.arange(len(names))
names = ['VT Dem Votes', 'VT Rep Votes']
plt.xticks(ypos, names)
plt.title("VT Votes from 2000-2016 Total")
plt.pie(list1, labels = names, colors = colors)
plt.show()


# # Question 3
def percentageRep(stateog):
    #Gathering year data from the year 2012 and 2016
    data2012_2016 = list(df.loc[:, 'year'] >= 2012)
    #gathering state data for the original state entry given from the main function
    state = list(df.loc[:, 'state_po'] == stateog)
    #finding the candidate votes numbers
    totalvotes = list(df.loc[:, 'candidatevotes'])
    #finding the republican party data
    repTotal = list(df.loc[:, 'party'] == 'republican')
    #finding the candidatevotes data
    candidatevotes = list(df.loc[:, 'candidatevotes'])

    vote = 0
    stateList = []
    repListTotal = []
    #making a list for where republican data is in the excel sheet
    for iteration, i in enumerate(repTotal):
        if i == True:
            repListTotal.append(iteration)
    #making a list of where all of the data is in the year 2012 and the year 2016
    above2012 = []
    for iteration, i in enumerate(data2012_2016):
        if i == True:
            above2012.append(iteration)
    #cross checking state data and making sure it's above the year 2012, then adding the state iteration to a list
    #and adding the total votes for the years above 2012 and 2016
    for iteration, i in enumerate(state):
        if iteration >= above2012[0]:
            if i == True:
                stateList.append(iteration)
                vote += totalvotes[iteration]
    #cross checking the republican list with the state list and making sure its above 2012 then adding the data to a
    #new list
    replist = []
    for i in repListTotal:
        for j in stateList:
            if i == j:
                if (i >= above2012[0]):
                    replist.append(i)
    #Adding the new list data together here
    totalRepVote = 0
    for i in replist:
        totalRepVote += candidatevotes[i]
    #percentage of the republican vote for the state calulated here
    percent = (totalRepVote / vote) * 100
    return percent


def percentageDem(stateog):
    # Gathering year data from the year 2012 and 2016
    data2012_2016 = list(df.loc[:, 'year'] >= 2012)
    #gathering state data for the original state entry given from the main function
    state = list(df.loc[:, 'state_po'] == stateog)
    # finding the candidate votes numbers
    totalvotes = list(df.loc[:, 'candidatevotes'])
    # finding the democratic party data
    demTotal = list(df.loc[:, 'party'] == 'democrat')
    # finding the candidatevotes data
    candidatevotes = list(df.loc[:, 'candidatevotes'])


    vote = 0
    stateList = []
    demListTotal = []
    # making a list for where republican data is in the excel sheet
    for iteration, i in enumerate(demTotal):
        if i == True:
            demListTotal.append(iteration)

    # making a list of where all of the data is in the year 2012 and the year 2016
    above2012 = []
    for iteration, i in enumerate(data2012_2016):
        if i == True:
            above2012.append(iteration)

    #cross checking state data and making sure it's above the year 2012, then adding the state iteration to a list
    #and adding the total votes for the years above 2012 and 2016
    for iteration, i in enumerate(state):
        if iteration >= above2012[0]:
            if i == True:
                stateList.append(iteration)
                vote += totalvotes[iteration]

    #cross checking the republican list with the state list and making sure its above 2012 then adding the data to a
    #new list
    demlist = []
    for i in demListTotal:
        for j in stateList:
            if i == j:
                if (i >= above2012[0]):
                    demlist.append(i)

    #Adding the new list data together here
    totalDemVote = 0
    for i in demlist:
        totalDemVote += candidatevotes[i]

    # percentage of the republican vote for the state calulated here
    percent = (totalDemVote / vote) * 100
    return percent


def main():
    #A list of all of the state's names in abbreviated formatting
    states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
              "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
              "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
              "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
              "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
    #making a dictionary of all of the state along with a placeholder 0 for democrat and republican separately
    dictRep = dict.fromkeys(states, 0)
    dictDem = dict.fromkeys(states, 0)

    #updating the dictionary values
    for state in states:
        up_dict = {state: percentageRep(state)}
        dictRep.update(up_dict)
    for state in states:
        up_dict = {state: percentageDem(state)}
        dictDem.update(up_dict)

    #listing the top 5 democratic states
    demstatelist = []
    print("Democrat Top 5:")
    sorted_dict = sorted(dictDem.items(), key=lambda kv: kv[1], reverse=True)
    for key, value in sorted_dict[:5]:
        print("%s: %s" % (key, value))
        demstatelist.append(value)

    #Listing the top 5 Republican states
    repstatelist = []
    repstatename = []
    print("Republican Top 5:")
    sorted_dict = sorted(dictRep.items(), key=lambda kv: kv[1], reverse=True)
    for key, value in sorted_dict[:5]:
        print("%s: %s" % (key, value))
        repstatelist.append(value)

    #For labeling purposes, making two lists of the state names which are top five
    demstatename = ["DC","HI","MD","CA","VT"]
    repstatename = ["WY", "OK", "WV", "ID", "KY"]
    print(demstatelist)
    #Democrat Top 5 Bar Graph making
    ypos = np.arange(len(demstatename))
    plt.xticks(ypos, demstatename)
    plt.title("Top Five Democratic States From 2012 to 2016")
    plt.xlabel("States")
    plt.ylabel("Percentage of votes Democrat")
    plt.bar(ypos, demstatelist)
    plt.show()
    #Republican Top 5 Bar Graph making
    ypos2 = np.arange(len(repstatename))
    plt.xticks(ypos2, repstatename)
    plt.title("Top Five Republican  From 2012 to 2016")
    plt.xlabel("States")
    plt.ylabel("Percentage of votes Republican")
    plt.bar(ypos2, repstatelist)
    plt.show()


main()
# # #
# # #Question 4
def NJvotesandparties(year, count, bool):
    #Gathering state data for our chosen state, New Jersey
    stateNJ = list(df.loc[:,'state_po'] == 'NJ')
    #Gathering totalvotes data
    totalvotes = list(df.loc[:, 'candidatevotes'])
    #Gathering republican data
    repTotal = list(df.loc[:,'party'] == 'republican')
    #Gathering democratic data
    demTotal = list(df.loc[:,'party'] == 'democrat')
    #Gathering candidatevotes data
    candidatevotes = list(df.loc[:,'candidatevotes'])

    nj_vote = 0
    stateNJlist = []
    replistTotal = []
    demlistTotal = []
    #Gathering republican list data
    for iteration, i in enumerate(repTotal):
        if i == True:
            replistTotal.append(iteration)
    #Gathering democratic list data
    for iteration, i in enumerate(demTotal):
        if i == True:
            demlistTotal.append(iteration)
    #Gathering state New Jersey info then adding the total votes for the state of new jersey
    for iteration, i in enumerate(stateNJ):
        if i == True:
            stateNJlist.append(iteration)
            nj_vote += totalvotes[iteration]

    #cross checking the state data with the republican data then adding to the list
    replistNJ = []
    for i in replistTotal:
        for j in stateNJlist:
            if i ==j:
                replistNJ.append(i)

    #cross checking the state data with the republican data then adding to the list
    demlistNJ = []
    for i in demlistTotal:
        for j in stateNJlist:
            if i == j:
                demlistNJ.append(i)

    #Cross checking the count with the iteration as well as checking the boolean to see if we
    #want republican data or democratic data
    totalDemVote = 0
    for iteration, i in enumerate(demlistNJ):
        if iteration == count:
            # print("Democrat", candidatevotes[i])
            if(bool == True):
                return candidatevotes[i]

    #Cross checking the count with the iteration as well as checking the boolean to see if we
    #want republican data or democratic data
    totalRepVote = 0
    for iteration, i in enumerate(replistNJ):
        if iteration == count:
            # print("Republican", candidatevotes[i])
            if(bool == False):
                return candidatevotes[i]



count = 0
demlist = []
replist = []
yearlist = []
#running a for loop through the years necessary of 1976-2016
#using booleans and count for checking data within the function
for i in range(1976,2020,4):
    demlist.append(NJvotesandparties(i,count, True))
    replist.append(NJvotesandparties(i,count, False))
    count += 1
    yearlist.append(i)


years = []
count=0
#Running the data again through the for loop to print the data from the new list
for i in range(1976,2020,4):
    years.append(i)
    print("Democrat Votes in NJ,",i, ":", demlist[count])
    print("Republican Votes in NJ,",i, ":", replist[count])
    count +=1

#Printing the data in the form of a plot with the republican data and the democratic data
#sorted by the color of their party
ypos = np.arange(len(years))
plt.xticks(ypos, years)
plt.title("NJ Democrat vs Republican Total Votes from 1976-2016")
plt.xlabel("Year")
plt.ylabel("Number of Votes")
plt.plot(ypos, demlist)
plt.plot(ypos, replist, color = "r")
plt.show()

#Question 6

def percentageRep(stateog):
    #Gathering data for the year 2016
   data2016 = list(df.loc[:, 'year'] >= 2016)
    #Gathering state data from the specified state
   state = list(df.loc[:, 'state_po'] == stateog)
    #Gathering totalvotes data
   totalvotes = list(df.loc[:, 'candidatevotes'])
    #Gathering republican data
   repTotal = list(df.loc[:, 'party'] == 'republican')
    #gathering candidate votes data
   candidatevotes = list(df.loc[:, 'candidatevotes'])


   vote = 0
   stateList = []
   repListTotal = []
    #Gathering data within a for loop
   for iteration, i in enumerate(repTotal):
       if i == True:
           repListTotal.append(iteration)
    #Gathering data above the year 2016
   above2016 = []
   for iteration, i in enumerate(data2016):
       if i == True:
           above2016.append(iteration)
    #Gathering data above the year of 2016
   for iteration, i in enumerate(state):
       if iteration >= above2016[0]:
           if i == True:
               stateList.append(iteration)
               vote += totalvotes[iteration]
    #cross checking the republican data with the state data and the year data to get our
    #desired numbers
   replist = []
   for i in repListTotal:
       for j in stateList:
           if i == j:
               if (i >= above2016[0]):
                   replist.append(i)
    #Republican vote data calculated then made into a percentage.
   totalRepVote = 0
   for i in replist:
       totalRepVote += candidatevotes[i]
   percent = (totalRepVote / vote) * 100
   return percent


def percentageDem(stateog):
    #Gathering data from the year 2016
   data2012_2016 = list(df.loc[:, 'year'] >= 2016)
    #Gathering data fromt he state specified
   state = list(df.loc[:, 'state_po'] == stateog)
    #Gathering total votes data
   totalvotes = list(df.loc[:, 'candidatevotes'])
    #Gathering Democratic Data
   demTotal = list(df.loc[:, 'party'] == 'democrat')
    #Gathering candidatevotes data
   candidatevotes = list(df.loc[:, 'candidatevotes'])


   vote = 0
   stateList = []
   demListTotal = []
    # Gathering data within a for loop
   for iteration, i in enumerate(demTotal):
       if i == True:
           demListTotal.append(iteration)
    #Gathering the data for the list for above2016
   above2016 = []
   for iteration, i in enumerate(data2012_2016):
       if i == True:
           above2016.append(iteration)
    #Cross checking the state data with the above2016 data
   for iteration, i in enumerate(state):
       if iteration >= above2016[0]:
           if i == True:
               stateList.append(iteration)
               vote += totalvotes[iteration]
    #Cross checking the state data with the democrat data and the above2016 data
   demlist = []
   for i in demListTotal:
       for j in stateList:
           if i == j:
               if (i > above2016[0]):
                   demlist.append(i)
    #Democratic vote then calculated into a percentage
   totalDemVote = 0
   for i in demlist:
       totalDemVote += candidatevotes[i]
   percent = (totalDemVote / vote) * 100
   return percent


def main():
    #States made into a list made up of abberviated names
   states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
             "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
             "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
             "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
             "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
    #Dictionary of repblican and democratic data
   dictRep = dict.fromkeys(states, 0)
   dictDem = dict.fromkeys(states, 0)
    #Updating the republican and democratic Dictionaries
   for state in states:
       up_dict = {state: percentageRep(state)}
       dictRep.update(up_dict)
   for state in states:
       up_dict = {state: percentageDem(state)}
       dictDem.update(up_dict)
    #Convering the values into lists
   listdem = list(dictDem.values())
   listrep = list(dictRep.values())
   winners = []
    #Finding the winners using a comparison if statement
   for iteration, i in enumerate(listdem):
       if listdem[iteration] < listrep[iteration]:
           winners.append(1)
       else:
           winners.append(2)
   # print(winners)
    #Using choropleth from plotly to graph out the map in accordance to the winners
   fig = px.choropleth(locations=states,
                       locationmode="USA-states",
                       color_continuous_scale=["#FF0000","#0000FF"],
                       color =  winners,
                       scope="usa",
                       title = "USA Election Winners 2016")

   fig.show()
#Calling the main function
main()
#Insight1
def percentageWritein(stateog):
    #Gathering data from the 2012 and 2016
    data2012_2016 = list(df.loc[:, 'year'] >= 2012)
    #Gathering data for the specific state
    state = list(df.loc[:, 'state_po'] == stateog)
    #Gathering totalvotes data
    totalvotes = list(df.loc[:, 'candidatevotes'])
    #Gathering writeintotal
    writeintotal = list(df.loc[:, 'writein'])
    #Gathering candidatevotes
    candidatevotes = list(df.loc[:, 'candidatevotes'])


    vote = 0
    stateList = []
    writeinListTotal = []

    #Gathering data for the writeinTotal then appending it to a list
    for iteration, i in enumerate(writeintotal):
        if i == True:
            writeinListTotal.append(iteration)

    #Gathering data for the years 2012-2016 then appending it to a list
    above2012 = []
    for iteration, i in enumerate(data2012_2016):
        if i == True:
            above2012.append(iteration)
    #Cross checking the state data with the 2012-2016 data
    for iteration, i in enumerate(state):
        if iteration >= above2012[0]:
            if i == True:
                stateList.append(iteration)
                vote += totalvotes[iteration]
    #Cross checking the writinlist data with the state data and the above2012-2016 data
    writeinList = []
    for i in writeinListTotal:
        for j in stateList:
            if i == j:
                if (i >= above2012[0]):
                    writeinList.append(i)
    #Finding the percentage of the totalwriteinvote
    totalwriteinvote = 0
    for i in writeinList:
        totalwriteinvote += candidatevotes[i]
    percent = (totalwriteinvote / vote) * 100


    #Returning the percentage
    return percent

def main():
    #All of the states in abbreviated format in a list
    states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
              "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
              "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
              "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
              "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
    #making a dictionary with a placeholder 0
    dictWriteIn = dict.fromkeys(states, 0)

    #updating the dictionary with the new write-in data
    for state in states:
        up_dict = {state: percentageWritein(state)}
        dictWriteIn.update(up_dict)
    #Sorting the dictionary then finding the top 5 states
    writeinstatelist = []
    print("Top 5 States With Write Ins:")
    sorted_dict = sorted(dictWriteIn.items(), key=lambda kv: kv[1], reverse=True)
    for key, value in sorted_dict[:5]:
        print("%s: %s" % (key, value))
        writeinstatelist.append(value)
    #List of the top 5 states for labeling purposes
    writeinstatename = ["VT","AK","WY","WA","ND"]
    #Plotting the data on a bar graph
    ypos = np.arange(len(writeinstatename))
    plt.xticks(ypos, writeinstatename)
    plt.title("Top Five Write In States From 2012 to 2016")
    plt.xlabel("States")
    plt.ylabel("Percentage of Write In Votes ")
    plt.bar(ypos, writeinstatelist)
    plt.show()

#Calling the main function
main()

#Insight2
def writeinVotes(yearWanted):
    #Gathering data from all the years
    years = list(df.loc[:, 'year'])
    #Gathering data from all the writeins
    writeins = list(df.loc[:,'writein'])
    #Gathering candidatevotes data
    candidatevotes = list(df.loc[:,'candidatevotes'])


    total = 0
    yearlist = []

    #Finding all of the years necessary by comparing it to the years wanted
    for iteration, year in enumerate(years):
        if year == yearWanted:
            yearlist.append(iteration)


    finalList = []

    #Comparing it to the writeins category and then finding the applicable candidatevotes category
    for iteration, writein in enumerate(writeins):
        if iteration in yearlist:
            if writein == True:
                finalList.append(candidatevotes[iteration])

    #Finding the finalList data
    for i in finalList:
        total+= i
    #Returning the total for the given year
    return total


writeinList = []
yearlist = []
votetotal = 0
#For loop going through all of the years then calling the function in accordance to every year
#To fill the yearlist
for i in range(1976,2020,4):
    writeinList.append(writeinVotes(i))
    yearlist.append(i)

ypos = np.arange(len(yearlist))
plt.xticks(ypos, yearlist)
plt.title("Write-In Votes from 1976-2016")
plt.xlabel("Year")
plt.ylabel("Number of Votes")
plt.plot(ypos, writeinList)
plt.show()
