from project import *
import builtins as __builtins__
import sys
import io

def test_save_p():
    input_values = ["1234"]
    expected_output = "Facebook - 1234"

    original_input = __builtins__.input
    __builtins__.input = lambda _: input_values.pop(0)

    save_p("Facebook")

    __builtins__.input = original_input

    with open("passwords.txt", "r") as file:
        content = file.read().strip()
        assert content == expected_output, f"Test failed. Expected: {expected_output}, Got: {content}"

def test_same_name():
    data  = []
    with open('passwords.txt', 'r', encoding='utf-8') as file:
        for  line in file:
            data.append(f"{line.rstrip()} \n")
    input_value = ["2","123456"]
    expected_output = "Facebook - 123456"
    original_input = __builtins__.input
    __builtins__.input = lambda _: input_value.pop(0)
    same_name("Facebook", data)
    __builtins__.input = original_input

    with open("passwords.txt", "r") as file:
        content = file.read().strip()
        assert content == expected_output, f"Test failed. Expected: {expected_output}, Got: {content}"

def test_get_name():
    data  = []
    with open('passwords.txt', 'r', encoding='utf-8') as file:
        for  line in file:
            data.append(f"{line.rstrip()} \n")
    input_values = ["Twitter", "1234"]
    expected_output = "Facebook - 123456\nTwitter - 1234"

    original_input = __builtins__.input
    __builtins__.input = lambda _: input_values.pop(0)

    get_name(data)

    __builtins__.input = original_input

    with open("passwords.txt", "r") as file:
        content = file.read().strip()
        assert content == expected_output, f"Test failed. Expected: {expected_output}, Got: {content}"

def test_same1():
    input_value = ["hello"]
    expected_output = "Facebook - 123456\nTwitter - 1234\nFacebook - hello"
    original_input = __builtins__.input
    __builtins__.input = lambda _: input_value.pop(0)
    same1("Facebook")
    __builtins__.input = original_input

    with open("passwords.txt", "r") as file:
        content = file.read().strip()
        assert content == expected_output, f"Test failed. Expected: {expected_output}, Got: {content}"

def test_menu():
    captured_output = io.StringIO()
    sys.stdout = captured_output
    menu()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    expected_output = ("\n\n================\nPassword Manager\n================\n[1] List saved passwords\n[2] Save new password\n[3] Generate new password\n[4] Quit Program\n================\n")
    assert output == expected_output, f"Test Failed. Expected: {expected_output}, Got: {output}"

def test_select_menu():
    input_value = "4"
    expected_output = ""
    original_input = __builtins__.input
    __builtins__.input = lambda _: input_value
    select_menu()
    __builtins__.input = original_input
    captured_output = io.StringIO()
    sys.stdout = captured_output
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    assert output == expected_output, f"Test failed. Expected: {expected_output}, Got: {output}"

def test_get_passwords():
    expected_output = ["1 Facebook - 123456 ", "2 Twitter - 1234 ", "3 Facebook - hello "]
    passwords = get_passwords()
    assert passwords == expected_output, f"Test failed. Expected: {expected_output}, Got: {passwords}"

def test_edit_menu():
    data  = []
    with open('passwords.txt', 'r', encoding='utf-8') as file:
        for  line in file:
            data.append(f"{line.rstrip()} \n")
    input_value = ["1","12345"]
    expected_output = "Facebook - 12345\nTwitter - 1234 \nFacebook - hello"
    original_input = __builtins__.input
    __builtins__.input = lambda _: input_value.pop(0)
    edit_menu(data)
    __builtins__.input = original_input
    with open("passwords.txt", "r") as file:
        content = file.read().strip()
        assert content == expected_output, f"Test failed. Expected: {expected_output}, Got: {content}"

def test_delete_menu():
    data  = []
    with open('passwords.txt', 'r', encoding='utf-8') as file:
        for  line in file:
            data.append(f"{line.rstrip()} \n")
    input_value = "1"
    expected_output = ""
    original_input = __builtins__.input
    __builtins__.input = lambda _: input_value
    delete_menu(data)
    __builtins__.input = original_input
    with open("passwords.txt", "r") as file:
        content = file.read().strip()
        assert content == expected_output, f"Test failed. Expected: {expected_output}, Got: {content}"

def test_give_generated():
    input_value = ["y", "10"]
    expected_output = 10
    original_input = __builtins__.input
    __builtins__.input = lambda _: input_value.pop(0)
    generated = give_generated()
    __builtins__.input = original_input
    assert len(generated) == expected_output, f"Test failed. Expected: {expected_output}, Got: {len(generated)}"

def test_select_menu2():
    data  = ["a"]
    input_value = "3"
    expected_output = ""
    original_input = __builtins__.input
    __builtins__.input = lambda _: input_value
    select_menu2(data)
    __builtins__.input = original_input
    captured_output = io.StringIO()
    sys.stdout = captured_output
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    assert output == expected_output, f"Çıktı kontrolü başarısız. Beklenen: {expected_output}, Alınan: {output}"