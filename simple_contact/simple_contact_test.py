import pytest
import simple_contact

# Test functions
@pytest.fixture(autouse=True)
def clear_contact_list_fixture():
    simple_contact.contact_list.clear()
    # If there's any other global state to reset, do it here.
    # For example, if simple_contact has a global variable for the next ID:
    # simple_contact.next_id = 1 # Resetting a hypothetical next_id

# Test functions

def test_display_menu(capsys):
    simple_contact.display_menu()
    captured = capsys.readouterr()
    expected_output = (
        "\n--- Main Menu ---\n"
        "1. Add Contact\n"
        "2. View All Contacts\n"
        "3. Search Contact\n"
        "4. Delete Contact\n"
        "5. Exit\n"
    )
    # Normalize whitespace for comparison, as print might add extra newlines
    assert "".join(captured.out.split()) == "".join(expected_output.split())

def test_add_contact():
    pass


def test_view_all_contacts():
    pass

def test_search_contact():
    pass

def test_delete_contact():
    pass