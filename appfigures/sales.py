from base import BaseClient

SALES_BASE_URI = "sales"

class SalesClient(BaseClient):
    def __init__(self, result_service, uri=SALES_BASE_URI, **kwargs):
        super(SalesClient, self).__init__(uri, result_service)

    def get_sales_report(self, report_type, startdate, enddate, **kwargs):
        args = (report_type, startdate, enddate)
        result = self.get_response(args, kwargs)
        return result