print(tsla.history)


tesla_data = tsla.history(period='max')
print(tesla_data)

print(type(tesla_data))





tesla_data.reset_index(inplace=True)
tesla_data.head()


url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
html_data  = requests.get(url).text

soup=BeautifulSoup(html_data,'html5lib')


#print(soup.find_all("tbody"))[1]

tables1 = soup.find_all("tbody")

tesla_revenue = pd.DataFrame(columns= ['Date', 'Revenue'])

print(tesla_revenue)
print(type(tesla_revenue))

for row in soup.find('tbody').find_all('tr'):
    col = row.find_all("td") #html for data cell <td> cell a </td>
    date = col[0].text      # write to  corosponding tables
    revenue = col[1].text      # .text returns chld strings.
    tesla_revenue = tesla_revenue.append({'Date':date, 'Revenue':revenue}, ignore_index=True)


print(tesla_revenue)
