# Script to load data from Json database into Objects to be treated
import os
import collections
import json
import sys
import data_srv as srv
path_to_structs = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'structs')
sys.path.insert(0, path_to_structs)
from heat_struct import Heat, Surfer
from round_struct import Round
from comp_struct import Competition


# inputs the user for the path to the dataset
def get_data_location() :
    bad_answer = True
    while bad_answer :
        dataset_path = input('Enter the path to the database [empty for default]:\n')
        if dataset_path == '' :
            current_path = os.path.dirname(os.path.abspath(__file__))
            temp = os.path.join(os.path.split(os.path.split(current_path)[0])[0],'wsl_predictor_bin')
            if not os.path.isdir(temp) :
                print('Could not find a default database')
                continue
            json_files = os.path.join(os.path.split(os.path.split(current_path)[0])[0],'wsl_predictor_bin', 'json_data')
            if not os.path.isdir(json_files) :
                print('Could not find a default database')
                continue
            dataset_path = json_files
            bad_answer = False
        elif not os.path.isdir(os.path.abspath(dataset_path)) :
            print('Folder {} not found'.format(dataset_path))
        elif not os.path.isdir(os.path.join(os.path.abspath(dataset_path), 'json_data')) :
            print('Folder you entered is not a dataset')
        else :
            bad_answer = False
    return dataset_path


# takes a filename for a year and returns a list of competition objects for this year
def get_comps_year(filename) :
    print(filename)
    files = [os.path.join(filename, file) for file in os.listdir(filename)]
    list_comps = []
    for file in files :
        print(file)
        with open(file) as fin :
            comp_data = json.load(fin)
            comp_object = Competition.from_json(comp_data)
            list_comps.append(comp_object)
    return list_comps


# takes the path to the database root and returns a list of Year named tuples
def load_database(filename) :
    try :
        start_year = int(input('What years do you want to load from dataset (initial) ? [2008-2017]  ').strip())
        end_year = int(input('What years do you want to load from dataset (final) ? [2008-2017]  ').strip())
    except ValueError :
        print('Enter years as valid integers')

    if not 2008 <= start_year <= 2017 or not 2008 <= end_year <= 2017:
        print('No info for provided years')
    elif start_year > end_year or not start_year or not end_year:
        print('please enter a working range and both limits')
    else :
        bad_answer = False


    subdirs = [x[0] for x in os.walk(filename)]

    dict_dataset = {}
    for dir_year in subdirs :
        # print(type(s), )
        try :
            int_year = int(os.path.split(dir_year)[1])
        except Exception :
            continue
        if start_year <= int_year <= end_year :
            list_comps = get_comps_year(os.path.abspath(dir_year))
            dict_dataset[int_year] = list_comps
    return dict_dataset


def main() :
    filename = get_data_location()
    dataset = load_database(filename)
    set = list(srv.get_surfers_list(2017, dataset))
    print (set)


if __name__ == '__main__' :
    main()
