import pandas as pd

#Step 1: Get the Data 
df= pd.read_csv('athletes.csv')

# Number of Men in Olympics
def men(df):
  men=['Male']
  men_df=df[df['Gender'].isin(men)]

  return(men_df)

# Number of Women  in Olympics
def women(df):
 women=['Female']
 women_df=df[df['Gender'].isin(women)]
 
 return(women_df)

# Number of golds won by Men
def golds_by_men():
  rank=[1]
  men_gold=men(df)[men(df)['Rank'].isin(rank)]

  return(men_gold)

# Number of golds won by Women
def golds_by_women():
  rank=[1]
  women_gold=women(df)[women(df)['Rank'].isin(rank)]

  return(women_gold)


# Total Number of Medals won by Men
def medals_by_men():
  rank=[1,2,3]
  men_medals=men(df)[men(df)['Rank'].isin(rank)]

  return(men_medals)

# Total Number of Medals won by Men vs Women
def medals_by_women():
  rank=[1,2,3]
  women_medals=women(df)[women(df)['Rank'].isin(rank)]

  return(women_medals)

# Number of medals won by specific country
def medals_by_country(country):
  country=[country]
  men_medals=medals_by_men()[medals_by_men()['Country'].isin(country)]
  women_medals=medals_by_women()[medals_by_women()['Country'].isin(country)]

  print("Number of medals won by Men: ", len(men_medals), " VS Women: ", len(women_medals) , " in USA")
  hyp(len(men_medals), len(women_medals))
  

# Hypothesis Test
def hyp(m_df, f_df):
  if m_df > f_df:
    print("Hypothesis proven True")
  else:
    print("Hypothesis proven False")
  print("-----------------------------------")

def testing():
  men_win=0
  women_win=0
  sport=['Gymnastic Artistic']
  men=golds_by_men()[golds_by_men()['Sport'].isin(sport)]
  men_result=men['Results'].values[0]
  women=golds_by_women()[golds_by_women()['Sport'].isin(sport)]
  women_result=women['Results'].values[0]

  winner(men_result, women_result, sport)

  sport=['Swimming 200M']
  men=golds_by_men()[golds_by_men()['Sport'].isin(sport)]
  men_result=men['Results'].values[0]
  women=golds_by_women()[golds_by_women()['Sport'].isin(sport)]
  women_result=women['Results'].values[0]

  winner(men_result, women_result,sport)

  sport=['Weightlifting 69KG']
  men=golds_by_men()[golds_by_men()['Sport'].isin(sport)]
  men_result=men['Results'].values[0]
  women=golds_by_women()[golds_by_women()['Sport'].isin(sport)]
  women_result=women['Results'].values[0]

  winner(men_result, women_result, sport)


def winner(men_result, women_result, sport):
   if men_result>women_result:
     print("Men has better score in ", sport)
   else:
    print("Women has better score in ", sport)


  





choice=1
print("\n")
print("Total number of Participants in Rio 2016 are: " ,len(df))


while(choice!=0):
  # user pick a choice 
  choice=int(input("\nChoose an option:\n"
  "1. Number of Males vs Female in Olympics \n"
  "2. Number of golds by Men vs Women:\n"
  "3. Number of medals by Men vs Women:\n "
  "4. Men vs Women medals winners in USA:\n"
  "0. Press 0 to exist: \n"))
  print("\n")
  if choice==1:
    print(len(men(df)), " men and ", len(women(df)), " women participated in Olympics")
    hyp(len(men(df)), len(women(df)))

  elif choice==2:
    # filter data and exclude country and sport 
    men_golds=golds_by_men().get(['Name', 'Gender', 'Rank'])
    #begin index from start
    men_golds.index=[list(range(1,len(men_golds)+1))]
    women_golds=golds_by_women().get(['Name', 'Gender', 'Rank'])
    women_golds.index=[list(range(1,len(women_golds)+1))]
    result=(men_golds.append(women_golds)).sort_values(by=["Name"])
    print(result)
    print("Number of golds won by Men: ", len(golds_by_men()), " VS Women: ", len(golds_by_women()))
    hyp(len(golds_by_men()), len(golds_by_women()))
    testing()

  elif choice==3:
    print("Number of medals won by Men: ", len(medals_by_men()), " VS Women: ", len(medals_by_women()))
    hyp(len(medals_by_men()), len(medals_by_women()))
    user=input(print("Do you want to save  athletes with medals into a file? (Y/N) \n"))
    if user=='Y':
        user=input(print("Enter file's name: (name.txt) \n"))
        outFile=open(user, 'a')

        men_medals=medals_by_men().get(['Name', 'Country' ,'Gender', 'Rank'])
        men_medals.index=[list(range(1,len(men_medals)+1))]
        women_medals=medals_by_women().get(['Name', 'Country','Gender', 'Rank'])
        women_medals.index=[list(range(1,len(women_medals)+1))]
        all_medal_winners=(men_medals.append(women_medals)).sort_values(by=["Rank"])
        print(all_medal_winners, file=outFile) 
        print("DONE-sent to file")

  elif choice==4:
    medals_by_country('USA')


  else:
    exit()
    








