from aws_cdk import core, aws_lambda


class MainStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        layer = aws_lambda.LayerVersion(
            self, "dependencies", code=aws_lambda.AssetCode("python.zip")
        )

        aws_lambda.Function(
            self,
            "Hello World",
            code=aws_lambda.Code.from_asset("lambda/"),
            handler="main.handler",
            runtime=aws_lambda.Runtime.PYTHON_3_7,
            layers=[layer],
        )
