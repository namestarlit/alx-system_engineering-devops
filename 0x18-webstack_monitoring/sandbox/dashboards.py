"""
Get all dashboards returns "OK" response

Usage:
    Install datadog_api_client package:
    'pip install datadog_api_client'

    Run this application:
    DD_SITE="datadoghq.com" DD_API_KEY="datadog_api_key" \
    DD_APP_KEY="<datadog_application_key>" python3 dashboards.py 
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DashboardsApi(api_client)
    response = api_instance.list_dashboards(
        filter_shared=False,
    )

    print(response)
