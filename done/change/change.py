def find_fewest_coins(coins: list, target: int) -> list:
    if target == 0:
        return []

    if target < 0:
        raise ValueError("target can't be negative")

    dp = [float("inf")] * (target + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, target + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[target] == float("inf"):
        raise ValueError("can't make target with given coins")

    result = []
    current_value = target
    for coin in reversed(coins):
        while (
            current_value >= coin and dp[current_value] == dp[current_value - coin] + 1
        ):
            result.append(coin)
            current_value -= coin

    return result[::-1]
