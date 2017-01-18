#Calculating Number Of Births Each Day Of Week
#mission 9 task 4
file_name='births.csv'
def read_csv(file_name):
    file = open(file_name, 'r')
    temp_string_list = file.read().split('\n')
    string_list = temp_string_list[1:]
    final_list = []
    for row in string_list:
        string_fields=row.split(',')
        int_fields = []
        for item in string_fields:
            int_fields.append(int(item))
        final_list.append(int_fields)
    return(final_list)
cdc_list=read_csv(file_name)
birth_day={}
def birth_per_week(cdc_list):
    for row in cdc_list:
        day=row[3]
        birth=row[4]
        if day in birth_day:
            birth_day[day] = birth_day[day] + birth
        else:
            birth_day[day]=birth
    print(birth_day)
birth_per_week(cdc_list)