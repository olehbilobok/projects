tables = [
    {'name': 'cities', 'rows': 'city_id INT PRIMARY KEY,\
                                city_name VARCHAR(255)'
     },

    {'name': 'appartments', 'rows': 'appartment_id INT PRIMARY KEY,\
                                    operation_type INT,\
                                    city_name INT REFERENCES cities(city_id) ON DELETE CASCADE,\
                                    district_name VARCHAR(255),\
                                    street_name VARCHAR(255),\
                                    square_meters FLOAT,\
                                    rooms_count INT,\
                                    floor INT,\
                                    total_price VARCHAR(255),\
                                    created_at TIMESTAMP,\
                                    user_id INT,\
                                    photo VARCHAR(255)'
     }
]
