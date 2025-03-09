FROM python:3.13
RUN apt-get update
RUN apt-get install jq git -y

RUN /usr/local/bin/python -m ensurepip --upgrade
#RUN /usr/local/bin/pip install poetry Django djangorestframework semver djangorestframework-recursive
RUN /usr/local/bin/pip install poetry pre-commit
#RUN mkdir -p /var/task/snyk-code-review-exercise/.venv

ADD . /var/task/qr-coder
RUN /usr/local/bin/poetry config virtualenvs.path /var/task/qr-coder/.venv

WORKDIR /var/task/qr-coder
ENV VENV_PATH=/var/task/qr-coder/.venv/bin/python

#fix pre-commit issues on container
#RUN git config --local core.fileMode false

COPY . /var/task/qr-coder
#CMD ["/var/task/snyk-code-review-exercise/start.sh"]
EXPOSE 8000