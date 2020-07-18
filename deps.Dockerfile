FROM amazonlinux:2

RUN yum install -y python37 && \
    yum install -y python3-pip && \
    yum install -y zip && \
    yum clean all
RUN python3.7 -m pip install --upgrade pip && \
    python3.7 -m pip install virtualenv

RUN mkdir -p /opt/deps/{python,output,requirements}
VOLUME ["/opt/deps/output", "/opt/deps/requirements"]
WORKDIR /opt/deps

RUN python3.7 -m venv deps

COPY scripts/builddeps.sh /opt/deps
COPY requirements/lambda.txt /opt/deps

CMD ["./builddeps.sh"]