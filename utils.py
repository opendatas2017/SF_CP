import numpy as np # linear algebra
def create_df(train , test):
    print("---test and train dataframe will be changed")
    train = train.copy()
    test = test.copy()
    
    
    col_filter_test = ['brand' , 'color' , 'fuelType' , 'productionDate',  'vehicleTransmission' ,'Привод' , 'engine_capacity', 'odometer_value' ,'bodyType_new']
    col_filter_train = ['manufacturer_name' , 'color' , 'engine_fuel' ,  'year_produced', 'transmission' , 'drivetrain' , 'engine_capacity' ,'odometer_value', 'body_type' ]
    
    train['manufacturer_name'] =train['manufacturer_name'].apply(lambda row: row.upper())
    test_brand =  list(test['brand'].unique())
    train = train[train['manufacturer_name'].isin(test_brand)]
    #train = train[['manufacturer_name', 'model_name', 'transmission', 'color',
    #   'odometer_value', 'year_produced', 'engine_fuel', 'engine_capacity', 'body_type', 'has_warranty', 'state',
    #   'drivetrain', 'price_usd', 'is_exchangeable', 'location_region',
    #   'up_counter', 'duration_listed']]
    
    
    color_dic ={'синий':'blue', 'чёрный':'black', 'белый':'white', 'серый':'grey', 'серебристый':'silver', 'красный':'red',
       'фиолетовый':'violet', 'бежевый':'other', 'зелёный':'green', 'коричневый':'brown', 'золотистый':'other',
       'голубой':'blue', 'пурпурный':'other', 'жёлтый':'yellow', 'оранжевый':'orange', 'розовый':'other'}
    
    test = test.replace({"color": color_dic})
    
    fuel_dic={'gasoline':'бензин', 'hybrid-petrol':'гибрид', 'gas':'газ', 'diesel':'дизель', 'hybrid-diesel':'гибрид',
       'electric':'электро'}
    train=train.replace({"engine_fuel": fuel_dic})
    
    tr_dic={'автоматическая':'automatic', 'роботизированная':'automatic', 'вариатор':'automatic', 'механическая':'mechanical'}
    
    test = test.replace({"vehicleTransmission": tr_dic})
    
    drivetrain_dic={'полный':'all', 'передний':'front', 'задний':'rear'}
    
    test = test.replace({"Привод": drivetrain_dic})
    
    test['engine_capacity']=test['engineDisplacement'].apply(lambda row: row.split(' ')[0])
    test.loc[test.engine_capacity =='undefined','engine_capacity']='0'
    test['engine_capacity'] = test['engine_capacity'].astype(float)
    
    train['engine_capacity'].fillna(0, inplace=True)
    
    test['odometer_value'] = test['mileage']*1.60934
    
    test['bodyType_new']=test['bodyType'].apply(lambda row: row.split(' ')[0])
    
    bt_test_dic={'седан-хардтоп':'седан', 'тарга':'седан', 'родстер':'кабриолет' ,'купе-хардтоп':'купе',  'лимузин':'универсал'}
    bt_dic={'седан':'sedan', 'внедорожник':'suv', 'лифтбек':'liftback' , 'хэтчбек': 'hatchback' , 'универсал':'universal' , 'минивэн':'minivan' , 'микровэн':'minivan' ,
         'купе':'coupe' , 'фургон':'van' , 'пикап':'pickup' ,'компактвэн':'minivan' ,'лимузин':'limousine' , 'кабриолет':'cabriolet'}
    dt2_dic={'minibus':'minivan'}
    
    
    train = train.replace({'body_type': dt2_dic})
    test = test.replace({"bodyType_new": bt_test_dic})
    test = test.replace({"bodyType_new": bt_dic})
    
    # usd - > rub  on dec 2019 and create y
    y=train['price_usd']*62.93
    
    test['engine_capacity'] = test['engine_capacity'].astype(float)
    
    test = test[col_filter_test]
    train = train[col_filter_train]
    
    test.columns = col_filter_train
    train.columns = col_filter_train
    
    for col in ['year_produced' , 'engine_capacity' , 'odometer_value' ]:
        test[col] = test[col].astype(np.float64)
        train[col] = train[col].astype(np.float64)

    
    
    return train , test, y 