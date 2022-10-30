from gpustealer import Booking

#rom booking.booking import Booking

# inst = Booking()
# inst.land_first_page()

with BestBuyripper() as rip:
    rip.install_plugins()
    rip.first_page()


    rip.select_link('val')
    rip.take_screenshots()
    rip.searchbox('computer parts')

    rip.select_link('val')
    rip.take_screenshots()

    print('Exiting..')

