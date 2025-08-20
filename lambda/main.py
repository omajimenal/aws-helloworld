def lambda_handler(event, context):
    try:
        return {
            "statusCode": 200,
            "body": "hola mundo OmarJ, Test case 1",
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": f"Error: {str(e)}"
        }
