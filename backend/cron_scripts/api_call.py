# Builtins
from os import getenv
import requests
from argparse import ArgumentParser
from datetime import datetime

# Internals
from backend.logger import LOGGER as log

# Externals
import psycopg


def main(args):
    # basic assumption: throw away unused keys
    # this is handled by argsparse, no need to clean this aspect here
    weather_params = vars(args)
    log.info(f'weather request init args: {weather_params}')
    cleaned_params = {}

    # our allowed input keys, though argsparse would already deny other keys
    keys = ['lat','lon','units']
    unused_keys = []
    
    for key, val in weather_params.items():
        if key in keys:
            cleaned_params[key] = val
        else:
            unused_keys.append(key)

    if len(unused_keys) > 0:
        log.warning(f"unused keys submitted: {','.join(unused_keys)}")
        
    # TODO: clean keys properly at some point
    log.debug(f'cleaned request args:{cleaned_params}')
        
    # call url
    url = 'https://api.openweathermap.org/data/3.0/onecall'

    # default internal keys
    cleaned_params['exclude']='minutely,hourly,daily,alerts'
    # TODO: setup os env in docker
    cleaned_params['appid'] = getenv('API_KEY')
    
    resp = requests.get(url, params=cleaned_params).json()

    # TODO: if get returns None, fix error handling
    temp_time = datetime.fromtimestamp(resp.get('current').get('dt'))
    current_temp = resp.get('current').get('temp')
    temp_description = resp.get('current').get('weather')[0].get('description')
    
    log.info(f'retrieved weather data: [{temp_time}]:[{current_temp} degrees]'
             f':[description - {temp_description}]')
    
    # TODO: insert to db
    try:
        # TODO: os.getenv once docker setup
        # connection = psycopg.connect(
        #     user=getenv('DB_USER'),
        #     password=getenv('DB_PASSWORD'),
        #     host=getenv('HOST'),
        #     port=getenv('PORT'),
        #     database=getenv('DATABASE')
        # )
        # cursor = connection.cursor()

        postgres_insert_query = f'''
        INSERT INTO weather (
            id,
            datetime,
            temp,
            description,
            lat,
            lon
        ) VALUES (
            {temp_time},
            {current_temp},
            {temp_description},
            {cleaned_params.get("lat")},
            {cleaned_params.get("lon")}
        )
        '''
        
        log.debug(f'postgreSQL query:{postgres_insert_query}')
        # cursor.execute(postgres_insert_query)

        # connection.commit()
        # log.info("Record inserted successfully into mobile table")

    except (Exception, psycopg2.Error) as err:
        log.error(f"PostgreSQL failure:{err}")

    finally:
        pass
        # closing database connection.
        # if connection:
        #     cursor.close()
        #     connection.close()
    
if __name__=='__main__':
    # to run this:
    # python -m backend.cron_scripts.api_call -lat=-33.8660 -lon=18.5344 -u=metric
    # this sets PYTHONPATH so we can import our LOGGER from backend/logger
    # instantiate parser
    parser = ArgumentParser(
        prog='Weather API Caller',
        description='calls weather data based on cli args',
    )


    parser.add_argument('-lat',default=-33.8660,type=float)
    parser.add_argument('-lon',default=18.5344,type=float)
    parser.add_argument(
        '-u', '--units',choices=['metric','imperial'],default='metric',type=str
    )
    
    args = parser.parse_args()
    main(args)