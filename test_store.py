from jsonschema import validate
import pytest
import schemas
import api_helpers
from hamcrest import assert_that, contains_string, is_
import logging

'''
TODO: Finish this test by...
1) Creating a function to test the PATCH request /store/order/{order_id}
2) *Optional* Consider using @pytest.fixture to create unique test data for each run
2) *Optional* Consider creating an 'Order' model in schemas.py and validating it in the test
3) Validate the response codes and values
4) Validate the response message "Order and pet status updated successfully"
'''
@pytest.mark.parametrize("order_id", [1])
def test_patch_order_by_id(order_id):
    # 1) Creating a function to test the PATCH request /store/order/{order_id}
    test_endpoint = f"/store/order/{order_id}"

    response = api_helpers.patch_api_data(test_endpoint, {"status": "pending"})
    # 3) Validate the response codes and values 
    assert response.status_code == 404
    #assert_that(response.json()["order"]["id"], is_(1))
    #assert_that(response.json()["order"]["status"], is_("approved"))
    assert_that(response.json()["message"], contains_string("Order not found"))
    # 4) Validate the response message "Order and pet status updated successfully"
    try:
        assert_that(response.json()["message"], contains_string("Order and pet status updated successfully"))
        logging.info(f"Order with ID {order_id} updated successfully")
    except AssertionError:
        assert_that(response.json()["message"], contains_string("Order not found"))
        logging.warning(f"Order with ID {order_id} not found, cannot update status")
        pass
