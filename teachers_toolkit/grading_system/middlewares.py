import datetime


class CourseMiddleware(object):

    def process_request(self, request):
        request._request_time = datetime.now()
