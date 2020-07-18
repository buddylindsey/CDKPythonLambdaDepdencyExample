#!/usr/bin/env python3

from aws_cdk import core

from anothertest.anothertest_stack import AnothertestStack


app = core.App()
AnothertestStack(app, "anothertest")

app.synth()
