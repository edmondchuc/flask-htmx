from flask.testing import FlaskClient


def test_hx_boost_true(client: FlaskClient):
    headers = {"HX-Boosted": "true"}
    rv = client.get("/hx-boost", headers=headers)
    assert rv.data.decode("utf-8") == "True"


def test_hx_boost_false(client: FlaskClient):
    rv = client.get("/hx-boost")
    assert rv.data.decode("utf-8") == "False"


def test_hx_current_url_set(client: FlaskClient):
    headers = {"HX-Current-URL": "http://localhost"}
    rv = client.get("/hx-current-url", headers=headers)
    assert rv.data.decode("utf-8") == "http://localhost"


def test_hx_current_url_not_set(client: FlaskClient):
    rv = client.get("/hx-current-url")
    assert rv.data.decode("utf-8") == "None"


def test_hx_history_restore_request_true(client: FlaskClient):
    headers = {"HX-History-Restore-Request": "true"}
    rv = client.get("/hx-history-restore-request", headers=headers)
    assert rv.data.decode("utf-8") == "True"


def test_hx_history_restore_request_false(client: FlaskClient):
    rv = client.get("/hx-history-restore-request")
    assert rv.data.decode("utf-8") == "False"


def test_hx_prompt_set(client: FlaskClient):
    prompt_value = "Enter your account name to confirm deletion"
    headers = {"HX-Prompt": prompt_value}
    rv = client.get("/hx-prompt", headers=headers)
    assert rv.data.decode("utf-8") == prompt_value


def test_hx_prompt_not_set(client: FlaskClient):
    rv = client.get("/hx-prompt")
    assert rv.data.decode("utf-8") == "None"


def test_hx_request_set(client: FlaskClient):
    headers = {"HX-Request": "true"}
    rv = client.get("/hx-request", headers=headers)
    assert rv.data.decode("utf-8") == "True"


def test_hx_request_not_set(client: FlaskClient):
    rv = client.get("/hx-request")
    assert rv.data.decode("utf-8") == "False"


def test_hx_target_set(client: FlaskClient):
    target_value = "some-element-id"
    headers = {"HX-Target": target_value}
    rv = client.get("/hx-target", headers=headers)
    assert rv.data.decode("utf-8") == target_value


def test_hx_target_not_set(client: FlaskClient):
    rv = client.get("/hx-target")
    assert rv.data.decode("utf-8") == "None"


def test_hx_trigger_name_set(client: FlaskClient):
    trigger_name_value = "element-name"
    headers = {"HX-Trigger-Name": trigger_name_value}
    rv = client.get("/hx-trigger-name", headers=headers)
    assert rv.data.decode("utf-8") == trigger_name_value


def test_hx_trigger_name_not_set(client: FlaskClient):
    rv = client.get("/hx-trigger-name")
    assert rv.data.decode("utf-8") == "None"


def test_hx_trigger_set(client: FlaskClient):
    trigger_id = "element-id"
    headers = {"HX-Trigger": trigger_id}
    rv = client.get("/hx-trigger", headers=headers)
    assert rv.data.decode("utf-8") == trigger_id


def test_hx_trigger_not_set(client: FlaskClient):
    rv = client.get("/hx-trigger")
    assert rv.data.decode("utf-8") == "None"
