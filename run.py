from booking import Booking

#rom booking.booking import Booking

# inst = Booking()
# inst.land_first_page()

with Booking() as bot:
    bot.install_plugins()

    bot.first_page()
    bot.select_link('val')
    bot.take_screenshots()
    bot.searchbox('computer parts')

    bot.select_link('val')
    bot.take_screenshots()

    print('Exiting..')

