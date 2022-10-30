import excel2json, wget, traceback, sys
import pandas, os, json



class Colors:
    reset = "\033[0m"

    # Black
    fgBlack = "\033[30m"
    fgBrightBlack = "\033[30;1m"
    bgBlack = "\033[40m"
    bgBrightBlack = "\033[40;1m"

    # Red
    fgRed = "\033[31m"
    fgBrightRed = "\033[31;1m"
    bgRed = "\033[41m"
    bgBrightRed = "\033[41;1m"

    # Green
    fgGreen = "\033[32m"
    fgBrightGreen = "\033[32;1m"
    bgGreen = "\033[42m"
    bgBrightGreen = "\033[42;1m"

    # Yellow
    fgYellow = "\033[33m"
    fgBrightYellow = "\033[33;1m"
    bgYellow = "\033[43m"
    bgBrightYellow = "\033[43;1m"

    # Blue
    fgBlue = "\033[34m"
    fgBrightBlue = "\033[34;1m"
    bgBlue = "\033[44m"
    bgBrightBlue = "\033[44;1m"
    # Magenta
    fgMagenta = "\033[35m"
    fgBrightMagenta = "\033[35;1m"
    bgMagenta = "\033[45m"
    bgBrightMagenta = "\033[45;1m"
    # Cyan
    fgCyan = "\033[36m"
    fgBrightCyan = "\033[36;1m"
    bgCyan = "\033[46m"
    bgBrightCyan = "\033[46;1m"
    # White
    fgWhite = "\033[37m"
    fgBrightWhite = "\033[37;1m"
    bgWhite = "\033[47m"
    bgBrightWhite = "\033[47;1m"


###########
color = Colors()
yellow = color.fgYellow
red = color.fgRed
blue = color.fgBlue
bblue = color.fgBrightBlue
cyan = color.fgCyan
bg_background = color.bgBlack
reset = color.reset




try:
    ''' Download link from file provided (rutgers server)'''
    URL = "https://rutgers.instructure.com/files/21024227/download?download_frd=1&verifier=lCAZtZ4pF98i8zlXHgfqV1WrQo6TV356HiEAs86A"
    wget(URL)
    if wget:
        print(f'[+] Downloaded .xls to {os.getcwd()}')
    src = os.getcwd()
    dst = "Balance Sheet and Income Statement.xls"
    os.rename(src, dst)
    if os.rename:
        print(f'[+] file [{dst}] saved in \n\t[{src}]')
except Exception as e:
    print(e)

try:
    excel2json.convert_from_file("Balance Sheet and Income Statement.xls")
    if excel2json:
        print(f'Wrote excel to json, file saved in {os.getcwd()}')
except Exception as e:
    print(e)

'''Read Excel to Pandas DF-- export to JSON since its small amount of data '''
print(f'Creating Pandas Dataframe for seperate .xls sheets')
df_balanceSheet = pandas.read_excel('Balance Sheet and Income Statement.xls', sheet_name='Balance Sheet')
df_incomeStatement = pandas.read_excel('Balance Sheet and Income Statement.xls', sheet_name='Income Statement')
bal_str = df_balanceSheet.to_json()
incom_str = df_incomeStatement.to_json()
print('Excel Sheet to JSON:\n', bal_str)
print('Excel Sheet to JSON:\n', incom_str)


'''Clean UP Pandas DF'''
df_balanceSheet.dropna(axis=0)  # , how='any', thresh=None, subset=None, inplace=False)
df_balanceSheet.dropna(axis=1)  # , how='any', thresh=None, subset=None, inplace=False)
df_incomeStatement.dropna(axis=0)  # , how='any', thresh=None, subset=None, inplace=False)
df_incomeStatement.dropna(axis=1)  # , how='any', thresh=None, subset=None, inplace=False)

'''Export To JSON'''
balnce_json = df_balanceSheet.to_json(orient="split")
income_json = df_incomeStatement.to_json(orient="split")
parsed_bal = json.loads(balnce_json)
parsed_inc = json.loads(income_json)
json.dumps(parsed_bal, indent=4)
json.dumps(parsed_inc, indent=4)


''' Print Data after master cleanup'''
print('ALL DATA AFTER CLEANING')
print(bal_str)
print(type(bal_str))
print(incom_str)
print(type(incom_str))
print(df_balanceSheet.head(20))
print(type(df_balanceSheet))
print(df_incomeStatement.head(20))
print(type(df_incomeStatement))
print(balnce_json)
print(income_json)


''' 
    *.keys to explore jsons. each excel page has a corrospondig json object to work with.
    *since the dataset is small i am going to use a json object, rather than pandas DF.
    * however, pandas was used to clean up the master dataset, mainly to remove NaN values, and shift cooropsponding indexes
'''
try:
    print(parsed_bal.keys())
    print(parsed_inc.keys())
    ''' use these for data parsing '''
    print(parsed_inc['data'])
    print(parsed_bal['data'])
    print('X' * 50)

    cash_securites = parsed_bal['data'][2]
    print(cash_securites)
    print(type(cash_securites))
    print(f'cash and liabalities {cash_securites[2]}{cash_securites[4]}')

    print(f'{yellow}[QUESTION 1] \n 1. Compute  the  current  ratio  &  quick  ratio  and  determine  if  the  firm’s  liquidity  has increased or decreased? {reset}')
    print(f' Current Ratio = (CURRENT_ASSETS) / (CURRENT_LIABILITIES) ')

    total_currentAssets = parsed_bal['data'][5]
    print('Total Current asset year-year', total_currentAssets)
    print('2019', total_currentAssets[2])
    print('2020', total_currentAssets[4])

    total_currentAssets2019 = total_currentAssets[2]
    total_currentAssets2020 = total_currentAssets[4]

    total_currentLiabilities = parsed_bal['data'][15]
    print('Total Current Liability year-year', total_currentLiabilities)
    print('2019', total_currentLiabilities[2])
    print('2020', total_currentLiabilities[4])

    '''Clean data up '''
    currentLiability2019 = total_currentLiabilities[2]
    currentLiability2020 = total_currentLiabilities[4]
    currentLiability2019 = currentLiability2019[1:]
    currentLiability2020 = currentLiability2020[1:]
    total_currentAssets2019=total_currentAssets2019[1:]
    total_currentAssets2020 = total_currentAssets2020[1:]
    print(type(total_currentAssets2019))
    total_currentAssets2019 = float(total_currentAssets2019)
    currentLiability2019 = float(currentLiability2019)
    total_currentAssets2020 = float(total_currentAssets2020)
    currentLiability2020 = float(currentLiability2020)
    total_currentAssets2019 = float(total_currentAssets2019)
    currentLiability2019 = float(currentLiability2019)
    total_currentAssets2020 = float(total_currentAssets2020)
    currentLiability2020 = float(currentLiability2020)
    '''End data cleanup'''

    '''Start ratio calculation'''
    liquidity_2019 = (total_currentAssets2019 / currentLiability2019)
    liquidity_2020 = (total_currentAssets2020 / currentLiability2020)
    print(f'{bblue}2019 Current Ratio: {liquidity_2019}')
    print(f'2019 Current Ratio: {liquidity_2020}{reset}')
    if liquidity_2019 > liquidity_2020:
        print('[+] The liquidity was larger in 2019 indicating a decrease, YOY')
    elif liquidity_2019 < liquidity_2020:
        print('[+] 2019\'s liquidiyt was less, indicateing an increase in liqudity, YOY')

    print('What are some implications for this result?')

except Exception as e:
    print(e, traceback.print_exc())



print('X'*50)
print(f'{yellow}Compute the debt ratio and determine if the firm has increased or decreased leverage?')
print(f'(Debt/Equity)=Total Shareholders’ Equity{reset}')

try:

    '''Gather Data & print values'''
    total_debt = parsed_bal['data'][21]
    total_equity = parsed_bal['data'][9]
    total_debt2019=total_debt[2]
    total_debt2020=total_debt[4]
    total_equity2019=total_equity[2]
    total_equity2020=total_equity[4]

    print('Total Debt: [LIST] \n', total_debt)
    print('Total Debt: [2019] \n', total_debt2019)
    print('Total Debt: [2020] \n', total_debt2020)

    print('Total Equity: [LIST] \n', total_equity)
    print('Total Equity: [2019] \n', total_equity2019)
    print('Total Euity: [2020] \n', total_equity2020)



    try:
        '''Clean data up '''
        print('DATA CLEANUP')
        total_equity2019 = total_equity2019[1:]
        total_equity2020 = total_equity2020[1:]
        total_debt2020 = total_debt2020[1:]
        total_debt2019 = total_debt2019[1:]
        total_debt2019 = float(total_debt2019)
        total_debt2020 = float(total_debt2020)
        total_equity2019 = float(total_equity2019)
        total_equity2020 = float(total_equity2020)
        print('end of data cleanup..')
    except Exception:
        print('Exception in cleanup, passing')
        pass
    '''End data cleanup'''

    '''Calculate and display'''
    debtRatio2019= total_debt2019/total_equity2019
    debtRatio2020= total_debt2020/total_equity2020
    print(' (Debt/Equity)=Total Shareholders’ Equity')
    print(f'[+] [2019 Debt Ratio]: \n {debtRatio2019}')
    print(f'[+] [2020 Debt Ratio]: \n {debtRatio2020}')

    if debtRatio2019 == debtRatio2020:
        print(f'[+] 2019\s debt ratio is [{debtRatio2019}] and 2020\'s debt ratio is [{debtRatio2020}]\n This indicates they are even, YOY.' )


except Exception as e:
    print(e, traceback.print_exc())


## parsed_inc['data']
print(f"{yellow}Compute the firm’s times-interest earned & cash coverage ratio?\n The times interest earned (TIE) ratio is a measure of a company's ability "
      "to meet its debt obligations based on its current income.")
print(f'(EBIT) / (total interest payable on bonds and other debt){reset}')

'''list ebt '''
ebit_list=parsed_inc['data'][7]
ebt_2019=ebit_list[2]
ebt_2020=ebit_list[4]

'''list interest'''
interest_list=parsed_inc['data'][8]
interest_2019=interest_list[2]
interest_2020=interest_list[4]

''' Clean UP '''
ebt_2019=ebt_2019[1:]
ebt_2020=ebt_2020[1:]
interest_2019 = interest_2019[1:]
interest_2020 = interest_2020[1:]
ebt_2019 = float(ebt_2019)
ebt_2020= float(ebt_2020)
interest_list2019 = interest_2019[1:]
print(interest_2019)
interest_2019 = str(interest_2019[1:-1])
interest_2020 = str(interest_2020[1:-1])
interest_2019 = float(interest_2019)
interest_2020 = float(interest_2020)
interest_2020 = -abs(interest_2020)
interest_2019 = -abs(interest_2019)

'''calculations for time-iterest earned'''
tie2019 = ebt_2019 / interest_2019
tie2020 = ebt_2020 / interest_2020

print('X'*50)
print('EBIT- [LIST]', ebit_list)
print('EBIT- [2019]', ebt_2019)
print('EBIT- [2020]', ebt_2020)
print('X'*50)
print('interest- [LIST]', interest_list)
print('interest- [2019]', interest_2019)
print('interest- [2020]', interest_2020)
print('X'*50)
print(f'{bblue}')
print('TIE- [2019]', tie2019)
print('TIE- [2020]', tie2020)
print(f'{reset}')


print('X' * 50)
print(f'{yellow}Compute the firm’s times-interest earned & cash coverage ratio?')
print(f'For companies that have interest expenses that need to be paid, the cash coverage ratio is used to determine whether the company has sufficient income to cover them.')
print(f'Current Assets / Interest payments. {reset}')

current_assets = parsed_bal['data'][5]
cash_2019 = current_assets[2]
cash_2020 = current_assets[4]

'''cleanup data '''
cash_2019 = cash_2019[1:]
cash_2020 = cash_2020[1:]
cash_2019 = float(cash_2019)
cash_2020 = float(cash_2020)


''' Calculations '''
CCR2019 = (cash_2019 / interest_2019) * .1
CCR2020 = (cash_2020 / interest_2020) * .1

'''Display Results'''
print('\n', 'X' *50)
print('Current Assets - Cash on Hand [LIST]\n', current_assets)
print('Current Assets - [2019]', cash_2019)
print('Current Assets - [2020]', cash_2020)
print('Interest- [LIST]', interest_list)
print('Interest- [2019]', interest_2019)
print('Interest- [2020]', interest_2020)
print(f'{bblue}')
print('[Cash Coverage Ratio] ')
print('CCR- [2019]', CCR2019)
print('CCR- [2020]', CCR2020)
print(f'{reset}')
print(f'{yellow}')
print('Compute the following ratios \n\t\t i) profit margin \n\t\tii) return on assets \n\t\tiii) return on equity')
print('Profit Margin = (Total Revenue / Total Expenses)')
print(f'{reset}')
print('\n', 'X' *50)


''' Get Data '''
revenues = parsed_inc['data'][2]
revenues_2019 = revenues[2]
revenues_2020 = revenues[4]

expenses = parsed_inc['data'][5]
expenses_2019 = expenses[2]
expenses_2020 = expenses[4]


''' Clean Up Data '''
revenues_2019 = revenues_2019[1:]
revenues_2020 = revenues_2020[1:]

# COMMA SEPERATION
reva = revenues_2020[0]
revb = revenues_2020[-5:]
revenues_2020 = reva + revb
revaa = revenues_2019[0]
revbb = revenues_2019[-5:]
revenues_2019 = revaa + revbb

print(revenues_2020)
print(revenues_2019)
revenues_2020 = float(revenues_2020)
revenues_2019 = float(revenues_2019)

print(expenses_2019)
expenses_2019 = str(expenses_2019[1:-1])
expenses_2020 = str(expenses_2020[1:-1])
expenses_2019 = str(expenses_2019[1:])
expenses_2020 = str(expenses_2020[1:])

print('X' * 50)
print(expenses_2019)
print(expenses_2020)


expenses_2019 = float(expenses_2019)
expenses_2020 = float(expenses_2020)
expenses_2019 = -abs(expenses_2019)
expenses_2020 = -abs(expenses_2020)

''' calculation '''
profit_margin2019 = (revenues_2019 / expenses_2019) *  .1
profit_margin2020 = (revenues_2020 / expenses_2020) * .1

'''display results'''
print('\n', 'X' *50)
print('Net Sales -  [LIST]\n', revenues)
print(' Revenues - [2019]', revenues_2019)
print(' Revenues - [2020]', revenues_2020)
print('EXPENSES -  [LIST]\n', expenses)
print('EXPENSES - [2019]', expenses_2019)
print('EXPENSES - [2020]', expenses_2020)
print(f'{bblue}')
print('PROFIT-MARGIN - [2019]', profit_margin2019)
print('PROFIT-MARGIN - [2020]', profit_margin2020)
print(f'{reset}')
print('\n', 'X' *50)


print(' START OF RETURN ON ASSETS (ROA)')
print('\n return on asssets =  net income \ total average assets. \n\t\t Average total assets = (total assets for current year) + (total assets for previous year) / 2')


''' Get Data'''
net_income = parsed_inc['data'][11]
net_income2019 = net_income[2]
net_income2020 = net_income[4]
total_assets = parsed_bal['data'][9]
total_assets2019 = total_assets[2]
total_assets2020 = total_assets[4]

''' clean up data '''
net_income2019 = net_income2019[1:]
net_income2020 = net_income2020[1:]
total_assets2019 = total_assets2019[1:]
total_assets2020 = total_assets2020[1:]

''' convert data'''
net_income2019 = float(net_income2019)
net_income2020 = float(net_income2020)
total_assets2020 = float(total_assets2020)
total_assets2019 = float(total_assets2019)


''' CALCULATION '''
avg_assets = (total_assets2020 + total_assets2019) / 2
ROA2020 = net_income2020 / avg_assets
print('\n', 'X' *50)
'''display results'''
print('Net income -  [LIST]\n', net_income)
print('net_income - [2019]', net_income2019)
print('net_income - [2020]', net_income2020)
print('TOTAL ASSETS -  [LIST]\n', total_assets)
print('TOTAL ASSETS - [2019]', total_assets2019)
print('TOTAL ASSETS - [2020]', total_assets2020)
print(f'{bblue}')
print("avg_assets = (total_assets2020 + total_assets2019) / 2")
print('AVERAGE ASSETS [2019 -2020]', avg_assets)
print('return on asssets =  net income \ total average assets')
print('ROA  [2019 -2020]', ROA2020)
print(f'{reset}')

print('\n', 'X' *50)
print(' START OF RETURN ON EQUITY (ROE)')

'''get data'''
total_liability = parsed_bal['data'][17]
total_asset = parsed_bal['data'][9]
total_liability2019 = total_liability[2]
total_liability2020 = total_liability[4]
total_asset2019=total_asset[2]
total_asset2020=total_asset[4]


'''clean data'''
total_liability2020=total_liability2020[1:]
total_liability2019=total_liability2019[1:]
total_asset2020=total_asset2020[1:]
total_asset2019=total_asset2019[1:]

''' convert data '''
total_liability2019=float(total_liability2019)
total_liability2020=float(total_liability2020)
total_asset2019=float(total_asset2019)
total_asset2020=float(total_asset2020)

''' calculation '''
shareholder_equity2020 = total_liability2020 - total_asset2020
shareholder_equity2019 = total_liability2019 - total_asset2019
ROE2019 =  float(net_income2019) / float(shareholder_equity2019)
ROE2020 =  float(net_income2020) / float(shareholder_equity2020)


'''display results'''
print('\n', 'X' *50)
print('total_asset -  [LIST]\n', total_asset)
print('total_asset -  [2019]\n', total_asset2019)
print('total_asset -  [2020]\n', total_asset2020)

print('total_liablity -  [LIST]\n', total_liability)
print('total_liablity - [2019]', total_liability2019)
print('total_liablity - [2020]', total_liability2020)
print(f'{bblue}')
print('\n Return on Equity = Net Income / Shareholder Equity.s. \n\t\t SHAREHOLDER EQUITY = TOTAL LIABILITY - TOTAL ASSET')
print('SHAREHOLDER EQUITY [2019]', shareholder_equity2019)
print('SHAREHOLDER EQUITY [2020]', shareholder_equity2020)
print('RETURN ON EQUITY [2019]', ROE2019)
print('RETURN ON EQUITY [2020]', ROE2020)
print(f'{reset}')

print('\n', 'X' *50)



