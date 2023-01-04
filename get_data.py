import os
import sys
from pathlib import Path, PurePath
import pandas as pd
from get_zip import get_zip_code
from pyiso_names import find_utility, find_iou_pyiso_abbreviation, find_noniou_pyiso_abbreviation
from gridstatus_get_data import get_CAISO_data, get_Ercot_data, get_ISONE_data, get_MISO_data
from gridstatus_get_data import get_SPP_data, get_PJM_data, get_NYISO_data
from eia_get_data import get_eia_respondent_data

JSON_FILE_OUTPUT = 'renewables.json'


if __name__ == '__main__':
    #os.environ['EIA_KEY'] = '1e5e14ac05bfda21affef0ea92a26702'
    # if only one argument it should be zip code within US
    # if two arguments it is latitude and longitude
    if len(sys.argv) == 2:
        zipcode = sys.argv[1]
    elif len(sys.argv) >= 3:
        zipcode = get_zip_code(sys.argv[1], sys.argv[2])
    else:
        zipcode = ''        
        print("program expects two inputs: latitude longitude or \n one input zip code")

    app_dir = os.getcwd()
    json_file = os.path.join(app_dir,JSON_FILE_OUTPUT)
    if os.path.exists(json_file):
        os.remove(json_file)

    if len(zipcode) > 0:
        print('zip code {0}'.format(zipcode))
        util_type, util_name = find_utility(zipcode)
        util_name = util_name.strip()
        print("utility name :[{0}]".format(util_name))
        if len(util_name) > 0 and len(util_type) > 0:
            if util_type == "iou":
                pyiso_abbr = find_iou_pyiso_abbreviation(util_name)
            elif util_type == "noniou":
                pyiso_abbr = find_noniou_pyiso_abbreviation(util_name)
            else:
                pyiso_abbr = ""
        print("pyiso abbreviation = {0}".format(pyiso_abbr))

        if pyiso_abbr == "NYISO":
            tmpstr = get_NYISO_data()
        elif pyiso_abbr == "CAISO":
            tmpstr = get_CAISO_data()
        elif pyiso_abbr == "Ercot":
            tmpstr = get_Ercot_data()
        elif pyiso_abbr == "ISONE":
            tmpstr = get_ISONE_data()
        elif pyiso_abbr == "MISO":
            tmpstr = get_MISO_data()
        elif pyiso_abbr == "PJM":
            tmpstr = get_PJM_data()
        elif pyiso_abbr == "SPP":
            tmpstr = get_SPP_data()
        else:
            tmpstr = get_eia_respondent_data(pyiso_abbr)

        if len(tmpstr) > 0:
            with open(json_file, "w") as outfile:
                outfile.write(tmpstr)

