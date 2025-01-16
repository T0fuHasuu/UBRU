# Printing List :

    countries = ['Thailand', 'Laos', 'Singapore', 'Japan']
    countries

# Printing element in index x :

    print(countries[2])

# Take elemetns :

    print(countries[0][:4], countries[3])

# Insert : 

    countries.insert(0, 'Myanmar')
    countries

# Pop :

    countries.pop(1)
    countries

# Dictionary :

    Movies = {
        'equalizer 3': '11:00am',
        'john wick 4': '1:00pm',
        'batman': '3:00pm'
    }
    Movies

# Changing dictionary :

    Movies['expand4ble'] = '10:00pm'
    Movies

# Pop dictionary :

    Movies.pop('john wick 4', None)
    Movies

# Set of elements :

    dataScientist = ['Python', 'R', 'SQL', 'Git', 'Tableau', 'SAS']
    dataEngineer = ['Python', 'Java', 'Scala', 'Git', 'SQL', 'Hadoop']

    print("Data Scientist Skills:", dataScientist)
    print("Data Engineer Skills:", dataEngineer)

# Combine sets :

    combined_skills = list(set(dataScientist + dataEngineer))

    print("Combined Skills:", combined_skills)

# Take set which are presented in both set :

    duplicate_skills = list(set(dataScientist) & set(dataEngineer))

    print("Duplicate Skills:", duplicate_skills)

# Cross out what's in both set :

    dataScientist = ['Python', 'R', 'SQL', 'Git', 'Tableau', 'SAS']
    dataEngineer = ['Python', 'Java', 'Scala', 'Git', 'SQL', 'Hadoop']

    different_skills = list(set(dataScientist) ^ set(dataEngineer))

    print("Different Skills:", different_skills)

# Mixed elements :

    sequence = [1, 2, 8, 100, 200, 'datacamp', 'tutorial']
    sequence

# Loop printing what's in the set :

    for item in sequence:
    print(item)

# Half pyramid shape loop :

    for i in range(1, 11):
        print((str(i) + ' ') * i)