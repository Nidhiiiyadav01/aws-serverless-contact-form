import json

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        
        name = body.get('name')
        email = body.get('email')
        message = body.get('message')

        print(f"New message from {name} ({email}): {message}")

        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'message': 'Form submitted successfully!'
            })
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
