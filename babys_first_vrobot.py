import splinter

first_vrobot = splinter.Browser('chrome')

first_vrobot.visit('google.ca')


first_vrobot.screenshot()