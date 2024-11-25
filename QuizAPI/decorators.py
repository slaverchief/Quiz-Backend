from QuizAPI.exceptions import HandledException
from rest_framework.response import Response


def handle_exceptions(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            return func(self, request, *args, **kwargs)
        except HandledException as exc:
           return Response(status=400, data={'detail': str(exc)})
    return wrapper