import pandas as pd
import sys
from get_zip import get_zip_code

## on windows
#data_dirctory = "C:/Users/pvan002/Box/green_charging/data/"
# on linux
data_directory = "/home/viswanath/Documents/EPRI/green_charging/python_38/data/"

zipcode_utility_name = "nrel_iouzipcodes2018.csv"
zipcode_noniou_utility_name = "nrel_noniouzipcodes2018.csv"
utility_name_abbr_map = "iou_pyiso_map.csv"
noniou_utility_name_abbr_map = "noniou_pyiso_map.csv"

def find_utility(zip_code_str):
    # this function receives a zip code as string and returns a string representing the BA abbreviated names
    # that are suitable to use with pyiso library
    tmp_zip = int(zip_code_str)
    df_iou = pd.read_csv(data_directory + zipcode_utility_name)
    tmp_df_zip = df_iou[df_iou['zip'] == tmp_zip ]
    if len(tmp_df_zip) > 0:
        # Excel sheet contains more than one rows for a given zip code with the same utility name for other variables
        utility_name = tmp_df_zip.iloc[0]['utility_name']
        return "iou", utility_name
    else:
        df_noniou = pd.read_csv(data_directory + zipcode_noniou_utility_name)
        tmp_df_zip = df_noniou[df_noniou['zip'] == tmp_zip ]
        if len(tmp_df_zip) > 0:
            utility_name = tmp_df_zip.iloc[0]['utility_name']
            return "noniou", utility_name
        else:
            print("unable to find pyiso abbreviation for {}".format(zip_code_str))
            return "", ""

def find_iou_pyiso_abbreviation(utility_name):
    if len(utility_name) > 0:
        df_util_abbr = pd.read_csv(data_directory +  utility_name_abbr_map)
        tmp_df_abbr = df_util_abbr[df_util_abbr['db_name'] == utility_name]
        if len(tmp_df_abbr) > 0:
            abbr = tmp_df_abbr.iloc[0]['pyiso_ba_name']
            return abbr
        else:
            print("unable to locate abbreviation for the utility -> {0}".format(utility_name))
            return "NOT_AVAIL"
    else:
        print("invalid utility name (empty)")
        return ""

def find_noniou_pyiso_abbreviation(utility_name):
    if len(utility_name) > 0:
        df_util_abbr = pd.read_csv(data_directory +  noniou_utility_name_abbr_map)
        tmp_df_abbr = df_util_abbr[df_util_abbr['db_name'] == utility_name]
        if len(tmp_df_abbr) > 0:
            abbr = tmp_df_abbr.iloc[0]['eia_name']
            return abbr
        else:
            print("unable to locate abbreviation for the utility -> {0}".format(utility_name))
            return "NOT_AVAIL"
    else:
        print("invalid utility name (empty)")
        return ""



if __name__ == '__main__':
    if len(sys.argv) >= 3:
        zipcode = get_zip_code(sys.argv[1], sys.argv[2])
        print('zip code {0}'.format(zipcode))
        util_type, util_name = find_utility(zipcode)
        print("utility name :[{0}]".format(util_name))
        if len(util_name) > 0 and len(util_type) > 0:
            if util_type == "iou":
                pyiso_abbr = find_iou_pyiso_abbreviation(util_name)
            elif util_type == "noniou":
                pyiso_abbr = find_noniou_pyiso_abbreviation(util_name)
            else:
                pyiso_abbr = ""
        print("pyiso abbreviation = {0}".format(pyiso_abbr))
    else:
        print("program expects two inputs: latitude longitude")