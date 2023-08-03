import boto3, json

client = boto3.client('apigateway', region_name='us-east-1')


api_id = 'nh5rqqbhq4'
parent_id = 'ya3mgo'

products = client.create_resource(
    restApiId=api_id,
    parentId=parent_id,
    pathPart='on_offer'
)
products_resource_id = products["id"]


product_method = client.put_method(
    restApiId=api_id,
    resourceId=products_resource_id,
    httpMethod='GET',
    authorizationType='NONE'
)

product_response = client.put_method_response(
    restApiId=api_id,
    resourceId=products_resource_id,
    httpMethod='GET',
    statusCode='200',
    responseParameters={
        'method.response.header.Access-Control-Allow-Headers': True,
        'method.response.header.Access-Control-Allow-Origin': True,
        'method.response.header.Access-Control-Allow-Methods': True
    },
    responseModels={
        'application/json': 'Empty'
    }
)

product_integration = client.put_integration(
    restApiId=api_id,
    resourceId=products_resource_id,
    httpMethod='GET',
    type='MOCK',
    requestTemplates={
        'application/json': '{"statusCode": 200}'
    }
)


product_integration_response = client.put_integration_response(
    restApiId=api_id,
    resourceId=products_resource_id,
    httpMethod='GET',
    statusCode='200',
    responseTemplates={
        "application/json": json.dumps({
            "product_item_arr": [{
                "product_name_str": "apple pie slice",
                "product_id_str": "a444",
                "price_in_cents_int": 595,
                "description_str": "amazing taste",
                "tag_str_arr": [
                  "pie slice",
                  "on offer"
                ],
                "special_int": 1
              }]
        })
    },
    responseParameters={
        'method.response.header.Access-Control-Allow-Headers': "'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'",
        'method.response.header.Access-Control-Allow-Methods': "'GET'",
        'method.response.header.Access-Control-Allow-Origin': "'*'"
    }
)


print ("DONE")
###this adds resource to product api previously created, parent id and api id are from ProductsApi