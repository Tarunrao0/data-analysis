import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("./adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df.groupby(['race']).size()

    # What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1) 

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((df[df['education'] == 'Bachelors']['education'].count() / df['education'].count()) * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    advanced_education = ['Bachelors', 'Masters', 'Doctorate']  

    advanced_edu_df = df[df['education'].isin(advanced_education)]
    lower_edu_df = df[~df['education'].isin(advanced_education)]
    
    high_earners_df_adv = advanced_edu_df[advanced_edu_df['salary'] == '>50K']
    high_earners_df_low = lower_edu_df[lower_edu_df['salary'] == '>50K']

    higher_education = advanced_edu_df.shape[0]
    lower_education = lower_edu_df.shape[0]

    # percentage with salary >50K
    higher_education_rich = round((high_earners_df_adv.shape[0] / higher_education) * 100, 1)
    lower_education_rich = round((high_earners_df_low.shape[0] / lower_education) * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers_df = df[df['hours-per-week'] == min_work_hours]
    
    num_min_workers = num_min_workers_df.shape[0]
    if num_min_workers > 0: 
        rich_count = num_min_workers_df[num_min_workers_df['salary'] == '>50K'].shape[0]
        rich_percentage = round((rich_count / num_min_workers) * 100, 1)
    else:
        rich_percentage = 0.0 

    # What country has the highest percentage of people that earn >50K?
    high_salary_df = df[df['salary'] == '>50K']
    
    high_salary_by_country = high_salary_df.groupby('native-country')['salary'].count()
    num_earning_people = df.groupby('native-country')['salary'].count()
    
    percentage_high_earners_by_country = (high_salary_by_country / num_earning_people) * 100
    percentage_high_earners_by_country = percentage_high_earners_by_country.round(1) 

    highest_earning_country = percentage_high_earners_by_country.idxmax()
    highest_earning_country_percentage = round(percentage_high_earners_by_country.max(), 1)

    # Identify the most popular occupation for those who earn >50K in India.
    high_earners_IN = df[(df['salary'] == '>50K') & (df['native-country'] == 'India')]
    occupation_count = high_earners_IN.groupby('occupation')['occupation'].count()

    top_IN_occupation = occupation_count.idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
