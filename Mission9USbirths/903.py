#Calculating Number Of Births Each Month
#mission 9 and task 3
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
births_per_months={}
def month_birth(cdc_list):
    for row in cdc_list:
        month=row[1]
        birth=row[4]
        if month in births_per_months:
            births_per_months[month]=births_per_months[month]+birth
        else:
            births_per_months[month]=birth
    print(births_per_months)
month_birth(cdc_list)
