from datetime import datetime
from http import HTTPStatus
from pathlib import Path
from functools import wraps

from rest_framework.response import Response


admin_list = {
    'DESKTOP-ELDL6E7': 'lasellar',
}


def log_decorator(func):
    @wraps(func)
    def wrapper(request, **kwargs):
        if request.META["COMPUTERNAME"] in admin_list:
            description = admin_list[request.META["COMPUTERNAME"]] + ' ' + request.META['HTTP_HOST']
        else:
            description = request.META['HTTP_HOST'] + (
                f' COMPUTERNAME: {request.META["COMPUTERNAME"]}'
                f' SERVER_NAME: {request.META["SERVER_NAME"]}'
            )
        try:
            if func.__name__ == 'logs':
                Log(datetime.now(), 200, 'LOGGER', description).warning()
                return func(request, **kwargs)
            Log(datetime.now(), HTTPStatus.OK, request.path, description).common()
            return func(request, **kwargs)
        except Exception as exception:
            Log(datetime.now(), HTTPStatus.INTERNAL_SERVER_ERROR, request.path,
                description=f'{description} {str(exception)}').error()
            return Response({'error': str(exception)}, status=HTTPStatus.INTERNAL_SERVER_ERROR)
    return wrapper


class Log:
    def __init__(self, time, code, endpoint, description):
        _DIR_ = Path(__file__).resolve().parent
        self.log_file_path = _DIR_ / 'logs' / str(time.year) / str(time.month) / f'{time.day}.html'
        self.log_file_path.parent.mkdir(parents=True, exist_ok=True)
        self.time = time
        self.description = description
        self.code = code
        self.common_color = '545454'
        self.warning_color = 'C4B933'
        self.error_color = 'B44545'
        self.endpoint = endpoint

        if self.log_file_path.stat().st_size == 0:
            with open(self.log_file_path, 'w') as log:
                log.write('<style>body { background-color: #2B2D30; color: white; }</style>')

    def writer(self, color, status):
        with open(self.log_file_path, 'a+') as log:
            log.write(
                f'<p style="color: #{color}; margin-top: 2px; '
                f'margin-bottom: 2px;">[{self.time.strftime("%H:%M:%S")}] '
                f'{self.code} {status}: {self.endpoint} {self.description}.</p>'
            )

    def common(self):
        self.writer(color=self.common_color, status='COMMON')

    def warning(self):
        self.writer(color=self.warning_color, status='WARNING')

    def error(self):
        self.writer(color=self.error_color, status='ERROR')
