import os
import sys
import pandas as pd
from get_zip import get_zip_code
from pyiso_names import find_utility, find_pyiso_abbreviation
from pyiso import client_factory

def get_data(pyiso_abbr):
    tmp_client = client_factory(pyiso_abbr, timeout_seconds = 60)
    data = tmp_client.get_generation(latest = True)
    df_data = pd.DataFrame(data)
    print(df_data.columns)
    print(len(df_data))
    print(df_data.head())

def get_eia_data(pyiso_abbr):
    tmp_client = client_factory("EIA", timeout_seconds = 60)
    tmp_client.set_ba(pyiso_abbr)
    data = tmp_client.get_generation(latest = True)
    print(data)
    df_data = pd.DataFrame(data)
    print(df_data.columns)
    print(len(df_data))
    print(df_data.head())



if __name__ == '__main__':
    os.environ['EIA_KEY'] = '1e5e14ac05bfda21affef0ea92a26702'
    if len(sys.argv) >= 3:
        zipcode = get_zip_code(sys.argv[1], sys.argv[2])
        print('zip code {0}'.format(zipcode))
        util_name = find_utility(zipcode)
        print("utility name :[{0}]".format(util_name))        
        pyiso_abbr = find_pyiso_abbreviation(util_name)
        print("pyiso abbreviation = {0}".format(pyiso_abbr))
        get_eia_data(pyiso_abbr)
        get_data(pyiso_abbr)
    else:
        print("program expects two inputs: latitude longitude")



