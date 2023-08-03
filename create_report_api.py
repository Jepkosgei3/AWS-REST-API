import boto3, json

client = boto3.client('apigateway', region_name='us-east-1')

api_id = 'nh5rqqbhq4'

resources = client.get_resources(restApiId=api_id)
root_id = [resource for resource in resources["items"] if resource["path"] == "/"][0]["id"]



report_resource = client.create_resource(
    restApiId=api_id,
    parentId=root_id,
    pathPart='create_report'
)
report_resource_id = report_resource["id"]



report_method = client.put_method(
    restApiId=api_id,
    resourceId=report_resource_id,
    httpMethod='POST',
    authorizationType='NONE'
)

report_response = client.put_method_response(
    restApiId=api_id,
    resourceId=report_resource_id,
    httpMethod='POST',
    statusCode='200',
    responseParameters={
        'method.response.header.Access-Control-Allow-Headers': False,
        'method.response.header.Access-Control-Allow-Origin': False,
        'method.response.header.Access-Control-Allow-Methods': False
    },
    responseModels={
        'application/json': 'Empty'
    }
)


report_integration = client.put_integration(
    restApiId=api_id,
    resourceId=report_resource_id,
    httpMethod='POST',
    type='MOCK',
    requestTemplates={
        'application/json': '{"statusCode": 200}'
    }
)


report_integration_response = client.put_integration_response(
    restApiId=api_id,
    resourceId=report_resource_id,
    httpMethod='POST',
    statusCode='200',
    responseParameters={
        'method.response.header.Access-Control-Allow-Headers': '\'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token\'',
        'method.response.header.Access-Control-Allow-Methods': '\'POST\'',
        'method.response.header.Access-Control-Allow-Origin': '\'*\''
    },
    # ithink they have an issue with real JSON here
    responseTemplates={
        "application/json": json.dumps({
            "msg_str": "report requested, check your phone shortly"
        })
    }
)


print ("DONE")
###code to create to generate inventory of the ProductsApi
###next is deployment