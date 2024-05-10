from tabulate import tabulate
import asyncio
from pyfiglet import figlet_format
import main_functions, menu_configs
print(figlet_format("aminoinfoclique", font="chunky", width=58))
print(tabulate(menu_configs.main_menu, tablefmt="github"))
select = int(input("-- Select::: "))
if select == 1:asyncio.get_event_loop().run_until_complete(main_functions.get_global_user_info())
elif select == 2:asyncio.get_event_loop().run_until_complete(main_functions.get_chat_info())
elif select == 3:asyncio.get_event_loop().run_until_complete(main_functions.get_account_info())