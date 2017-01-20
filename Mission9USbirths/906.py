#Write a function that can calculate the min and max values for any dictionary that's passed in.
#Write a function that extracts the same values across years and calculates the differences between consecutive values
# to show if number of births is increasing or decreasing
#Find a way to combine the CDC data with the SSA data, which you can find here.
# Specifically, brainstorm ways to deal with the overlapping time periods in the datasets.
# https://github.com/fivethirtyeight/data/tree/master/births
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
def maxValue(data):
    maxValue=0
    maxVal={}
    key=0
    for el in data.items():
        if el[1]>maxValue:
            maxValue=el[1]
            key=el[0]
        else:
            maxValue = el[1]
    maxVal[key] = maxValue
    return maxVal
def minValue(data1):
    minVal=min(data1.values())
    result = [key for key, value in data1.items() if value == minVal]
    minValDict={result[0]:minVal}
    return minValDict
print('max',maxValue(cdc_year_births))
print(cdc_year_births)
print('min',minValue(cdc_year_births))
