# Creating A More General Function
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
def calc_counts(cdc_list,row_data):
    sum_data={}
    for row in cdc_list:
        day=row[row_data]
        birth=row[4]
        if day in sum_data:
            sum_data[day] = sum_data[day] + birth
        else:
            sum_data[day]=birth
    return(sum_data)
column_data=4
cdc_year_births=calc_counts(cdc_list,0)
cdc_month_births=calc_counts(cdc_list,1)
cdc_dom_births=calc_counts(cdc_list,2)
cdc_dow_births=calc_counts(cdc_list,3)
print('cdc_year_births',cdc_year_births)
print('cdc_month_births',cdc_month_births)
print('cdc_dom_births',cdc_dom_births)
print('cdc_dow_births',cdc_dow_births)