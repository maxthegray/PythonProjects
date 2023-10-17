#hey
def get_age(max_age):
    age_at_middle_school = 10
    age_at_lower_school = 6
    age_at_high_school = 14
    age_at_college = 18
    age_at_adult = 22

    if max_age < age_at_lower_school:
        print("Max is too young for school")
    elif max_age < age_at_middle_school:
        print("Max is in lower school")
    elif max_age < age_at_high_school:
        print("Max is in middle school")
    elif max_age < age_at_college:
        print("Max is in high school")
    elif max_age < age_at_adult:
        print("Max is in college")
    else:
        print("Max is too old for school")

try:
    max_age = int(input("Max age? "))
    get_age(max_age)
except ValueError:
    print("age is just numbers broh. Just use numbers broh")
