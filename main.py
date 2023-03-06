import cpm.cpm as cpm


brrr_system = cpm.CPM()
# Input
brrr_system.load_data_from_file()
# brrr_system.load_data_from_user()
# Brrrr
brrr_system.solve()
# Output
brrr_system.print_result_network()
# brrr_system.show_result_network()
