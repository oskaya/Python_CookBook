import boto3, json
from configparser import ConfigParser
from botocore.exceptions import ClientError

#=======================================================================
#Cretae a parser to read configuration file
config  = ConfigParser()
config.read("config.ini")

#Get configuration values for AWS Account from "account_config" file in same directory
AWS_ACCESS_KEY_ID = config["account_config"].get("aws_access_key_id")
AWS_SECRET_KEY_ID = config["account_config"].get("aws_secret_access_key")
REGION = config["account_config"].get("region")
COLLECTION_ID = config["account_config"].get("collection_id")


#========================================================================
#Put here name of the pohoto you want to find emotions on
#Take care to path of the file
PHOTO = 'familiy.jpg'
#========================================================================
#Function definitions

def detect_faces(target_file, region):

    client=boto3.client('rekognition', region_name=region, aws_access_key_id=AWS_ACCESS_KEY_ID,
                                                           aws_secret_access_key=AWS_SECRET_KEY_ID)

    imageTarget = open(target_file, 'rb')

    response = client.detect_faces(Image={'Bytes': imageTarget.read()}, 
    Attributes=['ALL'])

    print(f"{len(response['FaceDetails'])} faces detected in  {PHOTO}")
    count = 1
    for faceDetail in response['FaceDetails']:
        print("========================================")
        print(f"Info for {count}. face is below")
        print('The detected face is between ' + str(faceDetail['AgeRange']['Low'])
              + ' and ' + str(faceDetail['AgeRange']['High']) + ' years old')

        #print('Here are the other attributes:')
        #print(json.dumps(faceDetail, indent=4, sort_keys=True))

        # Access predictions for individual face details and print them
        print("Gender: " + str(faceDetail['Gender']))
        print("Smile: " + str(faceDetail['Smile']))
        print("Eyeglasses: " + str(faceDetail['Eyeglasses']))
        print("Emotions: " + str(faceDetail['Emotions'][0]))
        print("\n")
        print("========================================")
        count += 1
    return 

def create_collection(collection_id, region):
    client = boto3.client('rekognition', region_name=region, aws_access_key_id=AWS_ACCESS_KEY_ID,
                                                             aws_secret_access_key=AWS_SECRET_KEY_ID)

    # Create a collection
    print('Creating collection:' + collection_id)
    response = client.create_collection(CollectionId=collection_id, 
    Tags={"SampleKey1":"SampleValue1"})
    print('Collection ARN: ' + response['CollectionArn'])
    print('Status code: ' + str(response['StatusCode']))
    print('Done...')
    return response
        
    
def delete_collection(collection_id):
    client = boto3.client('rekognition', aws_access_key_id=AWS_ACCESS_KEY_ID,
                                         aws_secret_access_key=AWS_SECRET_KEY_ID)
    
    print("\n")
    print("========================================")
    print('Attempting to delete collection ' + collection_id)
    
    status_code=0
    try:
        response=client.delete_collection(CollectionId=collection_id)
        status_code=response['StatusCode']
        
    except ClientError as e:
        if e.response['Error']['Code'] == 'ResourceNotFoundException':
            print ('The collection ' + collection_id + ' was not found ')
        else:
            print ('Error other than Not Found occurred: ' + e.response['Error']['Message'])
        status_code=e.response['ResponseMetadata']['HTTPStatusCode']
    else:
        print(collection_id, " deleted")
    return print(f"status code :{status_code}")


try:
    create_collection(COLLECTION_ID, REGION)
except :
    pass
else:
    detect_faces(PHOTO, REGION)
    
finally:

    delete_collection(COLLECTION_ID)
    

