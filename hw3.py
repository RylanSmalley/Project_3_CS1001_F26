from data import CountyDemographics


# Part 1 

# Purpose: add up the 2014 population of every county in the list.
# Input:   counties - a list of CountyDemographics objects (may be empty).
# Output:  the total 2014 population as an int (0 for an empty list).
def population_total(counties: list[CountyDemographics]) -> int:
    total = 0
    for county in counties:
        total += county.population['2014 Population']
    return int(total)


# Part 2 

# Purpose: keep only the counties that belong to the given state.
# Input:   counties - a list of CountyDemographics objects;
#          state - a two-letter state abbreviation such as 'CA'.
# Output:  a list of the CountyDemographics objects whose state matches
#          (an empty list if none match).
def filter_by_state(counties: list[CountyDemographics],
                    state: str) -> list[CountyDemographics]:
    result = []
    for county in counties:
        if county.state == state:
            result.append(county)
    return result


# Part 3 

# Purpose: estimate how many people fall in an education category.
# Input:   counties - a list of CountyDemographics objects;
#          key - an education key such as "Bachelor's Degree or Higher".
# Output:  the summed estimate of 2014 population * percent / 100 as a
#          float (0 if the key is not present).
def population_by_education(counties: list[CountyDemographics],
                            key: str) -> float:
    total = 0.0
    for county in counties:
        if key in county.education:
            total += (county.population['2014 Population']
                      * county.education[key] / 100)
    return total


# Purpose: estimate how many people fall in an ethnicity category.
# Input:   counties - a list of CountyDemographics objects;
#          key - an ethnicities key such as "Two or More Races".
# Output:  the summed estimate of 2014 population * percent / 100 as a
#          float (0 if the key is not present).
def population_by_ethnicity(counties: list[CountyDemographics],
                            key: str) -> float:
    total = 0.0
    for county in counties:
        if key in county.ethnicities:
            total += (county.population['2014 Population']
                      * county.ethnicities[key] / 100)
    return total


# Purpose: estimate how many people live below the poverty level.
# Input:   counties - a list of CountyDemographics objects.
# Output:  the summed estimate of 2014 population *
#          "Persons Below Poverty Level" / 100 as a float.
def population_below_poverty_level(
        counties: list[CountyDemographics]) -> float:
    total = 0.0
    for county in counties:
        if 'Persons Below Poverty Level' in county.income:
            total += (county.population['2014 Population']
                      * county.income['Persons Below Poverty Level'] / 100)
    return total


# Part 4 

# Purpose: find the population-weighted percent of people in an
#          education category across all of the given counties.
# Input:   counties - a list of CountyDemographics objects;
#          key - an education key.
# Output:  100 * (sub-population / total population) as a float
#          (0 if the key is missing or the total population is 0).
def percent_by_education(counties: list[CountyDemographics],
                         key: str) -> float:
    total = population_total(counties)
    if total == 0:
        return 0
    return 100 * population_by_education(counties, key) / total


# Purpose: find the population-weighted percent of people in an
#          ethnicity category across all of the given counties.
# Input:   counties - a list of CountyDemographics objects;
#          key - an ethnicities key.
# Output:  100 * (sub-population / total population) as a float
#          (0 if the key is missing or the total population is 0).
def percent_by_ethnicity(counties: list[CountyDemographics],
                         key: str) -> float:
    total = population_total(counties)
    if total == 0:
        return 0
    return 100 * population_by_ethnicity(counties, key) / total


# Purpose: find the population-weighted percent of people below the
#          poverty level across all of the given counties.
# Input:   counties - a list of CountyDemographics objects.
# Output:  100 * (people below poverty / total population) as a float
#          (0 if the total population is 0).
def percent_below_poverty_level(
        counties: list[CountyDemographics]) -> float:
    total = population_total(counties)
    if total == 0:
        return 0
    return 100 * population_below_poverty_level(counties) / total


# Part 5 

# Purpose: find counties whose education percent for a key is strictly
#          greater than a threshold.
# Input:   counties - a list of CountyDemographics objects;
#          key - an education key; threshold - a percentage value.
# Output:  a list of the matching CountyDemographics objects
#          (counties without the key are skipped).
def education_greater_than(counties: list[CountyDemographics], key: str,
                           threshold: float) -> list[CountyDemographics]:
    result = []
    for county in counties:
        if key in county.education and county.education[key] > threshold:
            result.append(county)
    return result


# Purpose: find counties whose education percent for a key is strictly
#          less than a threshold.
# Input:   counties - a list of CountyDemographics objects;
#          key - an education key; threshold - a percentage value.
# Output:  a list of the matching CountyDemographics objects
#          (counties without the key are skipped).
def education_less_than(counties: list[CountyDemographics], key: str,
                        threshold: float) -> list[CountyDemographics]:
    result = []
    for county in counties:
        if key in county.education and county.education[key] < threshold:
            result.append(county)
    return result


# Purpose: find counties whose ethnicity percent for a key is strictly
#          greater than a threshold.
# Input:   counties - a list of CountyDemographics objects;
#          key - an ethnicities key; threshold - a percentage value.
# Output:  a list of the matching CountyDemographics objects
#          (counties without the key are skipped).
def ethnicity_greater_than(counties: list[CountyDemographics], key: str,
                           threshold: float) -> list[CountyDemographics]:
    result = []
    for county in counties:
        if key in county.ethnicities and county.ethnicities[key] > threshold:
            result.append(county)
    return result


# Purpose: find counties whose ethnicity percent for a key is strictly
#          less than a threshold.
# Input:   counties - a list of CountyDemographics objects;
#          key - an ethnicities key; threshold - a percentage value.
# Output:  a list of the matching CountyDemographics objects
#          (counties without the key are skipped).
def ethnicity_less_than(counties: list[CountyDemographics], key: str,
                        threshold: float) -> list[CountyDemographics]:
    result = []
    for county in counties:
        if key in county.ethnicities and county.ethnicities[key] < threshold:
            result.append(county)
    return result


# Purpose: find counties whose "Persons Below Poverty Level" percent is
#          strictly greater than a threshold.
# Input:   counties - a list of CountyDemographics objects;
#          threshold - a percentage value.
# Output:  a list of the matching CountyDemographics objects.
def below_poverty_level_greater_than(
        counties: list[CountyDemographics],
        threshold: float) -> list[CountyDemographics]:
    result = []
    for county in counties:
        if county.income['Persons Below Poverty Level'] > threshold:
            result.append(county)
    return result


# Purpose: find counties whose "Persons Below Poverty Level" percent is
#          strictly less than a threshold.
# Input:   counties - a list of CountyDemographics objects;
#          threshold - a percentage value.
# Output:  a list of the matching CountyDemographics objects.
def below_poverty_level_less_than(
        counties: list[CountyDemographics],
        threshold: float) -> list[CountyDemographics]:
    result = []
    for county in counties:
        if county.income['Persons Below Poverty Level'] < threshold:
            result.append(county)
    return result
