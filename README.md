```python
import cpm.cpm as cpm

brrr_system = cpm.CPM()
# Input
brrr_system.load_data_from_user()
# Brrrr
brrr_system.solve()
# Output
brrr_system.print_result_network()
# brrr_system.show_result_network()
```
# Docs
-- [cpm](cpm) - main CPM folder </br>
&emsp; &nbsp; |-- [cpm](cpm/cpm) - contains main class, don't change declarations, just fill bodies (may use other files / classes / anything)</br>
&emsp; &nbsp; |-- [network](cpm/network) - contains data structures: Network, Node</br>
&emsp; &nbsp; |-- [test_data](cpm/test_data) - place for test data sets</br>
&emsp; &nbsp; |-- [test](cpm/test) - run using pytest</br>
-- [data_input](data_input.py) - shitty test data reader (used in cpm/test)</br>