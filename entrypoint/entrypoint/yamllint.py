import io
import locale
from os.path import isfile
from typing import List

from yamllint import linter
from yamllint.config import YamlLintConfig

from entrypoint.actions import error, warning, debug


def load_conf(config: str) -> YamlLintConfig:
    if config:
        if ':' not in config:
            config = 'extends: ' + config
        conf = YamlLintConfig(content=config)
    elif isfile('.yamllint'):
        conf = YamlLintConfig(file='.yamllint')
    elif isfile('.yamllint.yaml'):
        conf = YamlLintConfig(file='.yamllint.yaml')
    elif isfile('.yamllint.yml'):
        conf = YamlLintConfig(file='.yamllint.yml')
    else:
        conf = YamlLintConfig('extends: default')

    if conf.locale is not None:
        locale.setlocale(locale.LC_ALL, conf.locale)

    return conf


def run(files: List[str], config: YamlLintConfig) -> int:
    result = 0

    for file in files:
        debug(f"Processing file \"{file}\"")
        with io.open(file) as f:
            for problem in linter.run(f, config, file):
                params = dict(
                    file=file,
                    line=problem.line,
                    col=problem.column,
                )

                if problem.level == 'error':
                    result = 1
                    error(problem.desc, **params)
                else:
                    warning(problem.desc, **params)

                print(f"{file}:{problem.line}:{problem.column}: [{problem.level}] {problem.desc}")

    return result
