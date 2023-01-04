import datetime
import json
import gridstatus

def get_today_date_str():
    tday = datetime.date.today()
    tday_str = tday.strftime('%b %d, %Y')
    return tday_str


def get_iso8601_format_str(disp_time):
    return disp_time.isoformat()

CAISO_RENEWABLES = ['Solar', 'Wind', 'Geothermal',
                    'Small Hydro', 'Large Hydro', 'Batteries' ]
CAISO_OTHER = ['Biomass', 'Biogas', 'Coal', 'Nuclear', 'Natural Gas', 'Imports', 'Other']


def get_CAISO_data():
    # return percent of energy generated as renewable
    iso = gridstatus.CAISO()
    tmp_mix = iso.get_fuel_mix("latest")
    total_gen = tmp_mix.total_production
    if len(tmp_mix.mix) > 0:
        tmp_df = tmp_mix.mix.drop("Time", axis = 1).T
        tmp_df.columns= ['MW']
        tmp_df['percent'] = (tmp_df["MW"]/total_gen * 100).round(1) 
        ren_pc = 0
        for x in CAISO_RENEWABLES:
            if x == "Solar" and tmp_df.loc[x]['percent'] > 0:
                ren_pc = ren_pc + tmp_df.loc[x]['percent']
            else:
                ren_pc = ren_pc + tmp_df.loc[x]['percent']
        tmp_dict = {}
        #tmp_dict['Time'] = tmp_mix.mix.Time[0].strftime('%Y-%m-%d %X %z' )
        tmp_dict['Time'] =  get_iso8601_format_str(tmp_mix.mix.Time[0])
        tmp_dict['renewable_percent'] = ren_pc
        tmp_json_str = json.dumps(tmp_dict)
        return tmp_json_str
    else:  
        return ''   


Ercot_RENEWABLES = ['Solar', 'Wind', 'Power Storage', 'Hydro']
Ercot_OTHER = ['Coal and Lignite', 'Nuclear', 'Natural Gas', 'Other']
def get_Ercot_data():
    # return percent of energy generated as renewable
    iso = gridstatus.Ercot()
    tmp_mix = iso.get_fuel_mix("latest")
    total_gen = tmp_mix.total_production
    if len(tmp_mix.mix) > 0:
        tmp_df = tmp_mix.mix.drop("Time", axis = 1).T
        tmp_df.columns= ['MW']
        tmp_df['percent'] = (tmp_df["MW"]/total_gen * 100).round(1) 
        ren_pc = 0
        for x in Ercot_RENEWABLES:
            if x == "Solar" and tmp_df.loc[x]['percent'] > 0:
                ren_pc = ren_pc + tmp_df.loc[x]['percent']
            else:
                ren_pc = ren_pc + tmp_df.loc[x]['percent']
        tmp_dict = {}
        tmp_dict['Time'] = get_iso8601_format_str(tmp_mix.mix.Time[0])
        tmp_dict['renewable_percent'] = ren_pc
        tmp_json_str = json.dumps(tmp_dict)
        return tmp_json_str
    else:  
        return ''   


ISONE_RENEWABLES = ['Solar', 'Wind', 'Hydro']
ISONE_OTHER = ['Coal', 'Nuclear', 'Natural Gas', 'Other', 'Landfill Gas', 'Refuse', 'Wood']


def get_ISONE_data():
    # return percent of energy generated as renewable
    iso = gridstatus.ISONE()
    tmp_mix = iso.get_fuel_mix("latest")
    total_gen = tmp_mix.total_production
    if len(tmp_mix.mix) > 0:
        tmp_df = tmp_mix.mix.drop("Time", axis = 1).T
        tmp_df.columns= ['MW']
        tmp_df['percent'] = (tmp_df["MW"]/total_gen * 100).round(1) 
        ren_pc = 0
        for x in ISONE_RENEWABLES:
            if x == "Solar" and tmp_df.loc[x]['percent'] > 0:
                ren_pc = ren_pc + tmp_df.loc[x]['percent']
            else:
                ren_pc = ren_pc + tmp_df.loc[x]['percent']
        tmp_dict = {}
        tmp_dict['Time'] = get_iso8601_format_str(tmp_mix.mix.Time[0])
        tmp_dict['renewable_percent'] = ren_pc
        tmp_json_str = json.dumps(tmp_dict)
        return tmp_json_str
    else:  
        return ''   


NYISO_RENEWABLES = ['Other Renewables', 'Wind', 'Hydro']
NYISO_OTHER = ['Nuclear', 'Natural Gas', 'Other Fossil Fuels', 'Dual Fuel']
def get_NYISO_data():
    # return percent of energy generated as renewable
    iso = gridstatus.NYISO()
    #date_str = get_today_date_str()
    #tmp_df = iso.get_fuel_mix(date = date_str) 
    # if len(tmp_df) > 0:
    #     tmp_ser = tmp_df.iloc[-1] 
    #     tot_ren = 0
    #     for x in NYISO_RENEWABLES:
    #         if x == 'Solar':
    #             if tmp_ser['Solar'] > 0:
    #                 tot_ren = tot_ren + tmp_ser[x]
    #         else:
    #             tot_ren = tot_ren + tmp_ser[x]
    #     total_gen = tot_ren
    #     for y in NYISO_OTHER:
    #         total_gen = total_gen + tmp_ser[y]

    #     tmp_dict = {}
    #     tmp_dict['Time'] = tmp_ser['Time']
    #     tmp_dict['renewable_percent'] = int(tot_ren*100/total_gen)
    #     tmp_json_str = json.dumps(tmp_dict)
    #     return tmp_json_str
    # else:
    #     return ''
    tmp_mix = iso.get_fuel_mix("latest")
    total_gen = tmp_mix.total_production
    if len(tmp_mix.mix) > 0:
        tmp_df = tmp_mix.mix.drop("Time", axis = 1).T
        tmp_df.columns= ['MW']
        tmp_df['percent'] = (tmp_df["MW"]/total_gen * 100).round(1) 
        ren_pc = 0
        for x in NYISO_RENEWABLES:
            if x == "Solar" and tmp_df.loc[x]['percent'] > 0:
                ren_pc = ren_pc + tmp_df.loc[x]['percent']
            else:
                ren_pc = ren_pc + tmp_df.loc[x]['percent']
        tmp_dict = {}
        tmp_dict['Time'] = get_iso8601_format_str(tmp_mix.mix.Time[0])
        tmp_dict['renewable_percent'] = ren_pc
        tmp_json_str = json.dumps(tmp_dict)
        return tmp_json_str
    else:  
        return ''   


MISO_RENEWABLES = ['Wind', 'Solar']
MISO_OTHER = ['Nuclear', 'Natural Gas', 'Other', 'Coal']

def get_MISO_data():
    # return percent of energy generated as renewable
    iso = gridstatus.MISO()
    tmp_mix = iso.get_fuel_mix("latest")
    total_gen = tmp_mix.total_production
    if len(tmp_mix.mix) > 0:
        tmp_df = tmp_mix.mix.drop("Time", axis = 1).T
        tmp_df.columns= ['MW']
        tmp_df['percent'] = (tmp_df["MW"]/total_gen * 100).round(1) 
        ren_pc = 0
        for x in MISO_RENEWABLES:
            if x == "Solar" and tmp_df.loc[x]['percent'] > 0:
                ren_pc = ren_pc + tmp_df.loc[x]['percent']
            else:
                ren_pc = ren_pc + tmp_df.loc[x]['percent']
        tmp_dict = {}
        tmp_dict['Time'] = get_iso8601_format_str(tmp_mix.mix.Time[0])
        tmp_dict['renewable_percent'] = ren_pc
        tmp_json_str = json.dumps(tmp_dict)
        return tmp_json_str
    else:  
        return ''   


PJM_RENEWABLES = ['Other Renewables', 'Wind', 'Hydro', 'Solar', 'Storage']
PJM_OTHER = ['Nuclear', 'Gas', 'Coal', 'Other', 'Multiple Fuels', 'Oil']


def get_PJM_data():
    # return percent of energy generated as renewable
    iso = gridstatus.PJM()
    tmp_mix = iso.get_fuel_mix("latest")
    total_gen = tmp_mix.total_production
    if len(tmp_mix.mix) > 0:
        tmp_df = tmp_mix.mix.drop("Time", axis = 1).T
        tmp_df.columns= ['MW']
        tmp_df['percent'] = (tmp_df["MW"]/total_gen * 100).round(1) 
        ren_pc = 0
        for x in PJM_RENEWABLES:
            if x == "Solar" and tmp_df.loc[x]['percent'] > 0:
                ren_pc = ren_pc + tmp_df.loc[x]['percent']
            else:
                ren_pc = ren_pc + tmp_df.loc[x]['percent']
        tmp_dict = {}
        tmp_dict['Time'] = get_iso8601_format_str(tmp_mix.mix.Time[0])
        tmp_dict['renewable_percent'] = ren_pc
        tmp_json_str = json.dumps(tmp_dict)
        return tmp_json_str
    else:  
        return ''   


SPP_RENEWABLES = ['Hydro', 'Solar', 'Wind', ]
SPP_OTHER = ['Coal', 'Diesel Fuel Oil',  'Natural Gas', 'Nuclear',
       'Waste Disposal Services', 'Waste Heat', 'Other'  ]



def get_SPP_data():
    # return percent of energy generated as renewable
    iso = gridstatus.SPP()
    tmp_mix = iso.get_fuel_mix("latest")
    total_gen = tmp_mix.total_production
    if len(tmp_mix.mix) > 0:
        tmp_df = tmp_mix.mix.drop("Time", axis = 1).T
        tmp_df.columns= ['MW']
        tmp_df['percent'] = (tmp_df["MW"]/total_gen * 100).round(1) 
        ren_pc = 0
        for x in SPP_RENEWABLES:
            if x == "Solar" and tmp_df.loc[x]['percent'] > 0:
                ren_pc = ren_pc + tmp_df.loc[x]['percent']
            else:
                ren_pc = ren_pc + tmp_df.loc[x]['percent']
        tmp_dict = {}
        tmp_dict['Time'] = get_iso8601_format_str(tmp_mix.mix.Time[0])
        tmp_dict['renewable_percent'] = ren_pc
        tmp_json_str = json.dumps(tmp_dict)
        return tmp_json_str
    else:  
        return ''   


if __name__ == '__main__':
    tmpstr = get_NYISO_data()
    print(tmpstr)