from behave import given, when, then
from common.dropbox import DropBoxRequest


@given('Dropbox API with the access to a file')
def initialization(context):
    from common.cfg import cfg
    context.tester = DropBoxRequest(cfg["access_token"])
    context.cfg = cfg


@when("Send request to Dropbox to delete file")
def actual_deletion(context):
    context.response = context.tester.file_delete(
        context.cfg["relative_path"]+context.cfg["name_of_file_to_upload"])


@then('Receive response about successful deletion')
def check(context):
    assert context.response.ok
