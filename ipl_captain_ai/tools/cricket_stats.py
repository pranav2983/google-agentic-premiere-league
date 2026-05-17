"""
Cricket Stats Database Tool — Provides IPL player statistics.
Real ADK function tool invoked via Gemini function calling.
"""

BATTING_STATS = {
    "Virat Kohli": {"role":"Top-order","hand":"Right","team":"RCB","overall_sr":131.6,"powerplay_sr":138.2,"middle_sr":128.5,"death_sr":152.3,"vs_pace_sr":134.1,"vs_spin_sr":127.8,"avg":38.2,"runs":7500,"matches":245,"form_last5":"42,73*,18,56,91"},
    "Rohit Sharma": {"role":"Opener","hand":"Right","team":"MI","overall_sr":130.6,"powerplay_sr":142.5,"middle_sr":125.8,"death_sr":148.7,"vs_pace_sr":135.2,"vs_spin_sr":124.3,"avg":30.5,"runs":6200,"matches":250,"form_last5":"35,12,67*,44,28"},
    "Suryakumar Yadav": {"role":"Middle-order","hand":"Right","team":"MI","overall_sr":147.3,"powerplay_sr":135.6,"middle_sr":145.2,"death_sr":168.9,"vs_pace_sr":152.1,"vs_spin_sr":141.5,"avg":31.8,"runs":3200,"matches":130,"form_last5":"78*,53,8,45,62*"},
    "Shubman Gill": {"role":"Opener","hand":"Right","team":"GT","overall_sr":133.8,"powerplay_sr":140.2,"middle_sr":130.5,"death_sr":145.3,"vs_pace_sr":136.4,"vs_spin_sr":129.7,"avg":35.6,"runs":2800,"matches":95,"form_last5":"56,89*,24,37,71"},
    "Rishabh Pant": {"role":"WK-Batter","hand":"Left","team":"LSG","overall_sr":148.7,"powerplay_sr":155.3,"middle_sr":142.8,"death_sr":172.4,"vs_pace_sr":151.2,"vs_spin_sr":144.6,"avg":28.3,"runs":2400,"matches":98,"form_last5":"67*,23,88,14,52"},
    "MS Dhoni": {"role":"Finisher","hand":"Right","team":"CSK","overall_sr":135.2,"powerplay_sr":120.5,"middle_sr":128.6,"death_sr":165.8,"vs_pace_sr":138.4,"vs_spin_sr":130.1,"avg":39.1,"runs":5200,"matches":264,"form_last5":"28*,37,15,20*,46*"},
    "Hardik Pandya": {"role":"All-rounder","hand":"Right","team":"MI","overall_sr":153.6,"powerplay_sr":145.2,"middle_sr":148.3,"death_sr":175.6,"vs_pace_sr":155.8,"vs_spin_sr":150.2,"avg":27.5,"runs":2100,"matches":120,"form_last5":"45*,12,63,34,8"},
    "Ravindra Jadeja": {"role":"All-rounder","hand":"Left","team":"CSK","overall_sr":127.5,"powerplay_sr":110.3,"middle_sr":122.8,"death_sr":158.4,"vs_pace_sr":130.2,"vs_spin_sr":123.5,"avg":26.8,"runs":2700,"matches":220,"form_last5":"31,44*,19,52,8"},
    "Sanju Samson": {"role":"WK-Batter","hand":"Right","team":"RR","overall_sr":136.8,"powerplay_sr":148.5,"middle_sr":132.4,"death_sr":155.2,"vs_pace_sr":140.3,"vs_spin_sr":131.7,"avg":29.4,"runs":3400,"matches":160,"form_last5":"82*,15,47,33,68"},
    "KL Rahul": {"role":"Opener","hand":"Right","team":"DC","overall_sr":134.2,"powerplay_sr":139.8,"middle_sr":130.5,"death_sr":152.1,"vs_pace_sr":137.5,"vs_spin_sr":129.8,"avg":37.8,"runs":4500,"matches":145,"form_last5":"45,71*,12,58,36"},
    "Travis Head": {"role":"Opener","hand":"Left","team":"SRH","overall_sr":158.3,"powerplay_sr":168.5,"middle_sr":150.2,"death_sr":170.1,"vs_pace_sr":162.4,"vs_spin_sr":152.8,"avg":32.1,"runs":1200,"matches":28,"form_last5":"89,102*,45,23,67"},
    "Heinrich Klaasen": {"role":"Middle-order","hand":"Right","team":"SRH","overall_sr":171.2,"powerplay_sr":140.5,"middle_sr":165.8,"death_sr":198.5,"vs_pace_sr":168.3,"vs_spin_sr":175.6,"avg":33.5,"runs":1500,"matches":40,"form_last5":"56*,72,34,91*,18"},
}

BOWLING_STATS = {
    "Jasprit Bumrah": {"role":"Fast","style":"Right-arm fast","team":"MI","overall_econ":7.4,"powerplay_econ":7.1,"middle_econ":7.0,"death_econ":8.2,"wickets":165,"matches":130,"avg":23.5,"dot_pct":48.5,"vs_lhb_econ":7.8,"vs_rhb_econ":7.1,"form_last5":"2/24,1/32,3/18,0/38,2/26"},
    "Rashid Khan": {"role":"Leg-spinner","style":"Right-arm leg-break","team":"GT","overall_econ":6.6,"powerplay_econ":7.2,"middle_econ":6.2,"death_econ":8.5,"wickets":130,"matches":110,"avg":21.2,"dot_pct":45.3,"vs_lhb_econ":7.1,"vs_rhb_econ":6.3,"form_last5":"2/18,1/28,2/22,3/15,1/30"},
    "Yuzvendra Chahal": {"role":"Leg-spinner","style":"Right-arm leg-break","team":"PBKS","overall_econ":7.6,"powerplay_econ":8.2,"middle_econ":7.0,"death_econ":9.8,"wickets":187,"matches":158,"avg":22.8,"dot_pct":42.1,"vs_lhb_econ":7.2,"vs_rhb_econ":7.9,"form_last5":"1/35,2/28,0/42,3/22,1/38"},
    "Ravindra Jadeja": {"role":"Spin all-rounder","style":"Left-arm orthodox","team":"CSK","overall_econ":7.6,"powerplay_econ":7.8,"middle_econ":7.2,"death_econ":9.1,"wickets":150,"matches":220,"avg":30.5,"dot_pct":40.8,"vs_lhb_econ":6.8,"vs_rhb_econ":8.2,"form_last5":"1/28,2/24,0/32,1/30,2/22"},
    "Mohammed Shami": {"role":"Fast","style":"Right-arm fast-medium","team":"SRH","overall_econ":8.0,"powerplay_econ":7.5,"middle_econ":7.8,"death_econ":9.2,"wickets":95,"matches":78,"avg":24.8,"dot_pct":44.2,"vs_lhb_econ":8.5,"vs_rhb_econ":7.6,"form_last5":"3/22,1/38,2/30,0/42,2/28"},
    "Trent Boult": {"role":"Fast","style":"Left-arm fast-medium","team":"RR","overall_econ":8.1,"powerplay_econ":7.2,"middle_econ":8.0,"death_econ":9.5,"wickets":105,"matches":85,"avg":26.2,"dot_pct":43.5,"vs_lhb_econ":7.5,"vs_rhb_econ":8.5,"form_last5":"2/28,1/35,2/24,1/42,3/20"},
    "R Ashwin": {"role":"Off-spinner","style":"Right-arm off-break","team":"CSK","overall_econ":6.9,"powerplay_econ":7.5,"middle_econ":6.5,"death_econ":8.8,"wickets":180,"matches":210,"avg":27.5,"dot_pct":46.2,"vs_lhb_econ":6.2,"vs_rhb_econ":7.5,"form_last5":"2/22,1/26,2/18,1/35,0/28"},
    "Kagiso Rabada": {"role":"Fast","style":"Right-arm fast","team":"GT","overall_econ":8.2,"powerplay_econ":7.8,"middle_econ":7.9,"death_econ":9.5,"wickets":90,"matches":60,"avg":25.1,"dot_pct":42.8,"vs_lhb_econ":8.8,"vs_rhb_econ":7.8,"form_last5":"2/32,3/28,1/40,2/35,1/30"},
    "Kuldeep Yadav": {"role":"Chinaman","style":"Left-arm wrist spin","team":"DC","overall_econ":7.8,"powerplay_econ":8.5,"middle_econ":7.2,"death_econ":9.5,"wickets":72,"matches":65,"avg":25.5,"dot_pct":40.5,"vs_lhb_econ":8.5,"vs_rhb_econ":7.2,"form_last5":"3/18,1/32,2/25,0/38,2/22"},
    "Arshdeep Singh": {"role":"Fast","style":"Left-arm fast-medium","team":"PBKS","overall_econ":8.8,"powerplay_econ":7.8,"middle_econ":8.5,"death_econ":10.2,"wickets":85,"matches":70,"avg":27.5,"dot_pct":38.5,"vs_lhb_econ":8.2,"vs_rhb_econ":9.2,"form_last5":"2/35,1/42,3/28,1/38,2/30"},
}

VENUE_STATS = {
    "Wankhede Stadium, Mumbai": {"avg_1st":178,"avg_2nd":165,"chase_win_pct":52,"pace_wkt_pct":58,"spin_wkt_pct":42,"boundary":"Short straight 75m","pitch":"Flat batting track with late dew","dew":"Heavy after 8pm","pp_avg":52},
    "MA Chidambaram, Chennai": {"avg_1st":162,"avg_2nd":152,"chase_win_pct":42,"pace_wkt_pct":38,"spin_wkt_pct":62,"boundary":"Large 80m+","pitch":"Slow turner, assists spin","dew":"Moderate","pp_avg":45},
    "M Chinnaswamy, Bengaluru": {"avg_1st":185,"avg_2nd":175,"chase_win_pct":55,"pace_wkt_pct":52,"spin_wkt_pct":48,"boundary":"Short 65m","pitch":"Excellent batting, true bounce","dew":"Light","pp_avg":56},
    "Eden Gardens, Kolkata": {"avg_1st":170,"avg_2nd":160,"chase_win_pct":48,"pace_wkt_pct":50,"spin_wkt_pct":50,"boundary":"Massive 82m+","pitch":"Pace-friendly early, slows down","dew":"Heavy","pp_avg":48},
    "Narendra Modi, Ahmedabad": {"avg_1st":168,"avg_2nd":158,"chase_win_pct":45,"pace_wkt_pct":48,"spin_wkt_pct":52,"boundary":"Largest 90m+","pitch":"Spin-friendly, variable bounce","dew":"Light","pp_avg":46},
    "Arun Jaitley, Delhi": {"avg_1st":175,"avg_2nd":165,"chase_win_pct":50,"pace_wkt_pct":55,"spin_wkt_pct":45,"boundary":"Medium 72m","pitch":"Good batting, some spin later","dew":"Moderate-heavy","pp_avg":50},
    "Rajiv Gandhi, Hyderabad": {"avg_1st":172,"avg_2nd":162,"chase_win_pct":47,"pace_wkt_pct":54,"spin_wkt_pct":46,"boundary":"Medium-large 76m","pitch":"Pace and bounce","dew":"Moderate","pp_avg":49},
    "Sawai Mansingh, Jaipur": {"avg_1st":170,"avg_2nd":160,"chase_win_pct":46,"pace_wkt_pct":45,"spin_wkt_pct":55,"boundary":"Small 68m","pitch":"Slow, low bounce, spin-friendly","dew":"Light","pp_avg":47},
    "IS Bindra, Mohali": {"avg_1st":173,"avg_2nd":163,"chase_win_pct":49,"pace_wkt_pct":57,"spin_wkt_pct":43,"boundary":"Medium 74m","pitch":"Pace-friendly, seam early","dew":"Heavy evening","pp_avg":51},
}


def get_player_stats(player_name: str, stat_type: str = "batting") -> dict:
    """Look up IPL statistics for a specific player.
    Args:
        player_name: Full name of the cricket player (e.g., "Virat Kohli", "Jasprit Bumrah")
        stat_type: Type of stats to retrieve — "batting" or "bowling"
    Returns:
        Dictionary containing the player's IPL statistics.
    """
    db = BATTING_STATS if stat_type == "batting" else BOWLING_STATS
    if player_name in db:
        return {"player": player_name, "type": stat_type, "stats": db[player_name]}
    for name, stats in db.items():
        if player_name.lower() in name.lower() or name.lower() in player_name.lower():
            return {"player": name, "type": stat_type, "stats": stats}
    return {"player": player_name, "type": stat_type, "stats": None, "message": f"No stats found. Available: {', '.join(db.keys())}"}


def get_matchup_data(batter_name: str, bowler_name: str) -> dict:
    """Get head-to-head matchup data between a specific batter and bowler.
    Args:
        batter_name: Name of the batter (e.g., "Virat Kohli")
        bowler_name: Name of the bowler (e.g., "Rashid Khan")
    Returns:
        Dictionary with matchup analysis including advantage assessment.
    """
    batter = BATTING_STATS.get(batter_name, {})
    bowler = BOWLING_STATS.get(bowler_name, {})
    if not batter or not bowler:
        return {"batter": batter_name, "bowler": bowler_name, "analysis": "Insufficient data for matchup"}

    hand = batter.get("hand", "Right")
    style = bowler.get("style", "Unknown")
    econ_key = "vs_lhb_econ" if hand == "Left" else "vs_rhb_econ"
    relevant_econ = bowler.get(econ_key, bowler.get("overall_econ", 8.0))
    is_spin = any(w in style.lower() for w in ["spin", "leg", "off", "orthodox", "wrist"])
    batter_sr = batter.get("vs_spin_sr" if is_spin else "vs_pace_sr", batter.get("overall_sr", 130))
    advantage = "batter" if batter_sr > 140 and relevant_econ > 8.0 else "bowler" if relevant_econ < 7.5 else "even"

    return {
        "batter": batter_name, "bowler": bowler_name, "batter_hand": hand, "bowler_style": style,
        "batter_sr_vs_type": batter_sr, "bowler_econ_vs_hand": relevant_econ, "advantage": advantage,
        "analysis": f"{batter_name} ({hand}-hand) SR {batter_sr} vs {'spin' if is_spin else 'pace'}. {bowler_name} econ {relevant_econ} vs {hand.lower()}-handers. Advantage: {advantage.upper()}.",
    }


def get_venue_stats(venue_name: str) -> dict:
    """Get historical IPL statistics for a specific venue/ground.
    Args:
        venue_name: Name of the cricket venue (e.g., "Wankhede", "Chennai", "Eden Gardens")
    Returns:
        Dictionary containing venue statistics.
    """
    if venue_name in VENUE_STATS:
        return {"venue": venue_name, "stats": VENUE_STATS[venue_name]}
    for name, stats in VENUE_STATS.items():
        if venue_name.lower() in name.lower() or any(w.lower() in name.lower() for w in venue_name.split() if len(w) > 3):
            return {"venue": name, "stats": stats}
    return {"venue": venue_name, "stats": None, "message": f"Venue not found. Available: {', '.join(VENUE_STATS.keys())}"}
