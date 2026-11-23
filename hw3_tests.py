import data
import build_data
import unittest
import hw3


# These two values are defined to support testing below. The
# data within these structures should not be modified. Doing
# so will affect later tests.
#
# The data is defined here for visibility purposes in the context
# of this course.
full_data = build_data.get_data()

reduced_data = [
    data.CountyDemographics(
        {'Percent 65 and Older': 13.8,
         'Percent Under 18 Years': 25.2,
         'Percent Under 5 Years': 6.0},
        'Autauga County',
        {"Bachelor's Degree or Higher": 20.9,
         'High School or Higher': 85.6},
        {'American Indian and Alaska Native Alone': 0.5,
         'Asian Alone': 1.1,
         'Black Alone': 18.7,
         'Hispanic or Latino': 2.7,
         'Native Hawaiian and Other Pacific Islander Alone': 0.1,
         'Two or More Races': 1.8,
         'White Alone': 77.9,
         'White Alone, not Hispanic or Latino': 75.6},
        {'Per Capita Income': 24571,
         'Persons Below Poverty Level': 12.1,
         'Median Household Income': 53682},
        {'2010 Population': 54571,
         '2014 Population': 55395,
         'Population Percent Change': 1.5,
         'Population per Square Mile': 91.8},
        'AL'),
    data.CountyDemographics(
        {'Percent 65 and Older': 15.3,
         'Percent Under 18 Years': 25.1,
         'Percent Under 5 Years': 6.0},
        'Crawford County',
        {"Bachelor's Degree or Higher": 14.3,
         'High School or Higher': 82.2},
        {'American Indian and Alaska Native Alone': 2.5,
         'Asian Alone': 1.6,
         'Black Alone': 1.6,
         'Hispanic or Latino': 6.7,
         'Native Hawaiian and Other Pacific Islander Alone': 0.1,
         'Two or More Races': 2.8,
         'White Alone': 91.5,
         'White Alone, not Hispanic or Latino': 85.6},
        {'Per Capita Income': 19477,
         'Persons Below Poverty Level': 20.2,
         'Median Household Income': 39479},
        {'2010 Population': 61948,
         '2014 Population': 61697,
         'Population Percent Change': -0.4,
         'Population per Square Mile': 104.4},
        'AR'),
    data.CountyDemographics(
        {'Percent 65 and Older': 17.5,
         'Percent Under 18 Years': 18.1,
         'Percent Under 5 Years': 4.8},
        'San Luis Obispo County',
        {"Bachelor's Degree or Higher": 31.5,
         'High School or Higher': 89.6},
        {'American Indian and Alaska Native Alone': 1.4,
         'Asian Alone': 3.8,
         'Black Alone': 2.2,
         'Hispanic or Latino': 22.0,
         'Native Hawaiian and Other Pacific Islander Alone': 0.2,
         'Two or More Races': 3.4,
         'White Alone': 89.0,
         'White Alone, not Hispanic or Latino': 69.5},
        {'Per Capita Income': 29954,
         'Persons Below Poverty Level': 14.3,
         'Median Household Income': 58697},
        {'2010 Population': 269637,
         '2014 Population': 279083,
         'Population Percent Change': 3.5,
         'Population per Square Mile': 81.7},
        'CA'),
    data.CountyDemographics(
        {'Percent 65 and Older': 11.5,
         'Percent Under 18 Years': 21.7,
         'Percent Under 5 Years': 5.8},
        'Yolo County',
        {"Bachelor's Degree or Higher": 37.9,
         'High School or Higher': 84.3},
        {'American Indian and Alaska Native Alone': 1.8,
         'Asian Alone': 13.8,
         'Black Alone': 3.0,
         'Hispanic or Latino': 31.5,
         'Native Hawaiian and Other Pacific Islander Alone': 0.6,
         'Two or More Races': 5.0,
         'White Alone': 75.9,
         'White Alone, not Hispanic or Latino': 48.3},
        {'Per Capita Income': 27730,
         'Persons Below Poverty Level': 19.1,
         'Median Household Income': 55918},
        {'2010 Population': 200849,
         '2014 Population': 207590,
         'Population Percent Change': 3.4,
         'Population per Square Mile': 197.9},
        'CA'),
    data.CountyDemographics(
        {'Percent 65 and Older': 19.6,
         'Percent Under 18 Years': 25.6,
         'Percent Under 5 Years': 4.9},
        'Butte County',
        {"Bachelor's Degree or Higher": 17.9,
         'High School or Higher': 89.2},
        {'American Indian and Alaska Native Alone': 1.0,
         'Asian Alone': 0.3,
         'Black Alone': 0.2,
         'Hispanic or Latino': 5.8,
         'Native Hawaiian and Other Pacific Islander Alone': 0.2,
         'Two or More Races': 2.3,
         'White Alone': 96.1,
         'White Alone, not Hispanic or Latino': 90.6},
        {'Per Capita Income': 20995,
         'Persons Below Poverty Level': 15.7,
         'Median Household Income': 41131},
        {'2010 Population': 2891,
         '2014 Population': 2622,
         'Population Percent Change': -9.4,
         'Population per Square Mile': 1.3},
        'ID'),
    data.CountyDemographics(
        {'Percent 65 and Older': 15.3,
         'Percent Under 18 Years': 25.1,
         'Percent Under 5 Years': 6.9},
        'Pettis County',
        {"Bachelor's Degree or Higher": 15.2,
         'High School or Higher': 81.8},
        {'American Indian and Alaska Native Alone': 0.7,
         'Asian Alone': 0.7,
         'Black Alone': 3.4,
         'Hispanic or Latino': 8.3,
         'Native Hawaiian and Other Pacific Islander Alone': 0.3,
         'Two or More Races': 1.9,
         'White Alone': 92.9,
         'White Alone, not Hispanic or Latino': 85.5},
        {'Per Capita Income': 19709,
         'Persons Below Poverty Level': 18.4,
         'Median Household Income': 38580},
        {'2010 Population': 42201,
         '2014 Population': 42225,
         'Population Percent Change': 0.1,
         'Population per Square Mile': 61.9},
        'MO'),
    data.CountyDemographics(
        {'Percent 65 and Older': 18.1,
         'Percent Under 18 Years': 21.6,
         'Percent Under 5 Years': 6.5},
        'Weston County',
        {"Bachelor's Degree or Higher": 17.2,
         'High School or Higher': 90.2},
        {'American Indian and Alaska Native Alone': 1.7,
         'Asian Alone': 0.4,
         'Black Alone': 0.7,
         'Hispanic or Latino': 4.2,
         'Native Hawaiian and Other Pacific Islander Alone': 0.0,
         'Two or More Races': 2.2,
         'White Alone': 95.0,
         'White Alone, not Hispanic or Latino': 91.5},
        {'Per Capita Income': 28764,
         'Persons Below Poverty Level': 11.2,
         'Median Household Income': 55461},
        {'2010 Population': 7208,
         '2014 Population': 7201,
         'Population Percent Change': -0.1,
         'Population per Square Mile': 3.0},
        'WY')
    ]

# Index reference for reduced_data:
# 0 Autauga (AL)  1 Crawford (AR)  2 San Luis Obispo (CA)  3 Yolo (CA)
# 4 Butte (ID)    5 Pettis (MO)    6 Weston (WY)

class TestCases(unittest.TestCase):

    # Part 1
    # test population_total
    def test_population_total_empty(self):
        self.assertEqual(hw3.population_total([]), 0)

    def test_population_total_single(self):
        self.assertEqual(hw3.population_total([reduced_data[2]]), 279083)

    def test_population_total_reduced(self):
        self.assertEqual(hw3.population_total(reduced_data), 655813)

    def test_population_total_full(self):
        self.assertEqual(hw3.population_total(full_data), 318857056)

    # Part 2
    # test filter_by_state
    def test_filter_by_state_ca(self):
        self.assertEqual(hw3.filter_by_state(reduced_data, 'CA'),
                         [reduced_data[2], reduced_data[3]])

    def test_filter_by_state_other_state(self):
        self.assertEqual(hw3.filter_by_state(reduced_data, 'WY'),
                         [reduced_data[6]])

    def test_filter_by_state_absent(self):
        self.assertEqual(hw3.filter_by_state(reduced_data, 'NY'), [])

    def test_filter_by_state_empty(self):
        self.assertEqual(hw3.filter_by_state([], 'CA'), [])

    def test_filter_by_state_full_ca(self):
        ca = hw3.filter_by_state(full_data, 'CA')
        self.assertEqual(len(ca), 58)
        self.assertEqual(hw3.population_total(ca), 38802500)

    # Part 3
    # test population_by_education
    def test_population_by_education_single(self):
        # 279083 * 31.5 / 100
        self.assertAlmostEqual(
            hw3.population_by_education([reduced_data[2]],
                                        "Bachelor's Degree or Higher"),
            87911.145, places=3)

    def test_population_by_education_reduced(self):
        self.assertAlmostEqual(
            hw3.population_by_education(reduced_data,
                                        "Bachelor's Degree or Higher"),
            195114.091, places=3)

    def test_population_by_education_bad_key(self):
        self.assertEqual(
            hw3.population_by_education(reduced_data, 'Not a Key'), 0)

    def test_population_by_education_empty(self):
        self.assertEqual(
            hw3.population_by_education([], 'High School or Higher'), 0)

    # test population_by_ethnicity
    def test_population_by_ethnicity_single(self):
        # 279083 * 3.4 / 100
        self.assertAlmostEqual(
            hw3.population_by_ethnicity([reduced_data[2]],
                                        'Two or More Races'),
            9488.822, places=3)

    def test_population_by_ethnicity_two_counties(self):
        # 55395 * 2.7 / 100 + 61697 * 6.7 / 100
        self.assertAlmostEqual(
            hw3.population_by_ethnicity(reduced_data[0:2],
                                        'Hispanic or Latino'),
            5629.364, places=3)

    def test_population_by_ethnicity_bad_key(self):
        self.assertEqual(
            hw3.population_by_ethnicity(reduced_data, 'Not a Key'), 0)

    def test_population_by_ethnicity_empty(self):
        self.assertEqual(
            hw3.population_by_ethnicity([], 'Hispanic or Latino'), 0)

    # test population_below_poverty_level
    def test_population_below_poverty_level_single(self):
        # 279083 * 14.3 / 100
        self.assertAlmostEqual(
            hw3.population_below_poverty_level([reduced_data[2]]),
            39908.869, places=3)

    def test_population_below_poverty_level_two_counties(self):
        # 279083 * 14.3 / 100 + 207590 * 19.1 / 100
        self.assertAlmostEqual(
            hw3.population_below_poverty_level(reduced_data[2:4]),
            79558.559, places=3)

    def test_population_below_poverty_level_empty(self):
        self.assertEqual(hw3.population_below_poverty_level([]), 0)

    # Part 4
    # test percent_by_education
    def test_percent_by_education_single(self):
        self.assertAlmostEqual(
            hw3.percent_by_education([reduced_data[2]],
                                     "Bachelor's Degree or Higher"),
            31.5)

    def test_percent_by_education_weighted(self):
        # weighted by population, not a plain average of 31.5 and 17.9
        self.assertAlmostEqual(
            hw3.percent_by_education([reduced_data[2], reduced_data[4]],
                                     "Bachelor's Degree or Higher"),
            31.3734165, places=5)

    def test_percent_by_education_reduced(self):
        self.assertAlmostEqual(
            hw3.percent_by_education(reduced_data, 'High School or Higher'),
            86.3910853, places=5)

    def test_percent_by_education_bad_key_and_empty(self):
        self.assertEqual(hw3.percent_by_education(reduced_data, 'Not a Key'), 0)
        self.assertEqual(hw3.percent_by_education([], 'High School or Higher'), 0)

    # test percent_by_ethnicity
    def test_percent_by_ethnicity_single(self):
        self.assertAlmostEqual(
            hw3.percent_by_ethnicity([reduced_data[3]], 'Hispanic or Latino'),
            31.5)

    def test_percent_by_ethnicity_weighted(self):
        # plain average of 2.7 and 6.7 would be 4.7
        self.assertAlmostEqual(
            hw3.percent_by_ethnicity(reduced_data[0:2], 'Hispanic or Latino'),
            4.8076419, places=5)

    def test_percent_by_ethnicity_bad_key_and_empty(self):
        self.assertEqual(hw3.percent_by_ethnicity(reduced_data, 'Not a Key'), 0)
        self.assertEqual(hw3.percent_by_ethnicity([], 'White Alone'), 0)

    # test percent_below_poverty_level
    def test_percent_below_poverty_level_single(self):
        self.assertAlmostEqual(
            hw3.percent_below_poverty_level([reduced_data[2]]), 14.3)

    def test_percent_below_poverty_level_weighted(self):
        self.assertAlmostEqual(
            hw3.percent_below_poverty_level(reduced_data[2:4]),
            16.3474364, places=5)

    def test_percent_below_poverty_level_reduced(self):
        self.assertAlmostEqual(
            hw3.percent_below_poverty_level(reduced_data),
            16.4241505, places=5)

    def test_percent_below_poverty_level_empty(self):
        self.assertEqual(hw3.percent_below_poverty_level([]), 0)

    # Part 5
    # test education_greater_than
    def test_education_greater_than_excludes_equal(self):
        # San Luis Obispo is exactly 31.5, so only Yolo qualifies
        self.assertEqual(
            hw3.education_greater_than(reduced_data,
                                       "Bachelor's Degree or Higher", 31.5),
            [reduced_data[3]])

    def test_education_greater_than_multiple(self):
        self.assertCountEqual(
            hw3.education_greater_than(reduced_data,
                                       'High School or Higher', 89.0),
            [reduced_data[2], reduced_data[4], reduced_data[6]])

    def test_education_greater_than_none_and_empty(self):
        self.assertEqual(
            hw3.education_greater_than(reduced_data,
                                       "Bachelor's Degree or Higher", 60.0),
            [])
        self.assertEqual(
            hw3.education_greater_than([], 'High School or Higher', 0.0), [])

    # test education_less_than
    def test_education_less_than_excludes_equal(self):
        self.assertCountEqual(
            hw3.education_less_than(reduced_data,
                                    "Bachelor's Degree or Higher", 17.9),
            [reduced_data[1], reduced_data[5], reduced_data[6]])

    def test_education_less_than_one(self):
        self.assertEqual(
            hw3.education_less_than(reduced_data,
                                    "Bachelor's Degree or Higher", 15.0),
            [reduced_data[1]])

    def test_education_less_than_bad_key_and_empty(self):
        self.assertEqual(
            hw3.education_less_than(reduced_data, 'Not a Key', 100.0), [])
        self.assertEqual(
            hw3.education_less_than([], 'High School or Higher', 100.0), [])

    # test ethnicity_greater_than
    def test_ethnicity_greater_than_excludes_equal(self):
        # San Luis Obispo is exactly 22.0, so only Yolo qualifies
        self.assertEqual(
            hw3.ethnicity_greater_than(reduced_data, 'Hispanic or Latino',
                                       22.0),
            [reduced_data[3]])

    def test_ethnicity_greater_than_multiple(self):
        self.assertCountEqual(
            hw3.ethnicity_greater_than(reduced_data, 'Asian Alone', 1.5),
            [reduced_data[1], reduced_data[2], reduced_data[3]])

    def test_ethnicity_greater_than_none_and_empty(self):
        self.assertEqual(
            hw3.ethnicity_greater_than(reduced_data, 'Hispanic or Latino',
                                       50.0),
            [])
        self.assertEqual(
            hw3.ethnicity_greater_than([], 'Hispanic or Latino', 0.0), [])

    # test ethnicity_less_than
    def test_ethnicity_less_than_excludes_equal(self):
        self.assertCountEqual(
            hw3.ethnicity_less_than(reduced_data, 'Hispanic or Latino', 5.8),
            [reduced_data[0], reduced_data[6]])

    def test_ethnicity_less_than_all(self):
        self.assertCountEqual(
            hw3.ethnicity_less_than(reduced_data, 'Two or More Races', 10.0),
            reduced_data)

    def test_ethnicity_less_than_bad_key_and_empty(self):
        self.assertEqual(
            hw3.ethnicity_less_than(reduced_data, 'Not a Key', 100.0), [])
        self.assertEqual(
            hw3.ethnicity_less_than([], 'Hispanic or Latino', 100.0), [])

    # test below_poverty_level_greater_than
    def test_below_poverty_level_greater_than_excludes_equal(self):
        # Butte is exactly 15.7, so it is excluded
        self.assertCountEqual(
            hw3.below_poverty_level_greater_than(reduced_data, 15.7),
            [reduced_data[1], reduced_data[3], reduced_data[5]])

    def test_below_poverty_level_greater_than_none(self):
        self.assertEqual(
            hw3.below_poverty_level_greater_than(reduced_data, 30.0), [])

    def test_below_poverty_level_greater_than_empty(self):
        self.assertEqual(hw3.below_poverty_level_greater_than([], 0.0), [])

    # test below_poverty_level_less_than
    def test_below_poverty_level_less_than_excludes_equal(self):
        # Butte is exactly 15.7, so it is excluded
        self.assertCountEqual(
            hw3.below_poverty_level_less_than(reduced_data, 15.7),
            [reduced_data[0], reduced_data[2], reduced_data[6]])

    def test_below_poverty_level_less_than_one(self):
        self.assertEqual(
            hw3.below_poverty_level_less_than(reduced_data, 12.0),
            [reduced_data[6]])

    def test_below_poverty_level_less_than_empty(self):
        self.assertEqual(hw3.below_poverty_level_less_than([], 50.0), [])



if __name__ == '__main__':
    unittest.main()
