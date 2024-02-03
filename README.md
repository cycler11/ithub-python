Project Description

The project is a Python package designed to analyze firewall rules stored in a CSV file and extract specific information from these rules.

Project Contents

1. FW_rule.py: Module containing the definition of the FWRule class representing a firewall rule.
2. FW_rule_selector.py: Module containing the FWRuleSelector class for selecting and analyzing firewall rules.
3. read_csv.py: Module responsible for reading rules from a CSV file and converting them into FWRule objects.
4. save_to_csv.py: Module containing the save_to_csv function that saves the selection results to CSV files.
5. main.py: Main project file where rules analysis and result saving are performed.

Additional Notes

Please ensure that your CSV files with firewall rules have the correct format and encoding (Win 1251) for proper reading and writing.
Refer to the documentation of each module to learn more about available methods and functions.