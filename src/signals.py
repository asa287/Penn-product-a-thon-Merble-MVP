# 信贷信号识别

def detect_signals(row):
    signals = []

    if row["credit_card_balance_change_"] > 0.3:
        signals.append("Liquidity stress")

    if row["tuition_payment"] > 5000:
        signals.append("Education expense")

    if row["recent_large_purchase"] == 1:
        signals.append("Major purchase")

    return signals