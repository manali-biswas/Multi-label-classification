from urllib.error import HTTPError
import requests
import re

class luis2: 
   
    def predict_proba(self,queries) :
        res=[]
        for x in queries:
            arr=[]
            try:
                query = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", x).split())
                #query = remove_stop(query)
                if len(query)>500:
                    response = requests.get('https://meetingintent.cognitiveservices.azure.com/luis/prediction/v3.0/apps/555b30db-d2b3-4029-bd60-3b7f3af8638d/slots/production/predict?subscription-key=061b62549df24c629ebfdae74992c428&verbose=true&show-all-intents=true&log=true&query='+query[:500])
                else:
                    response = requests.get('https://meetingintent.cognitiveservices.azure.com/luis/prediction/v3.0/apps/555b30db-d2b3-4029-bd60-3b7f3af8638d/slots/production/predict?subscription-key=061b62549df24c629ebfdae74992c428&verbose=true&show-all-intents=true&log=true&query='+query)
                response.raise_for_status()
                # access JSOn content
                jsonResponse = response.json()
                y=jsonResponse
                arr.append(y['prediction']['intents']['Meeting']['score'])
                arr.append(y['prediction']['intents']['urgent']['score'])
                arr.append(y['prediction']['intents']['None']['score'])
                res.append(arr)        


            except HTTPError as http_err:
                print(f'HTTP error occurred: {http_err}')

            except Exception as err:
                print(f'Other error occurred: {err}')            

        
        return res