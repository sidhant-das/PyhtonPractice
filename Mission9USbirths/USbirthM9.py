file_name='births.csv'
def read_csv(file_name):
    file = open(file_name, 'r')
    temp_string_list = file.read().split('\n')
    string_list = temp_string_list[1:10]
    final_list = []
    for row in string_list:
        string_fields=row.split(',')
        int_fields = []
        for item in string_fields:
            int_fields.append(int(item))
        final_list.append(int_fields)
    return(final_list)
cdc_list=read_csv(file_name)
print(cdc_list)