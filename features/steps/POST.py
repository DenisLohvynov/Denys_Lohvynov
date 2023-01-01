from behave import given, when, then
from common.dropbox import DropBoxRequest


@given('Dropbox API')
def initialization(context):
    from common.cfg import cfg
    context.tester = DropBoxRequest(cfg["access_token"])
    context.cfg = cfg


@when('Send request to Dropbox to upload file')
def file_upload(context):
    with open(f'common/{context.cfg["name_of_file_to_upload"]}',
              'rb') as f:
        context.response = context.tester.file_upload(
            context.cfg["relative_path"] +
            context.cfg["name_of_file_to_upload"], f.read())


@then('Receive response about successful operation')
def check(context):
    assert context.response.ok
