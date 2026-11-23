import pytest

from tasks.logs import WordCounter, chunks, top_ips


def test_word_counter():
    wc = WordCounter()
    wc.add_word("apple")
    wc.add_word("banana")
    wc.add_word("apple")
    assert wc.get_count("apple") == 2
    assert wc.get_count("banana") == 1
    assert wc.get_count("cucumber") == 0


def test_word_counter_instances_are_independent():
    a = WordCounter()
    b = WordCounter()
    a.add_word("x")
    assert b.get_count("x") == 0


def test_top_ips():
    lines = [
        "10.0.0.1 GET /",
        "10.0.0.2 GET /",
        "",
        "10.0.0.1 GET /a",
        "10.0.0.3 GET /",
        "10.0.0.1 POST /b",
        "10.0.0.2 GET /c",
    ]
    assert top_ips(lines, 2) == [("10.0.0.1", 3), ("10.0.0.2", 2)]


def test_top_ips_empty():
    assert top_ips([], 3) == []


@pytest.mark.parametrize("items, size, expected", [
    pytest.param([1, 2, 3, 4, 5], 2, [[1, 2], [3, 4], [5]], id="with_tail"),
    pytest.param([1, 2, 3, 4], 2, [[1, 2], [3, 4]], id="no_empty_tail"),
    pytest.param([], 3, [], id="empty"),
    pytest.param([1, 2], 5, [[1, 2]], id="size_bigger_than_list"),
])
def test_chunks(items, size, expected):
    assert list(chunks(items, size)) == expected


def test_chunks_is_generator():
    gen = chunks([1, 2, 3], 1)
    assert next(gen) == [1]
