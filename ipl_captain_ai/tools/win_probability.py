"""
Win Probability Calculator Tool — Mathematical win probability based on match state.
Provides confidence scores and counterfactual analysis for strategic decisions.
"""
import math


def calculate_win_probability(
    innings: int,
    current_score: int,
    wickets_fallen: int,
    overs_completed: float,
    target: int = 0,
    batting_team: str = "",
    bowling_team: str = "",
    venue: str = "",
    is_powerplay: bool = False,
    is_death_overs: bool = False,
    alternative_scenario: str = "",
) -> dict:
    """Calculate win probability for the batting team based on current match state.

    Args:
        innings: Current innings (1 or 2)
        current_score: Current score of batting team
        wickets_fallen: Number of wickets fallen (0-10)
        overs_completed: Overs completed (e.g., 12.3 means 12 overs and 3 balls)
        target: Target score (required for 2nd innings, 0 for 1st innings)
        batting_team: Name of the batting team
        bowling_team: Name of the bowling team
        venue: Venue name for context
        is_powerplay: Whether currently in powerplay (overs 1-6)
        is_death_overs: Whether currently in death overs (overs 16-20)
        alternative_scenario: Description of alternative strategy to compare (e.g., "bowl spinner instead of pacer")

    Returns:
        Dictionary with win probability percentage, projected score,
        required run rate, and counterfactual comparison if alternative provided.
    """
    total_overs = 20.0
    balls_bowled = int(overs_completed) * 6 + round((overs_completed % 1) * 10)
    balls_remaining = int((total_overs * 6) - balls_bowled)

    if balls_remaining <= 0:
        balls_remaining = 1

    current_rr = (current_score / (balls_bowled / 6)) if balls_bowled > 0 else 0.0
    wickets_in_hand = 10 - wickets_fallen

    if innings == 1:
        # First innings: project final score
        projected = _project_first_innings_score(current_score, balls_bowled, balls_remaining, wickets_in_hand)
        # Win probability based on projected score vs typical venue score
        base_prob = min(85, max(15, 45 + (projected - 170) * 0.5))
        # Adjust for wickets
        if wickets_fallen >= 7:
            base_prob -= 15
        elif wickets_fallen >= 5:
            base_prob -= 8

        result = {
            "innings": 1,
            "batting_team": batting_team,
            "current_score": f"{current_score}/{wickets_fallen}",
            "overs": overs_completed,
            "current_run_rate": round(current_rr, 2),
            "projected_score": projected,
            "win_probability_pct": round(base_prob, 1),
            "assessment": _first_innings_assessment(projected, wickets_in_hand, balls_remaining),
        }
    else:
        # Second innings: chase calculation
        runs_needed = target - current_score
        required_rr = (runs_needed / (balls_remaining / 6)) if balls_remaining > 0 else 999
        win_prob = _chase_win_probability(runs_needed, balls_remaining, wickets_in_hand, required_rr)

        result = {
            "innings": 2,
            "batting_team": batting_team,
            "current_score": f"{current_score}/{wickets_fallen}",
            "overs": overs_completed,
            "target": target,
            "runs_needed": runs_needed,
            "balls_remaining": balls_remaining,
            "current_run_rate": round(current_rr, 2),
            "required_run_rate": round(required_rr, 2),
            "win_probability_pct": round(win_prob, 1),
            "assessment": _chase_assessment(runs_needed, balls_remaining, wickets_in_hand, required_rr),
        }

    # Counterfactual analysis
    if alternative_scenario:
        # Simulate impact of alternative strategy
        alt_prob_delta = _estimate_alternative_impact(alternative_scenario, result.get("win_probability_pct", 50))
        result["counterfactual"] = {
            "alternative": alternative_scenario,
            "probability_change_pct": round(alt_prob_delta, 1),
            "alternative_win_probability_pct": round(result["win_probability_pct"] + alt_prob_delta, 1),
            "verdict": "BETTER" if alt_prob_delta > 2 else "WORSE" if alt_prob_delta < -2 else "MARGINAL DIFFERENCE",
        }

    return result


def _project_first_innings_score(current: int, balls_done: int, balls_left: int, wickets_hand: int) -> int:
    """Project first innings total based on current state."""
    if balls_done == 0:
        return 170

    current_rr = current / (balls_done / 6)
    # Acceleration factor based on phase
    if balls_left > 84:  # Still in powerplay
        accel = 1.15
    elif balls_left > 30:  # Middle overs
        accel = 1.08
    else:  # Death overs
        accel = 1.25

    # Wicket penalty
    wkt_factor = max(0.6, 1 - (10 - wickets_hand) * 0.05)
    projected_remaining = current_rr * accel * wkt_factor * (balls_left / 6)

    return int(current + projected_remaining)


def _chase_win_probability(runs_needed: int, balls_left: int, wickets_hand: int, rrr: float) -> float:
    """Calculate chase win probability using a scoring-rate difficulty model."""
    if runs_needed <= 0:
        return 99.0
    if balls_left <= 0:
        return 0.0
    if wickets_hand <= 0:
        return 0.0

    # Base probability from required rate difficulty
    if rrr <= 6.0:
        base = 85
    elif rrr <= 8.0:
        base = 70
    elif rrr <= 10.0:
        base = 55
    elif rrr <= 12.0:
        base = 38
    elif rrr <= 14.0:
        base = 22
    elif rrr <= 16.0:
        base = 12
    else:
        base = 5

    # Wicket factor
    wkt_bonus = (wickets_hand - 5) * 3  # +3% per extra wicket above 5, -3% per wicket below 5

    # Balls remaining factor (more balls = better)
    ball_factor = min(10, (balls_left - runs_needed * 0.8) * 0.3)

    prob = base + wkt_bonus + ball_factor
    return max(1, min(99, prob))


def _first_innings_assessment(projected: int, wickets: int, balls: int) -> str:
    """Generate assessment text for first innings situation."""
    if projected >= 190:
        strength = "DOMINANT — on track for a massive total"
    elif projected >= 175:
        strength = "STRONG — building a competitive score"
    elif projected >= 160:
        strength = "PAR — need acceleration to finish strong"
    elif projected >= 145:
        strength = "BELOW PAR — need boundaries or will fall short"
    else:
        strength = "IN TROUBLE — need a rescue act"

    if wickets <= 3 and balls > 30:
        wicket_note = "Wickets in hand — can afford to be aggressive"
    elif wickets <= 5:
        wicket_note = "Key batters still there but need to be smart"
    else:
        wicket_note = "Deep into the tail — every run counts"

    return f"{strength}. {wicket_note}. Projected: {projected}."


def _chase_assessment(runs: int, balls: int, wickets: int, rrr: float) -> str:
    """Generate assessment text for second innings chase."""
    if rrr <= 6:
        difficulty = "COMFORTABLE — cruising to victory"
    elif rrr <= 8:
        difficulty = "MANAGEABLE — steady scoring will do"
    elif rrr <= 10:
        difficulty = "TIGHT — need to find boundaries regularly"
    elif rrr <= 12:
        difficulty = "TOUGH — need a big over or two"
    elif rrr <= 15:
        difficulty = "VERY DIFFICULT — need a Dhoni-esque finish"
    else:
        difficulty = "NEAR IMPOSSIBLE — miracle needed"

    return f"{difficulty}. Need {runs} off {balls} balls ({rrr:.1f} RPO). {wickets} wickets in hand."


def _estimate_alternative_impact(scenario: str, current_prob: float) -> float:
    """Estimate probability impact of an alternative strategy."""
    scenario_lower = scenario.lower()
    delta = 0.0

    # Positive impacts
    if any(w in scenario_lower for w in ["bumrah", "best bowler", "strike bowler"]):
        delta += 5.0
    if any(w in scenario_lower for w in ["yorker", "death specialist"]):
        delta += 3.0
    if any(w in scenario_lower for w in ["spinner", "spin"] ) and any(w in scenario_lower for w in ["turning", "spin track"]):
        delta += 4.0

    # Negative impacts
    if any(w in scenario_lower for w in ["part-timer", "part timer"]):
        delta -= 6.0
    if any(w in scenario_lower for w in ["expensive", "leaking"]):
        delta -= 4.0
    if "no change" in scenario_lower:
        delta -= 2.0

    # Random noise for realism
    import random
    delta += random.uniform(-2, 2)

    return delta
