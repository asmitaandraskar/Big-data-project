import boto3
import pprint
session = boto3.Session(region_name='us-east-1',
aws_access_key_id="ASIAQEDJZY5T3Q4MCN7V",
aws_secret_access_key="lZckpfjkfpAH3CmyI701xDq+H4PTQh02VyvoVimW",
aws_session_token="FwoGZXIvYXdzECcaDL7K+IVjBpoiti/lkSLGAduxj9pw5375Xst6hUR7g9xbWkWAm5uNRP/rVJN56jyEHF7fcE5CdaZy+GJsAs7R/CAmEKJYJcx9o0qFqm/piaVh/WRSSPOZ4m7q6JMAX3GdNaaOXgJExQDFzcn3K0qR8VMviXr86JaIf86LhKuHhkqRbrldfKefTZV4ho3/4Oxi/J8xCpXNw0gW2qpiSpg10NNuCZOJswljirMB3LuD9ehTD0K/p/CeidqSeV8Trdk3EzuEJKVOnIpRSs50Ae15az4Uu/9lzSjq8YegBjItKrKzk1G3u92cYQTeSOrRYPt2heL8y3NEEyzV2Hmcq260EvDEKATz+rKzri1R")

cloud_cl_ob = session.client('cloudformation')
# pprint.pprint(cloud_cl_ob.describe_stacks())

stack_template = ""
with open(f"emr_template.json","r") as fd:
    stack_template = fd.read()
# print(stack_template)

params = [
    {
        "ParameterKey" : 'KeyName',
        "ParameterValue" : 'testkey'
    }
]
cloud_cl_ob.create_stack(StackName="TestingEMRusingPython1",TemplateBody=stack_template,Parameters=params)