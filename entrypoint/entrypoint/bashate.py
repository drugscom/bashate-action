from bashate.bashate import BashateRun
from entrypoint import actions


class RunnerWithActionsReporter(BashateRun):
    def log_error(self, error, line, filename, filelineno, warn=False):
        super(RunnerWithActionsReporter, self).log_error(
            error, line, filename, filelineno, warn
        )

        params = dict(
            file=filename,
            line=filelineno,
        )

        if warn:
            actions.warning(error, **params)
        else:
            actions.error(error, **params)
