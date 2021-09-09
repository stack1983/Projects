# Add BMI for males and females for age groups
# Add overall BMI males vs females

import csv
import numpy as np
import pandas as pd

patient_information = {}
with open('insurance.csv') as insurance_file:
    insurance_csv = csv.DictReader(insurance_file)
    index = 1

    for patient in insurance_csv:
        patient_information[index] = patient
        index += 1

age = []
def average_age_of_patient():
    count = 0
    total_ages = 0
    average_age = 0

    for key in patient_information:
        age.append(patient_information[key]["age"])
        count += 1

    for number in age:
        total_ages += int(number)
        average_age = total_ages/count

    print("The average age of an insured individual is " + str(round(average_age)) + " years of age.")

average_age_of_patient()

def where_are_most_insured():
    southwest_total = 0
    southeast_total = 0
    northeast_total = 0
    northwest_total = 0

    for key in patient_information:
        if patient_information[key]["region"] == "southwest":
            southwest_total += 1
        elif patient_information[key]["region"]== "southeast":
            southeast_total += 1
        elif patient_information[key]["region"]== "northeast":
            northeast_total += 1
        elif patient_information[key]["region"]== "northwest":
            northwest_total += 1

    max_population = southeast_total

    if southwest_total > max_population and northeast_total < max_population and northwest_total < max_population:
        print("A majority of the insured live in the southwest.")
    elif northwest_total > max_population and northeast_total < max_population:
        print("A majority of the insured live in the northwest.")
    elif northeast_total > max_population:
        print("A majority of the insured live in the northeast.")
    else:
        print("A majority of the insured live in the southeast.")

# where_are_most_insured()

def smoker_vs_nonsmoker():
    smoker_total_cost = 0
    nonsmoker_total_cost = 0
    smoker_count = 0
    nonsmoker_count = 0
    smoker_avg_cost = 0
    nonsmoker_avg_cost = 0
    for key in patient_information:
        if patient_information[key]["smoker"] == "yes":
            current_cost = float(patient_information[key]["charges"].strip("'"))
            round(current_cost,2)
            smoker_total_cost += current_cost
            smoker_count += 1
            smoker_avg_cost = round(smoker_total_cost,2)/smoker_count
        else:
            current_cost = float(patient_information[key]["charges"].strip("'"))
            round(current_cost,2)
            nonsmoker_total_cost += current_cost
            nonsmoker_count +=1
            nonsmoker_avg_cost = round(nonsmoker_total_cost,2)/nonsmoker_count

    print("Total cost for nonsmokers is " + str(round(nonsmoker_total_cost,2)) + " with an average cost of " + str(round(nonsmoker_avg_cost,2)) + " per person.")
    print("Total cost for smokers is " + str(round(smoker_total_cost,2)) + " with an average cost of " + str(round(smoker_avg_cost,2)) + " per person.")

# smoker_vs_nonsmoker()

def average_num_of_children_per_family():
    total_children = 0
    family_count = 0

    for key in patient_information:
        if int(patient_information[key]["children"]) > 0:
            current_children = int(patient_information[key]["children"])
            total_children += current_children
            family_count += 1
    average_children = total_children/family_count
    print("The average number of children per family with children is " + str(round(average_children)) + ".")

# average_num_of_children_per_family()

def average_bmi_of_insured():
    total_bmi = 0
    count = 0
    for key in patient_information:
        current_bmi = float(patient_information[key]["bmi"])
        total_bmi += current_bmi
        count += 1

    average_bmi = total_bmi/count
    print("The average BMI for the insured is " + str(round(average_bmi,2)) + ".")

# average_bmi_of_insured()

def male_vs_female_cost():
    female_count = 0
    male_count = 0
    total_female_cost = 0
    total_male_cost = 0
    patients_without_sex = 0

    for key in patient_information:
        if patient_information[key]["sex"] == "female":
            total_female_cost += float(patient_information[key]["charges"])
            female_count += 1
        elif patient_information[key]["sex"] == "male":
            total_male_cost += float(patient_information[key]["charges"])
            male_count += 1
        else:
            patients_without_sex += 1

    avg_female_cost = round(total_female_cost/female_count,2)
    avg_male_cost = round(total_male_cost/male_count,2)

    print("The average cost of a male to be insured is " + str(avg_male_cost) + " and the average cost for a female to be insured is " + str(avg_female_cost) + ".")

# male_vs_female_cost()

def male_vs_female_smoker():
    female_smoker_count = 0
    male_smoker_count = 0
    female_smoker_charges = 0
    male_smoker_charges = 0

    for key in patient_information:
        if patient_information[key]["sex"] == "female" and patient_information[key]["smoker"] == "yes":
            female_smoker_charges += float(patient_information[key]["charges"])
            female_smoker_count += 1
        elif patient_information[key]["sex"] == "male" and patient_information[key]["smoker"] == "yes":
            male_smoker_charges += float(patient_information[key]["charges"])
            male_smoker_count += 1
        else:
            continue

    female_avg_smoker_cost = round(female_smoker_charges/female_smoker_count,2)
    male_avg_smoker_cost = round(male_smoker_charges/male_smoker_count,2)

    print("The average cost of a male smoker is " + str(male_avg_smoker_cost) + " and the average cost of a female smoker is " + str(female_avg_smoker_cost) + ".")

# male_vs_female_smoker()

def avg_male_age_vs_avg_female_age():
    male_age_total = 0
    female_age_total = 0
    male_age_count = 0
    female_age_count = 0
    patients_missing_sex = 0

    for key in patient_information:
        if patient_information[key]["sex"] == "female":
            male_age_total += int(patient_information[key]["age"])
            male_age_count += 1
        elif patient_information[key]["sex"] == "male":
            female_age_total += int(patient_information[key]["age"])
            female_age_count += 1
        else:
            patients_missing_sex += 1

    avg_male_age_insured = round(male_age_total/male_age_count)
    avg_female_age_insured = round(female_age_total/female_age_count)

    print("There are " + str(male_age_count) + " males insured and the average age of a male insured is " + str(avg_male_age_insured) + ".")
    print("There are " + str(female_age_count) + " females insured and the average age of a female insured is " + str(avg_female_age_insured) + ".")

# avg_male_age_vs_avg_female_age()

def male_vs_female_nonsmoker():
    female_nonsmoker_count = 0
    male_nonsmoker_count = 0
    female_nonsmoker_charges = 0
    male_nonsmoker_charges = 0

    for key in patient_information:
        if patient_information[key]["sex"] == "female" and patient_information[key]["smoker"] == "no":
            female_nonsmoker_charges += float(patient_information[key]["charges"])
            female_nonsmoker_count += 1
        elif patient_information[key]["sex"] == "male" and patient_information[key]["smoker"] == "no":
            male_nonsmoker_charges += float(patient_information[key]["charges"])
            male_nonsmoker_count += 1
        else:
            continue

    female_avg_nonsmoker_cost = round(female_nonsmoker_charges/female_nonsmoker_count,2)
    male_avg_nonsmoker_cost = round(male_nonsmoker_charges/male_nonsmoker_count,2)

    print("The average cost of a male nonsmoker is " + str(male_avg_nonsmoker_cost) + " and the average cost of a female nonsmoker is " + str(female_avg_nonsmoker_cost) + ".")

# male_vs_female_nonsmoker()

def stats_for_insured_in_20s():
    child_count_20s = 0
    smokers_in_20s = 0
    males_in_20s = 0
    females_in_20s = 0
    male_cost_in_20s_total = 0
    female_cost_in_20s_total = 0
    total_insured_in_20s = 0
    insured_missing_sex_info_in_20s = 0
    southwest_total_in_20s = 0
    southeast_total_in_20s = 0
    northeast_total_in_20s = 0
    northwest_total_in_20s = 0
    # Loop through record of insured
    for key in patient_information:
        # Check if insured is within specified age range
        if int(patient_information[key]["age"]) >= 20 and int(patient_information[key]["age"]) < 30:
            # Check if insured is a smoker in age range
            if patient_information[key]["smoker"] == "yes":
                smokers_in_20s += 1
            # Check if insured has children
            if int(patient_information[key]["children"]) > 0:
                child_count_20s += int(patient_information[key]["children"])
            # Check for sex designation in age range
            if patient_information[key]["sex"] == "male":
                males_in_20s += 1
                male_cost_in_20s_total += float(patient_information[key]["charges"])
            elif patient_information[key]["sex"] == "female":
                females_in_20s += 1
                female_cost_in_20s_total += float(patient_information[key]["charges"])
            else:
                insured_missing_sex_info_in_20s += 1
            # Count where insured live in age range
            if patient_information[key]["region"] == "southwest":
                southwest_total_in_20s += 1
            elif patient_information[key]["region"] == "southeast":
                southeast_total_in_20s += 1
            elif patient_information[key]["region"] == "northeast":
                northeast_total_in_20s += 1
            elif patient_information[key]["region"] == "northwest":
                northwest_total_in_20s += 1
            # Set insured total in their 20s
            total_insured_in_20s += 1
        # Loop to next iteration if current age not in range
        else:
            continue
    # Set variable to compare regional population totals of those insured and in their 20s.
    max_population = southeast_total_in_20s
    # Runs stats on insured in their 20s
    if total_insured_in_20s > 0:
        if insured_missing_sex_info_in_20s > 0:
            print("There are " + str(insured_missing_sex_info_in_20s) + " records of insured in their 20s missing a sex designation.")
        # Check which region the majority of insured in their 20s lives.
        if southwest_total_in_20s > max_population and northeast_total_in_20s < max_population and northwest_total_in_20s < max_population:
            print("A majority of the insured in their 20s live in the southwest.")
        elif northwest_total_in_20s > max_population and northeast_total_in_20s < max_population:
            print("A majority of the insured in their 20s live in the northwest.")
        elif northeast_total_in_20s > max_population:
            print("A majority of the insured in their 20s live in the northeast.")
        else:
            print("A majority of the insured in their 20s live in the southeast.")
        # Stats on males in their 20s
        if males_in_20s > 0:
            avg_male_cost_in_20s = round(male_cost_in_20s_total / males_in_20s, 2)
            print("There are " + str(
                males_in_20s) + " males in their 20's and the average insurance cost of a male in their 20's is " + str(
                avg_male_cost_in_20s))
        else:
            print("There are no males insured in their 20's.")
        # Stats on females in their 20s
        if females_in_20s > 0:
            avg_female_cost_in_20s = round(female_cost_in_20s_total / females_in_20s, 2)
            print("There are " + str(
                females_in_20s) + " females in their 20's and the average insurance cost of a female in their 20's is " + str(
                avg_female_cost_in_20s))
        else:
            print("There are no females insured in their 20's.")
        # Avg number of children insured in their 20s has
        if child_count_20s > 0:
            avg_children_in_20s = round(child_count_20s / (total_insured_in_20s))
            print("The average number of children someone in their 20's has is " + str(avg_children_in_20s))
        else:
            print("There is no one insured in their 20's that has children.")
        # Stats on insured in their 20s that are smokers
        if smokers_in_20s > 0 and total_insured_in_20s > 0:
            print("The number of 20 to 30 year olds insured is " + str(total_insured_in_20s) + ".")
            print("The number of 20 to 30 year olds that are smokers is " + str(smokers_in_20s) + " which is " + str(
                round((smokers_in_20s / (total_insured_in_20s)) * 100, 2)) + " percent of 20 to 30 year olds.")
        else:
            print("There are no smokers that are insured and in their 20's.")
    else:
        print("No one is insured that is in their 20's.")

# stats_for_insured_in_20s()

def stats_for_insured_in_30s():
    child_count_30s = 0
    smokers_in_30s = 0
    males_in_30s = 0
    females_in_30s = 0
    male_cost_in_30s_total = 0
    female_cost_in_30s_total = 0
    total_insured_in_30s = 0
    insured_missing_sex_info_in_30s = 0
    southwest_total_in_30s = 0
    southeast_total_in_30s = 0
    northeast_total_in_30s = 0
    northwest_total_in_30s = 0
    # Loop through record of insured
    for key in patient_information:
        # Check if insured is within specified age range
        if int(patient_information[key]["age"]) >= 30 and int(patient_information[key]["age"]) < 40:
            # Check if insured is a smoker in age range
            if patient_information[key]["smoker"] == "yes":
                smokers_in_30s += 1
            # Check if insured has children in age range
            if int(patient_information[key]["children"]) > 0:
                child_count_30s += int(patient_information[key]["children"])
            # Check for sex designation in age range
            if patient_information[key]["sex"] == "male":
                males_in_30s += 1
                male_cost_in_30s_total += float(patient_information[key]["charges"])
            elif patient_information[key]["sex"] == "female":
                females_in_30s += 1
                female_cost_in_30s_total += float(patient_information[key]["charges"])
            else:
                insured_missing_sex_info_in_30s += 1
            # Count where insured live in age range
            if patient_information[key]["region"] == "southwest":
                southwest_total_in_30s += 1
            elif patient_information[key]["region"] == "southeast":
                southeast_total_in_30s += 1
            elif patient_information[key]["region"] == "northeast":
                northeast_total_in_30s += 1
            elif patient_information[key]["region"] == "northwest":
                northwest_total_in_30s += 1
            # Set insured total in their 30s
            total_insured_in_30s += 1
        # Loop to next iteration if current age not in range
        else:
            continue

    # Set variable to compare regional population totals of those insured and in their 30s.
    max_population = southeast_total_in_30s
    # Runs stats on insured in their 30s
    if total_insured_in_30s > 0:
        # Notify user if any insured in their 30s is missing a sex designation
        if insured_missing_sex_info_in_30s > 0:
            print("There are " + str(insured_missing_sex_info_in_30s) + " records of insured in their 30s missing a sex designation.")
        # Check which region the majority of insured in their 30s lives.
        if southwest_total_in_30s > max_population and northeast_total_in_30s < max_population and northwest_total_in_30s < max_population:
            print("A majority of the insured in their 30s live in the southwest.")
        elif northwest_total_in_30s > max_population and northeast_total_in_30s < max_population:
            print("A majority of the insured in their 30s live in the northwest.")
        elif northeast_total_in_30s > max_population:
            print("A majority of the insured in their 30s live in the northeast.")
        else:
            print("A majority of the insured in their 30s live in the southeast.")
        # Stats on males in their 30s
        if males_in_30s > 0:
            avg_male_cost_in_30s = round(male_cost_in_30s_total / males_in_30s, 2)
            print("There are " + str(
                males_in_30s) + " males in their 30's and the average insurance cost of a male in their 30's is " + str(
                avg_male_cost_in_30s))
        else:
            print("There are no males insured in their 30's.")
        # Stats on female in their 30s
        if females_in_30s > 0:
            avg_female_cost_in_30s = round(female_cost_in_30s_total / females_in_30s, 2)
            print("There are " + str(
                females_in_30s) + " females in their 30's and the average insurance cost of a female in their 30's is " + str(
                avg_female_cost_in_30s))
        else:
            print("There are no females insured in their 30's.")
        # Avg number of children insured in their 30s has
        if child_count_30s > 0:
            avg_children_in_30s = round(child_count_30s / (total_insured_in_30s))
            print("The average number of children someone in their 30's has is " + str(avg_children_in_30s))
        else:
            print("There is no one insured in their 30's that has children.")\
        # Stats on smokers in their 30s
        if smokers_in_30s > 0 and total_insured_in_30s > 0:
            print("The number of 30 to 40 year olds insured is " + str(total_insured_in_30s) + ".")
            print("The number of 30 to 40 year olds that are smokers is " + str(smokers_in_30s) + " which is " + str(
                round((smokers_in_30s / (total_insured_in_30s)) * 100, 2)) + " percent of 30 to 40 year olds.")
        else:
            print("There are no smokers that are insured and in their 30's.")
    else:
        print("No one is insured that is in their 30's.")

# stats_for_insured_in_30s()

def stats_for_insured_in_40s():
    child_count_40s = 0
    smokers_in_40s = 0
    males_in_40s = 0
    females_in_40s = 0
    male_cost_in_40s_total = 0
    female_cost_in_40s_total = 0
    total_insured_in_40s = 0
    insured_missing_sex_info_in_40s = 0
    southwest_total_in_40s = 0
    southeast_total_in_40s = 0
    northeast_total_in_40s = 0
    northwest_total_in_40s = 0
    # Loop through insured record
    for key in patient_information:
        # Check to make sure insured is within specified age range
        if int(patient_information[key]["age"]) >= 40 and int(patient_information[key]["age"]) < 50:
            # Check to see if insured is a smoker in age range
            if patient_information[key]["smoker"] == "yes":
                smokers_in_40s += 1
            # Check if insured has children in age range
            if int(patient_information[key]["children"]) > 0:
                child_count_40s += int(patient_information[key]["children"])
            # Check for sex designation of insured in age range
            if patient_information[key]["sex"] == "male":
                males_in_40s += 1
                male_cost_in_40s_total += float(patient_information[key]["charges"])
            elif patient_information[key]["sex"] == "female":
                females_in_40s += 1
                female_cost_in_40s_total += float(patient_information[key]["charges"])
            else:
                insured_missing_sex_info_in_40s += 1
                # Count where insured live in age range
            if patient_information[key]["region"] == "southwest":
                southwest_total_in_40s += 1
            elif patient_information[key]["region"] == "southeast":
                southeast_total_in_40s += 1
            elif patient_information[key]["region"] == "northeast":
                northeast_total_in_40s += 1
            elif patient_information[key]["region"] == "northwest":
                northwest_total_in_40s += 1
            # Set total number of insured in their 40s
            total_insured_in_40s += 1
        # Loop to next iteration if current age not in range
        else:
            continue
    # Set variable to compare regional population totals of those insured and in their 40s.
    max_population_in_40s = southeast_total_in_40s
    # Runs stats on insured in their 40s
    if total_insured_in_40s > 0:
        # Notify user if any of the insured are missing a sex designation
        if insured_missing_sex_info_in_40s > 0:
            print("There are " + str(insured_missing_sex_info_in_40s) + " records of insured in their 40s missing a sex designation.")
        # Check which region the majority of insured in their 40s lives.
        if southwest_total_in_40s > max_population_in_40s and northeast_total_in_40s < max_population_in_40s and northwest_total_in_40s < max_population_in_40s:
            print("A majority of the insured in their 40s live in the southwest.")
        elif northwest_total_in_40s > max_population_in_40s and northeast_total_in_40s < max_population_in_40s:
            print("A majority of the insured in their 40s live in the northwest.")
        elif northeast_total_in_40s > max_population_in_40s:
            print("A majority of the insured in their 40s live in the northeast.")
        else:
            print("A majority of the insured in their 40s live in the southeast.")
        # Stats on males in their 40s
        if males_in_40s > 0:
            avg_male_cost_in_40s = round(male_cost_in_40s_total / males_in_40s, 2)
            print("There are " + str(
                males_in_40s) + " males in their 40's and the average insurance cost of a male in their 40's is " + str(
                avg_male_cost_in_40s))
        else:
            print("There are no males insured in their 40's.")
        # Stats on females in their 40s
        if females_in_40s > 0:
            avg_female_cost_in_40s = round(female_cost_in_40s_total / females_in_40s, 2)
            print("There are " + str(
                females_in_40s) + " females in their 40's and the average insurance cost of a female in their 40's is " + str(
                avg_female_cost_in_40s))
        else:
            print("There are no females insured in their 40's.")
        # Avg number of children a family in their 40s has
        if child_count_40s > 0:
            avg_children_in_40s = round(child_count_40s / (total_insured_in_40s))
            print("The average number of children someone in their 40's has is " + str(avg_children_in_40s))
        else:
            print("There is no one insured in their 40's that has children.")
        # Stats on smokers in their 40s
        if smokers_in_40s > 0 and total_insured_in_40s > 0:
            print("The number of 40 to 50 year olds insured is " + str(total_insured_in_40s) + ".")
            print("The number of 40 to 50 year olds that are smokers is " + str(smokers_in_40s) + " which is " + str(
                round((smokers_in_40s / (total_insured_in_40s)) * 100, 2)) + " percent of 40 to 50 year olds.")
        else:
            print("There are no smokers that are insured and in their 40's.")
    else:
        print("No one is insured that is in their 40's.")

# stats_for_insured_in_40s()

def stats_for_insured_in_50s():
    child_count_50s = 0
    smokers_in_50s = 0
    males_in_50s = 0
    females_in_50s = 0
    male_cost_in_50s_total = 0
    female_cost_in_50s_total = 0
    total_insured_in_50s = 0
    insured_missing_sex_info_in_50s = 0
    southwest_total_in_50s = 0
    southeast_total_in_50s = 0
    northeast_total_in_50s = 0
    northwest_total_in_50s = 0
    area_in_50s = ""
    # Loop through insured record
    for key in patient_information:
        # Check if insured is within specified age range
        if int(patient_information[key]["age"]) >= 50 and int(patient_information[key]["age"]) < 60:
            # Check if insured is a smoker in age range
            if patient_information[key]["smoker"] == "yes":
                smokers_in_50s += 1
            # Check if insured has children in age range
            if int(patient_information[key]["children"]) > 0:
                child_count_50s += int(patient_information[key]["children"])
            # Check for insured sex designation in age range
            if patient_information[key]["sex"] == "male":
                males_in_50s += 1
                male_cost_in_50s_total += float(patient_information[key]["charges"])
            elif patient_information[key]["sex"] == "female":
                females_in_50s += 1
                female_cost_in_50s_total += float(patient_information[key]["charges"])
            else:
                insured_missing_sex_info_in_50s += 1
                # Count where insured live in age range
            if patient_information[key]["region"] == "southwest":
                southwest_total_in_50s += 1
            elif patient_information[key]["region"] == "southeast":
                southeast_total_in_50s += 1
            elif patient_information[key]["region"] == "northeast":
                northeast_total_in_50s += 1
            elif patient_information[key]["region"] == "northwest":
                northwest_total_in_50s += 1
            # Set number of total insured in their 50s
            total_insured_in_50s += 1
        # Loop to next iteration if current age not in range
        else:
            continue

    # Set variable to compare regional population totals of those insured and in their 50s.
    max_population_in_50s = 0
        # Stats on insured in their 50s
    if total_insured_in_50s > 0:
        #Notify user if insured in their 50s is missing a sex designation
        if insured_missing_sex_info_in_50s > 0:
            print("There are " + str(insured_missing_sex_info_in_50s) + " records of insured in their 50s missing a sex designation.")
        # Check which region the majority of insured in their 50s lives.
        if southwest_total_in_50s > max_population_in_50s:
            max_population_in_50s = southwest_total_in_50s
            area_in_50s = "southwest"
        elif northwest_total_in_50s > max_population_in_50s:
            max_population_in_50s = northwest_total_in_50s
            area_in_50s = "northwest"
        elif northeast_total_in_50s > max_population_in_50s:
            max_population_in_50s = northeast_total_in_50s
            area_in_50s = "northeast"
        print("A majority of the insured in their 50s live in the " + area_in_50s + ".")
        # Stats on males in their 50s
        if males_in_50s > 0:
            avg_male_cost_in_50s = round(male_cost_in_50s_total / males_in_50s, 2)
            print("There are " + str(
                males_in_50s) + " males in their 50's and the average insurance cost of a male in their 50's is " + str(
                avg_male_cost_in_50s))
        else:
            print("There are no males insured in their 50's.")
        # Stats on females in their 50s
        if females_in_50s > 0:
            avg_female_cost_in_50s = round(female_cost_in_50s_total / females_in_50s, 2)
            print("There are " + str(
                females_in_50s) + " females in their 50's and the average insurance cost of a female in their 50's is " + str(
                avg_female_cost_in_50s))
        else:
            print("There are no females insured in their 50's.")
        # Avg number of children families in their 50s has
        if child_count_50s > 0:
            avg_children_in_50s = round(child_count_50s / (total_insured_in_50s))
            print("The average number of children someone in their 50's has is " + str(avg_children_in_50s))
        else:
            print("There is no one insured in their 50's that has children.")
        # Stats on smokers in their 50s
        if smokers_in_50s > 0 and total_insured_in_50s > 0:
            print("The number of 50 to 60 year olds insured is " + str(total_insured_in_50s) + ".")
            print("The number of 50 to 60 year olds that are smokers is " + str(smokers_in_50s) + " which is " + str(
                round((smokers_in_50s / (total_insured_in_50s)) * 100, 2)) + " percent of 50 to 60 year olds.")
        else:
            print("There are no smokers that are insured and in their 50's.")
    else:
        print("No one is insured that is in their 50's.")

# stats_for_insured_in_50s()

def stats_for_insured_in_60s():
    child_count_60s = 0
    smokers_in_60s = 0
    males_in_60s = 0
    females_in_60s = 0
    male_cost_in_60s_total = 0
    female_cost_in_60s_total = 0
    total_insured_in_60s = 0
    insured_missing_sex_info_in_60s = 0
    southwest_total_in_60s = 0
    southeast_total_in_60s = 0
    northeast_total_in_60s = 0
    northwest_total_in_60s = 0

    # Loop through insured records
    for key in patient_information:
        # Check if insured is within the specified age range
        if int(patient_information[key]["age"]) >= 60 and int(patient_information[key]["age"]) < 70:
            # Check for smokers in age range
            if patient_information[key]["smoker"] == "yes":
                smokers_in_60s += 1
            # Check for children in age range
            if int(patient_information[key]["children"]) > 0:
                child_count_60s += int(patient_information[key]["children"])
            # Check for sex designation in age range
            if patient_information[key]["sex"] == "male":
                males_in_60s += 1
                male_cost_in_60s_total += float(patient_information[key]["charges"])
            elif patient_information[key]["sex"] == "female":
                females_in_60s += 1
                female_cost_in_60s_total += float(patient_information[key]["charges"])
            else:
                insured_missing_sex_info_in_60s += 1
            if patient_information[key]["region"] == "southwest":
                southwest_total_in_60s += 1
            elif patient_information[key]["region"] == "southeast":
                southeast_total_in_60s += 1
            elif patient_information[key]["region"] == "northeast":
                northeast_total_in_60s += 1
            elif patient_information[key]["region"] == "northwest":
                northwest_total_in_60s += 1
            # Set number of total insured in their 60s
            total_insured_in_60s += 1
        # Loop to next iteration if current age not in range
        else:
            continue

    # Set variable to compare where majority of insured in their 60s reside
    max_population_in_60s = 0
    # Stats on insured in their 60s
    if total_insured_in_60s > 0:
        # Notify user if insured in their 50s is missing a sex designation
        if insured_missing_sex_info_in_60s > 0:
            print("There are " + str(
                insured_missing_sex_info_in_60s) + " records of insured in their 60s missing a sex designation.")
            # Check which region the majority of insured in their 40s lives.
            if southwest_total_in_60s > max_population_in_60s and northeast_total_in_60s < max_population_in_60s and northwest_total_in_60s < max_population_in_60s:
                print("A majority of the insured in their 60s live in the southwest.")
            elif northwest_total_in_60s > max_population_in_60s and northeast_total_in_60s < max_population_in_60s:
                print("A majority of the insured in their 60s live in the northwest.")
            elif northeast_total_in_60s > max_population_in_60s:
                print("A majority of the insured in their 60s live in the northeast.")
            else:
                print("A majority of the insured in their 60s live in the southeast.")
        # Stats on males in their 60s
        if males_in_60s > 0:
            avg_male_cost_in_60s = round(male_cost_in_60s_total / males_in_60s, 2)
            print("There are " + str(
                males_in_60s) + " males in their 60's and the average insurance cost of a male in their 60's is " + str(
                avg_male_cost_in_60s))
        else:
            print("There are no males insured in their 60's.")
        # Stats on females in their 60s
        if females_in_60s > 0:
            avg_female_cost_in_60s = round(female_cost_in_60s_total / females_in_60s, 2)
            print("There are " + str(
                females_in_60s) + " females in their 60's and the average insurance cost of a female in their 60's is " + str(
                avg_female_cost_in_60s))
        else:
            print("There are no females insured in their 60's.")
        # Avg number of children for those in their 60s
        if child_count_60s > 0:
            avg_children_in_60s = round(child_count_60s / (total_insured_in_60s))
            print("The average number of children someone in their 60's has is " + str(avg_children_in_60s))
        else:
            print("There is no one insured in their 60's that has children.")
        # Stats on smokers in their 60s
        if smokers_in_60s > 0 and total_insured_in_60s > 0:
            print("The number of 60 to 70 year olds insured is " + str(total_insured_in_60s) + ".")
            print("The number of 60 to 70 year olds that are smokers is " + str(smokers_in_60s) + " which is " + str(
                round((smokers_in_60s / (total_insured_in_60s)) * 100, 2)) + " percent of 60 to 70 year olds.")
        else:
            print("There are no smokers that are insured and in their 60's.")
    else:
        print("No one is insured that is in their 60's.")

# stats_for_insured_in_60s()


def stats_for_insured_in_70s():
    child_count_70s = 0
    smokers_in_70s = 0
    males_in_70s = 0
    females_in_70s = 0
    male_cost_in_70s_total = 0
    female_cost_in_70s_total = 0
    total_insured_in_70s = 0
    insured_missing_sex_info_in_70s = 0
    southwest_total_in_70s = 0
    southeast_total_in_70s = 0
    northeast_total_in_70s = 0
    northwest_total_in_70s = 0

    # Loop through insured records
    for key in patient_information:
        # Check if insured is within specified age range
        if int(patient_information[key]["age"]) >= 70 and int(patient_information[key]["age"]) < 80:
            # Check if insured is a smoker in age range
            if patient_information[key]["smoker"] == "yes":
                smokers_in_70s += 1
            # Check if insured has children in age range
            if int(patient_information[key]["children"]) > 0:
                child_count_70s += int(patient_information[key]["children"])
            # Check for sex designation in age range
            if patient_information[key]["sex"] == "male":
                males_in_70s += 1
                male_cost_in_70s_total += float(patient_information[key]["charges"])
            elif patient_information[key]["sex"] == "female":
                females_in_70s += 1
                female_cost_in_70s_total += float(patient_information[key]["charges"])
            else:
                insured_missing_sex_info_in_70s += 1
            if patient_information[key]["region"] == "southwest":
                southwest_total_in_70s += 1
            elif patient_information[key]["region"] == "southeast":
                southeast_total_in_70s += 1
            elif patient_information[key]["region"] == "northeast":
                northeast_total_in_70s += 1
            elif patient_information[key]["region"] == "northwest":
                northwest_total_in_70s += 1
            # Count number of insured in their 70s
            total_insured_in_70s += 1
        # Loop to next iteration if current age is outside of age range
        else:
            continue

    # Set variable to compare where majority of insured in their 70s reside
    max_population_in_70s = 0
    # Stats on insured in their 70s
    if total_insured_in_70s > 0:
        # Notify user if insured in their 50s is missing a sex designation
        if insured_missing_sex_info_in_70s > 0:
            print("There are " + str(
                insured_missing_sex_info_in_70s) + " records of insured in their 70s missing a sex designation.")
            # Check which region the majority of insured in their 70s lives.
            if southwest_total_in_70s > max_population_in_70s and northeast_total_in_70s < max_population_in_70s and northwest_total_in_70s < max_population_in_70s:
                print("A majority of the insured in their 70s live in the southwest.")
            elif northwest_total_in_70s > max_population_in_70s and northeast_total_in_70s < max_population_in_70s:
                print("A majority of the insured in their 70s live in the northwest.")
            elif northeast_total_in_70s > max_population_in_70s:
                print("A majority of the insured in their 70s live in the northeast.")
            else:
                print("A majority of the insured in their 70s live in the southeast.")
        if males_in_70s > 0:
            avg_male_cost_in_70s = round(male_cost_in_70s_total / males_in_70s, 2)
            print("There are " + str(males_in_70s) + " males in their 70's and the average insurance cost of a male in their 70's is " + str(avg_male_cost_in_70s))
        else:
            print("There are no males insured in their 70's.")
        if females_in_70s > 0:
            avg_female_cost_in_70s = round(female_cost_in_70s_total/females_in_70s,2)
            print("There are " + str(females_in_70s) + " females in their 70's and the average insurance cost of a female in their 70's is " + str(avg_female_cost_in_70s))
        else:
            print("There are no females insured in their 70's.")
        if child_count_70s > 0:
            avg_children_in_70s = round(child_count_70s/(total_insured_in_70s))
            print("The average number of children someone in their 70's has is " + str(avg_children_in_70s))
        else:
            print("There is no one insured in their 70's that has children.")
        if smokers_in_70s > 0 and total_insured_in_70s > 0:
            print("The number of 70 to 80 year olds insured is " + str(total_insured_in_70s) + ".")
            print("The number of 70 to 80 year olds that are smokers is " + str(smokers_in_70s) + " which is " + str(round((smokers_in_70s/(total_insured_in_70s))*100,2)) + " percent of 70 to 80 year olds.")
        else:
            print("There are no smokers that are insured and in their 70's.")
    else:
        print("No one is insured that is in their 70's.")

# stats_for_insured_in_70s()



