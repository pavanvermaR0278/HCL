try:
    import csv
    from builtins import type
    import pymongo
    import requests

except Exception as e:
    print("Some Modules are Missing ")


class MongoDB(object):

    def __init__(self, dBName=None, collectionName=None):

        self.dBName = dBName
        self.collectionName = collectionName
        self.myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        self.mydb = self.myclient[self.dBName]
        self.mycol = self.mydb[self.collectionName]




    def DownloaData(self, CSV_URL=None):
        with requests.Session() as s:
            download = s.get(CSV_URL)

            decoded_content = download.content.decode('utf-8')

            cr = csv.reader(decoded_content.splitlines(), delimiter=',')
            #list1=list(cr)
        return cr




    def InsertData(self,data=None):
        csv_list = list(data)

        temp_list = list()

        for i in range(1, len(csv_list)):
             var = {"_id": csv_list[i][3], "Result Time": csv_list[i][0], "Granularity Period": csv_list[i][1], "Object Name": csv_list[i][2], "CallAttemps": csv_list[i][3]}
             temp_list.append(var)
             temp_list.append(var)

        x = self.mycol.insert_many(temp_list)
        print(x.inserted_ids)



if __name__ == "__main__":
    CSV_URL = 'http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv'
    mongodb = MongoDB(dBName = 'RealState', collectionName='Property3')
    data=mongodb.DownloaData(CSV_URL)
    mongodb.InsertData(data)