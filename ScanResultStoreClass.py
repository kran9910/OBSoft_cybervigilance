#ScanResultStore class which is responsible for calling the API which takes a search term and returns its related scan results.
#The class method scan_results_data(query) returns the parsed response as a list of ScanResults.
import requests
from requests import HTTPError
from ScanResult import ScanResult

# Requests variables
server_url = "http://192.168.5.218/cybervigilance/web/"
WsseStringfile = open("C:/Users/MB/Desktop/OBSoft/WsseUserToken.txt","r")
wsse = (WsseStringfile.read(228)) #The WSSE authentication string which is loaded from a local file once the program is started
WsseStringfile.close()

class ScanResultStore:
    def __init__(self):
        self.server_url = server_url
        self.wsse = wsse

    # api getter
    def get_scan_results(self,query):
        url = self.server_url + "api/private/scan/results?query="+ query
        try:
            response = requests.get(
                url=str(url),
                headers={"x-wsse": self.wsse}
            )
            # If the response was successful, no Exception will be raised
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')
        else:
            response_json = response.json()
            return response_json

    # Returns a list of ScanResult objects corresponding to the data fetched from the API
    def scan_results_data(self,query):
        List = []
        for data in self.get_scan_results(query= query)['data']:
            scanResult = ScanResult(
                source=data.get('source'),
                ranking=data.get('ranking'),
                engine=data.get('engine'),
                category=data.get('category'),
                feedback=data.get('feedback'),
            )
            List.append(scanResult)
        return List
