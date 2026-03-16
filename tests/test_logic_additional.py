from logic_utils import (
    parse_guess,
    check_guess_with_message,
    update_score,
)


def test_parse_guess_decimal():
    ok, val, err = parse_guess("42.0")
    assert ok is True
    assert val == 42
    assert err is None


def test_parse_guess_invalid():
    ok, val, err = parse_guess("not-a-number")
    assert ok is False
    assert val is None
    assert err == "That is not a number."


def test_check_guess_with_message_high_low_win():
    outcome, message = check_guess_with_message(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message.upper()

    outcome, message = check_guess_with_message(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message.upper()

    outcome, message = check_guess_with_message(50, 50)
    assert outcome == "Win"
    assert "CORRECT" in message.upper()


def test_update_score_win_min_points():
    # Large attempt number should floor points to 10
    score = update_score(0, "Win", 20)
    assert score == 10


def test_update_score_too_high_even_odd():
    # Even attempts give +5 for Too High
    s = update_score(0, "Too High", 2)
    assert s == 5
    # Odd attempts give -5 for Too High
    s = update_score(0, "Too High", 1)
    assert s == -5


def test_update_score_too_low():
    s = update_score(10, "Too Low", 3)
    assert s == 5
