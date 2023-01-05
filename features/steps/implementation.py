from behave import given, when, then
from common.main_class import AddRemoveUser


@given("the driver is initialized")
def init_driver(context):
    try:
        temp = context.config.userdata.get(
            "location")
        binary_location, service_location = temp.split("|")
    except BaseException:
        binary_location = None
        service_location = None
    context.cls = AddRemoveUser(binary_location, service_location)
    context.name = "Denys Lohvynov"


@when("we login successfully")
def login(context):
    context.cls.login_page()


@when("we go to the Admin panel")
def go_to_admin(context):
    context.cls.to_Admin()


@when("we add a new ESS user")
def add_new_user(context):
    context.cls.add_new_user(context.name)


@then("we check that the new ESS user is appeared in the list")
def check_new_user(context):
    assert context.cls.check_wether_in_table(context.name)


@then("we remove the row with the new ESS user")
def remove_row(context):
    context.cls.delete_raw(context.name)
    assert not context.cls.check_wether_in_table(context.name)
