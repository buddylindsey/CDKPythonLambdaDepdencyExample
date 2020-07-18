#!/usr/bin/env python3

from aws_cdk import core

from stacks.main_stack import MainStack


app = core.App()
MainStack(app, "CDKPythonLambdaDepdencyExample")

app.synth()
