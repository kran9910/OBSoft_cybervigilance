# OBSoft_cybervigilance
ScanResult.py: Class for the ScanResult objects.

ScanResultStoreClass.py: Implements the ScanResultStore class which is responsible for calling the API which takes a search term (query) and returns its related scan results. The class method scan_results_data(query) returns the parsed response as a list of ScanResults. This class needs the WSSE authentication string which is loaded from a local file once the program is started and will be used as a header for the requests.

main.py: Main class that prompts the user to enter the search word, call the store class method that connects to the API and print all the attributes of the first result in the response in the first place, then prints the attributes of all the objects fetched
