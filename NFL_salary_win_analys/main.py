import pandas as pd
import openpyxl
pd.options.display.float_format = '{:.2f}'.format
import matplotlib.pyplot as plt

pd.options.display.width = None
pd.options.display.max_columns = None
pd.set_option('display.max_rows', 3000)
pd.set_option('display.max_columns', 3000)

cap_2023 = 224800000.00

abrev = ['gb', 'kc', 'chi', 'det', 'min', 'atl', 'no', 'tb', 'car', 'den', 'lac', 'lv', 'lar', 'nyg', 'pit', 'dal',
         'sf']
plot_label = ['Green Bay', 'Kansas City', 'Chicago', 'Detroit', 'Minnesota', 'Atlanta', 'New Orleans', 'Tampa Bay',
              'Carolina', 'Denver', 'LA Chargers', 'Vegas', 'LA Rams', 'NY Giants', 'Pittsburgh', 'Dallas',
              'San Francisco']
main_color = ['green', 'red', 'darkorange', 'dodgerblue', 'purple', 'black', 'goldenrod', 'darkred', 'cyan', 'blue',
              'deepskyblue', 'black', 'yellow', 'darkblue', 'black', 'slategrey', 'goldenrod']
mark_color = ['yellow', 'red', 'navy', 'lightslategray', 'yellow', 'red', 'bisque', 'red', 'black', 'orange',
              'yellow', 'slategray', 'blue', 'red', 'gold', 'blue', 'red']

data_name = []
for i in abrev:
    #file_name = '/Users/abner/Desktop/' + i + '_snaps_cap_hit.xlsx'
    file_name = i + '_snaps_cap_hit.xlsx'
    data = pd.read_excel(file_name)
    data_name.append(data)

fig, ax = plt.subplots()
for i in range(0, len(data_name)):
    data = data_name[i]
    data.drop(columns=['Player', 'Snaps', 'Snaps_percentage', 'total_snaps', 'Cap_Hit'], inplace=True)
    cap_on_field = data.groupby("Week").sum().reset_index()
    cap_on_field['Cap_percentage'] = cap_on_field['Cap_on_field'] / cap_2023
    cap_on_field['Cap_percentage'] = round(cap_on_field['Cap_percentage'], 4) * 100

    cap_on_field.plot(x='Week', y='Cap_percentage', ax=ax, color=main_color[i], linestyle='-', marker='o',
                      markerfacecolor=mark_color[i], label=plot_label[i])
    plt.axhline(y=cap_on_field['Cap_percentage'].mean(), color=main_color[i], linestyle='--')

plt.xlabel("Week")
plt.ylabel("Percentage of salary cap playing each week")
plt.xticks(range(1, 23))

plt.show()
