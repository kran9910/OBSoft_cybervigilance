#Main class that prompts the user to enter the search word, call the store class method that connects
#to the API and print all the attributes of the first result in the response in the first place,
#then prints the attributes of all the objects fetched
from ScanResultStoreClass import *

query = input("Enter the search word 'regex test demo fake profile' without quotation marks: ")
#query = "regex test demo fake profile"
MainScanResultStore = ScanResultStore()
List = MainScanResultStore.scan_results_data(query)

FirstScanResult = List[0]
print("\nPrinting attributes of the First Object Fetched:")
print("Source: " + str(FirstScanResult.source))
print("Ranking: " + str(FirstScanResult.ranking))
print("Engine: " + str(FirstScanResult.engine))
print("Category: " + str(FirstScanResult.category))
print("Feedback: " + str(FirstScanResult.feedback))

print("\nPrinting attributes of all the objects fetched")
for scanResult in List:
    print("\nObject Fetched:")
    print("Source: " + str(scanResult.source))
    print("Ranking: " + str(scanResult.ranking))
    print("Engine: " + str(scanResult.engine))
    print("Category: " + str(scanResult.category))
    print("Feedback: " + str(scanResult.feedback))

#input("Press Enter to exit...")