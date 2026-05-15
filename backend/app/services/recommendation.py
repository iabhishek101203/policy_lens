from typing import Dict, List


def build_recommendations(item: Dict, user_profile: Dict) -> List[Dict]:
    recommendations = []
    base_category = item.get("category") or user_profile.get("category")

    if base_category:
        recommendations.append({
            "title": f"Related {base_category} scheme",
            "reason": "Matches your interest category",
        })

    if user_profile.get("state"):
        recommendations.append({
            "title": "State-specific policy recommendation",
            "reason": f"Relevant for {user_profile['state']}",
        })

    if user_profile.get("income_bracket") == "low":
        recommendations.append({
            "title": "Low-income support scheme",
            "reason": "Designed for low-income applicants.",
        })

    return recommendations
