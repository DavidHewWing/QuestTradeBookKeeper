import qt_controller
import gscontroller


def run():
    # questtrade data
    account = qt_controller.get_user_account()
    positions, total = qt_controller.get_positions(account, simple=True)
    balance = qt_controller.get_balances(account)

    # googlesheets data
    uninvested_cash = get_uninvested_from_txt()
    spreadsheet_id = gscontroller.get_spreadsheet_id()

    # update the overall data spreadsheet
    header_values = gscontroller.get_header_values(total, positions, balance)
    values = [header_values['Date'], float(uninvested_cash), header_values['Uninvested'], header_values['Buy-In Price'], header_values['Market Value'], header_values['Increase']]
    gscontroller.append_row(spreadsheet_id, values)


def get_uninvested_from_txt():
    cash_file = open('./src/tokens/cash_invested.txt', 'r')
    cash = cash_file.readline()
    return cash

