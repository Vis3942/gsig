import requests
import json
import datetime
import sys

EIA_KEY = '1e5e14ac05bfda21affef0ea92a26702'
EIA_BASE_URL = 'https://api.eia.gov/v2/electricity/rto/fuel-type-data/data'
#https://api.eia.gov/v2/electricity/rto/fuel-type-data/data?api_key=1e5e14ac05bfda21affef0ea92a26702&frequency=hourly&facets[respondent][]=NYIS&data[]=value
EIA_GEN_RENEWABLES_IDS = ["WAT", "SUN", "WND"]
EIA_GEN_IDS = ["OIL", "OTH", "COL", "NUC", "NG"]
# CAN "NUC" alias nuclear considered as clean energy

supported_ids = [
"EEI", "OVEC", "SOCO", "NW", "SW", "SE", "TEX", "AVA", "EPE", "GRIF",
"HGMA", "HST", "DOPD", "SCL", "TPWR", "DUK", "GVL", "NWMT", "SRP",
"CAR", "BANC", "SEPA", "AECI", "CPLW", "ISNE", "MISO", "PACE", "PJM",
"SWPP", "CENT", "AZPS", "GRID", "FMPP", "LDWP", "NYIS", "PSCO", "MIDW",
"BPAT", "GWA", "WWA", "CISO", "ERCO", "FPC", "PGE", "GLHB", "DEAA",
"TIDC", "AVRN", "AEC", "SCEG", "TEPC", "TVA", "WACM", "WALC", "TEC",
"MIDA", "FPL", "NSB", "GCPD", "WAUW", "CPLE", "JEA", "PACW", "PNM", "SEC",
"NE", "IPCO", "TAL", "CHPD", "LGEE", "NEVP", "PSEI", "SC", "US48", "CAL",
"FLA", "NY", "TEN", "IID", "SPA", "YAD"    
]

def get_eia_respondent_data(respondent_id):
    if respondent_id in supported_ids:
        api_url = EIA_BASE_URL + '?api_key=' + EIA_KEY + '&frequency=hourly&facets[respondent][]=' 
        api_url = api_url + respondent_id + '&data[]=value'
        #tmp_start = datetime.datetime.utcnow() # eia requires utc times
        tmp_start = datetime.date.today()
        tmp_start_str = tmp_start.strftime('%Y-%m-%d')
        tmp_end_str = (tmp_start + datetime.timedelta(days=2)).strftime('%Y-%m-%d')
        api_url = api_url + "&start=" + tmp_start_str + "&end="+ tmp_end_str
        try:
            response = requests.get(api_url)
            response.raise_for_status()
        except requests.exceptions.HTTPError as errh:
            print("Error http: {}".format(errh))
            return ""
        except requests.exceptions.ConnectionError as errc:
            #return "An Error Connecting to the API occurred:" + repr(errc)
            print("Error Connecting: {}".format(errc))
            return ""
        except requests.exceptions.Timeout as errt:
            #return "A Timeout Error occurred:" + repr(errt)
            print("Error Timeout: {}".format(errt))
        except requests.exceptions.RequestException as err:
            #return "An Unknown Error occurred" + repr(err)
            print("Error: {}".format(err))
            return ""

        print(response.json()['response'])
        tmp_data_dict = response.json()['response']['data']
        # assuming data is received in sorted order
        print("tmp data dict len = {0}".format(len(tmp_data_dict)))
        if len(tmp_data_dict) > 0:
            tmp_period_str = tmp_data_dict[-1]['period']
            #all generations for tmp_period_str
            tmp_gens = list(filter(lambda x: x['period'] == tmp_period_str, tmp_data_dict))
            total_gen = 0
            renewable_gen = 0
            for y in tmp_gens:
                total_gen = total_gen + y['value']
                if y['fueltype'] in EIA_GEN_RENEWABLES_IDS:
                    renewable_gen = renewable_gen + y['value']

            tmp_dict = {}
            tmp_dict['Time'] = tmp_period_str+":00:00"
            tmp_dict['renewable_percent'] = round(renewable_gen/total_gen * 100)
            tmp_json_str = json.dumps(tmp_dict)
            return tmp_json_str
        else:
            return ""
    else:
        return ""
         

if __name__ == '__main__':
    #specify the respondent id for eia data access
    if len(sys.argv) >= 2:
        tmp_ret_str = get_eia_respondent_data(sys.argv[1])
        print(tmp_ret_str)
    else:
        print("Requires 1 argument: string of respondent id for EIA")


