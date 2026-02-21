def apply_guardrails(response: str) -> str:
    """
    Apply medical safety guardrails to generated response.
    """

    restricted_keywords = [
        "prescribe",
        "dosage",
        "take 500mg",
        "medical prescription"
    ]

    for word in restricted_keywords:
        if word in response.lower():
            return "⚠️ I cannot provide prescription or dosage advice. Please consult a licensed medical professional."

    disclaimer = (
        "\n\n---\n⚠️ This information is for educational purposes only. "
        "Consult a qualified healthcare professional."
    )

    return response + disclaimer