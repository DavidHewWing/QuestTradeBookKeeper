from . import qt_controller
from . import gscontroller


def run(account):
    # questtrade data
    account_name = account['qt_account_number']
    account_info = qt_controller.get_user_account(account_name)
    positions, total = qt_controller.get_positions(account_name, simple=True)
    balance = qt_controller.get_balances(account_name)

    # googlesheets data
    spreadsheet_id = account['spreadsheet_id']

    # update the overall data spreadsheet
    header_values = gscontroller.get_header_values(total, positions, balance)
    values = [header_values['Date'], account['cash_invested'], header_values['Uninvested'], header_values['Buy-In Price'], header_values['Market Value'], header_values['Increase']]
    gscontroller.append_row(spreadsheet_id, values)



