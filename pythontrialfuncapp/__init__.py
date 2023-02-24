import logging
import json
import public_ip as ip

import azure.functions as func
from azure.storage.filedatalake import DataLakeServiceClient


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        data = {
            "name": name
    }
        # with open("datafile.json", "w") as write_file:
            # json.dump(data, write_file, indent = 1)

        # service_client = DataLakeServiceClient(account_url="{}://{}.dfs.core.windows.net".format("https", "pythondatalakestorage"), credential="TUqyfiyqzrCVHJw8yJubcDDrC41WuGYqynOxADr3hzsIwE4Ebsl1ItiFVlLHV2VTs+a6fK5LmbkR+AStMacpAw==")
        # mycontainer = service_client.get_file_system_client("demo")
        # mycontainer.create_directory("jsondirectory")
        # file_system_client = service_client.get_file_system_client(file_system="demo")
        # directory_client = file_system_client.get_directory_client("jsondirectoryv2")
        # file_client = directory_client.create_file("uploadedjsonfile.json")
        # local_file = open("datafile.json", "r")

        # filedata = json.dumps(data)
        # file_client.append_data(data=filedata, offset=0, length=len(filedata))
        # file_client.flush_data(len(filedata))

        # return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")

        publicIP = ip.get()
        return func.HttpResponse(f"Hello, {name}. your public IPAddress is {publicIP} & This HTTP triggered function executed successfully.")

        
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
