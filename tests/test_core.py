from evalforge import score_cases


def test_score_cases():
    result = score_cases([{"prediction": "yes", "reference": "YES"}, {"prediction": "no", "reference": "yes"}])
    assert result == {"accuracy": 0.5, "count": 2}
