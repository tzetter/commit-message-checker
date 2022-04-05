from setuptools import setup

setup(
    name='commit-message-checker',
    entry_points = {
        'console_scripts': [
            'commit-message-checker = commit_message_checker.check:check_commit_message',
        ],
    },
)