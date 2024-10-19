from datetime import datetime
from pathlib import Path


class Log:
    def __init__(self, time, code, description):
        _DIR_ = Path(__file__).resolve().parent
        self.log_file_path = _DIR_ / 'logs' / str(time.year) / str(time.month) / f'{time.day}.html'
        self.log_file_path.parent.mkdir(parents=True, exist_ok=True)
        self.time = time
        self.description = description
        self.code = code
        self.common_color = '545454'
        self.warning_color = 'C4B933'
        self.error_color = 'B44545'

        if self.log_file_path.stat().st_size == 0:
            with open(self.log_file_path, 'w') as log:
                log.write('<style>body { background-color: #2B2D30; color: white; }</style>')

    def writer(self, color, status):
        with open(self.log_file_path, 'a+') as log:
            log.write(
                f'<p style="color: #{color}; margin-top: 2px; '
                f'margin-bottom: 2px;">[{self.time.hour}:'
                f'{self.time.minute}:{self.time.second}] '
                f'{self.code} {status}: {self.description}.</p>'
            )

    def common(self):
        self.writer(color=self.common_color, status='COMMON')

    def warning(self):
        self.writer(color=self.warning_color, status='WARNING')

    def error(self):
        self.writer(color=self.error_color, status='ERROR')


Log(datetime.now(), 200, 'description common').common()
Log(datetime.now(), 404, 'description warning').warning()
Log(datetime.now(), 500, 'description error').error()
