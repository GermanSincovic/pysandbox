import pytest

from tasks.basics import (
    Vlan, add_item, build_url, char_frequency, count_calls, even_squares, flatten,
    group_by_length, is_palindrome, merge_counts, reverse_words, safe_divide,
    sort_devices, unique_sorted,
)


@pytest.mark.parametrize("text, expected", [
    pytest.param("show ip route", "route ip show", id="three_words"),
    pytest.param("  a   b ", "b a", id="extra_spaces"),
    pytest.param("single", "single", id="one_word"),
    pytest.param("", "", id="empty"),
    pytest.param("show interfaces Gi0/1", "Gi0/1 interfaces show", id="special"),
    pytest.param("ip-route add", "add ip-route", id="minus"),
    pytest.param("host_name is up", "up is host_name", id="underscore"),
])
def test_01_reverse_words(text, expected):
    assert reverse_words(text) == expected


@pytest.mark.parametrize("text, expected", [
    pytest.param("Level", True, id="mixed_case"),
    pytest.param("A man, a plan, a canal: Panama", True, id="with_punctuation"),
    pytest.param("router", False, id="not_palindrome"),
    pytest.param("", True, id="empty"),
])
def test_02_is_palindrome(text, expected):
    assert is_palindrome(text) == expected


@pytest.mark.parametrize("text, expected", [
    pytest.param("aab b", {"a": 2, "b": 2}, id="skips_spaces"),
    pytest.param("abc", {"a": 1, "b": 1, "c": 1}, id="all_unique"),
    pytest.param("", {}, id="empty"),
])
def test_03_char_frequency(text, expected):
    assert char_frequency(text) == expected


@pytest.mark.parametrize("items, expected", [
    pytest.param([3, 1, 3, 2, 1], [1, 2, 3], id="numbers"),
    pytest.param(["b", "a", "b"], ["a", "b"], id="strings"),
    pytest.param([], [], id="empty"),
])
def test_04_unique_sorted(items, expected):
    assert unique_sorted(items) == expected


def test_05_merge_counts():
    a = {"x": 1, "y": 2}
    b = {"y": 3, "z": 4}
    assert merge_counts(a, b) == {"x": 1, "y": 5, "z": 4}


def test_05_merge_counts_does_not_change_input():
    a = {"x": 1}
    b = {"x": 2}
    merge_counts(a, b)
    assert a == {"x": 1}
    assert b == {"x": 2}


def test_06_group_by_length():
    assert group_by_length(["ssh", "dns", "http", "ntp"]) == {3: ["ssh", "dns", "ntp"], 4: ["http"]}
    assert group_by_length([]) == {}


@pytest.mark.parametrize("nested, expected", [
    pytest.param([[1, 2], [3], []], [1, 2, 3], id="with_empty_inner"),
    pytest.param([], [], id="empty"),
])
def test_07_flatten(nested, expected):
    assert flatten(nested) == expected


def test_08_sort_devices():
    devices = [
        {"name": "sw3", "vlan": 20},
        {"name": "sw2", "vlan": 10},
        {"name": "sw1", "vlan": 20},
    ]
    original = [dict(d) for d in devices]
    assert [d["name"] for d in sort_devices(devices)] == ["sw2", "sw1", "sw3"]
    assert devices == original, "input list must not be changed"


def test_09_add_item_new_list_each_call():
    assert add_item(1) == [1]
    assert add_item(2) == [2]


def test_09_add_item_with_given_list():
    items = ["a"]
    assert add_item("b", items) == ["a", "b"]
    items = []
    add_item("x", items)
    assert items == ["x"]


@pytest.mark.parametrize("args, kwargs, expected", [
    pytest.param(("api.local",), {}, "https://api.local", id="host_only"),
    pytest.param(("api.local", "v1", "alarms"), {}, "https://api.local/v1/alarms", id="path"),
    pytest.param(("api.local", "v1"), {"limit": 10, "page": 2},
                 "https://api.local/v1?limit=10&page=2", id="path_and_params"),
    pytest.param(("api.local",), {"q": "x"}, "https://api.local?q=x", id="params_only"),
])
def test_10_build_url(args, kwargs, expected):
    assert build_url(*args, **kwargs) == expected


@pytest.mark.parametrize("a, b, expected", [
    pytest.param(10, 4, 2.5, id="normal"),
    pytest.param(1, 0, None, id="zero"),
    pytest.param(0, 5, 0, id="zero_numerator"),
])
def test_11_safe_divide(a, b, expected):
    assert safe_divide(a, b) == expected


def test_12_vlan_repr():
    assert repr(Vlan(10, "users")) == "Vlan(10, 'users')"
    assert repr(Vlan(10, "O'Brien")) == "Vlan(10, 'O'Brien')"
    # Якраз без !r працює нормально


def test_12_vlan_equal_by_vid():
    assert Vlan(10, "users") == Vlan(10, "other")
    assert Vlan(10, "users") != Vlan(20, "users")


def test_12_vlan_in_set():
    assert len({Vlan(10, "a"), Vlan(10, "b"), Vlan(20, "c")}) == 2


@pytest.mark.parametrize("vid", [0, 4095, -1])
def test_12_vlan_invalid_vid(vid):
    with pytest.raises(ValueError):
        Vlan(vid, "bad")


def test_13_even_squares():
    assert list(even_squares(7)) == [0, 4, 16, 36]
    assert list(even_squares(0)) == []


def test_13_even_squares_is_generator():
    gen = even_squares(10)
    assert next(gen) == 0
    assert next(gen) == 4


def test_14_count_calls():
    @count_calls
    def ping(host):
        """Ping a host."""
        return f"pong {host}"

    assert ping("a") == "pong a"
    ping("b")
    assert ping.calls == 2
    assert ping.__name__ == "ping"
    assert ping.__doc__ == "Ping a host."
