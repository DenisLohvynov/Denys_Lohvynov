from behave import given, when, then
from common.dropbox import DropBoxRequest


@given('Dropbox API with access to a file')
def initialization(context):
    from common.cfg import cfg
    context.tester = DropBoxRequest(cfg["access_token"])
    context.cfg = cfg


@when("Send request to Dropbox to recieve file's metadata")
def get_name(context):
    context.response = context.tester.file_get_metadata(
        context.cfg["relative_path"]+context.cfg["name_of_file_to_upload"])


@then('Receive response with')
def check(context):
    assert context.response.ok
    assert context.response.json()['name'] == context.cfg[
        "name_of_file_to_upload"]
