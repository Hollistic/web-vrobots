import splinter

first_vrobot = splinter.Browser('chrome')

first_vrobot.visit('https://google.ca')


first_vrobot.screenshot('test', '.png', True, False)

first_vrobot.quit()