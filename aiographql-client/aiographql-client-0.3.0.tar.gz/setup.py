# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['aiographql', 'aiographql.client']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.5,<4.0',
 'cafeteria-asyncio>=0.1.0,<0.2.0',
 'graphql-core-next>=1.1,<2.0']

setup_kwargs = {
    'name': 'aiographql-client',
    'version': '0.3.0',
    'description': 'An asyncio GraphQL client built on top of aiohttp and graphql-core-next',
    'long_description': '# Asyncio GraphQL Client\nAn asyncio GraphQL client built on top of aiohttp and graphql-core-next. The client by default introspects schemas and validates all queries prior to dispatching to the server.\n\n## Installation\n`pip install aiographql-client`\n\n## Example Usage\nHere are some example usages of this client implementation. These examples use the [Hasura GraphQL Engine](https://hasura.io/).\n\n### Simple Query\n```py\nasync def get_bots():\n    client = GraphQLClient(\n        endpoint="http://localhost:8080/v1alpha1/graphql",\n        headers={"x-hasura-admin-secret": "myadminsecretkey"},\n    )\n    request = GraphQLRequest(\n        query="""\n        query get_bots {\n          chatbot {\n            id, bot_name\n          }\n        }\n        """\n    )\n    transaction = await client.post(request)\n\n    # display the query used\n    print(transaction.request.query)\n\n    # dump the response data\n    print(transaction.response.data)\n```\n\n### Query Subscription\n```py\nasync def get_bots():\n    client = GraphQLClient(\n        endpoint="http://localhost:8080/v1alpha1/graphql",\n        headers={"x-hasura-admin-secret": "myadminsecretkey"},\n    )\n    request = GraphQLRequest(\n        query="""\n        subscription get_bot_updates {\n          chatbot {\n            id, bot_name\n          }\n        }\n        """\n    )\n    \n    # configure callbacks, here we simply print the event message when a data event\n    # (`GraphQLSubscriptionEvent`) is received.\n    callbacks = CallbackRegistry()\n    callbacks.register(\n        GraphQLSubscriptionEventType.DATA, lambda event: print(event.message)\n    )\n    \n    subscription: GraphQLSubscription = await client.subscribe(request, callbacks)\n    await subscription.task\n```\n\n### Query Validation Failures\nIf your query is invalid, thanks to graphql-core-next, we get a detailed exception in the traceback.\n\n```\naiographql.client.exceptions.GraphQLClientValidationException: Query validation failed\n\nCannot query field \'ids\' on type \'chatbot\'. Did you mean \'id\'?\n\nGraphQL request (4:13)\n3:           chatbot {\n4:             ids, bot_names\n               ^\n5:           }\n\nCannot query field \'bot_names\' on type \'chatbot\'. Did you mean \'bot_name\' or \'bot_language\'?\n\nGraphQL request (4:18)\n3:           chatbot {\n4:             ids, bot_names\n                    ^\n5:           }\n\n```\n\n### Sample Requests\n#### Using `variables` and `operationName`\n```py\nGraphQLRequest(\n    query="""\n    query get_bot_created($id: Int) {\n      chatbot(where: {id: {_eq: $id}}) {\n        id, created\n      }\n    }\n    query get_bot_name($id: Int) {\n      chatbot(where: {id: {_eq: $id}}) {\n        id, bot_name\n      }\n    }\n    """,\n    variables={\'id\': \'109\'},\n    operationName=\'get_bot_name\'\n)\n```\n',
    'author': 'Twyla Engineering',
    'author_email': 'software@twyla.ai',
    'url': 'https://github.com/twyla-ai/aiographql-client',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
