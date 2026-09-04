"""Evaluate paired prediction/reference cases."""


def score_cases(cases: list[dict]) -> dict[str, float]:
    """Return exact-match accuracy and evaluated case count."""
    if not cases:
        return {"accuracy": 0.0, "count": 0}
    correct = sum(
        str(case.get("prediction", "")).strip().casefold()
        == str(case.get("reference", "")).strip().casefold()
        for case in cases
    )
    return {"accuracy": correct / len(cases), "count": len(cases)}
