Problem Description:
You are given an array prices where prices[i] is the price of the i-th item. You are also given an integer k representing the total number of vouchers available.

Each voucher can be applied to any item. When a voucher is applied to an item, it halves the item's current price (using floor division). You can apply multiple vouchers to the same item, and each voucher stacks, i.e.:

1 voucher: floor(price / 2)

2 vouchers: floor(floor(price / 2) / 2), and so on...

You must use exactly k vouchers. After using all the vouchers, calculate the minimum total cost you have to pay for all items.

🧠 Your Task:
Return the minimum total cost after applying the k vouchers optimally.
You may also return the final price of each item or the number of vouchers applied per item if needed.
                                                                                                               

                                                                                                               
                                                                                                               import heapq
import math

def minimize_cost_with_vouchers(prices, k):
    n = len(prices)
    current_prices = prices[:]
    voucher_counts = [0] * n

    # Max heap: (-saving, index)
    heap = []
    for i, price in enumerate(prices):
        next_price = price // 2
        saving = price - next_price
        heapq.heappush(heap, (-saving, i, price, 0))  # (neg_saving, index, current_value, vouchers_used)

    for _ in range(k):
        if not heap:
            break  # no more useful vouchers to apply

        neg_saving, i, current_value, count = heapq.heappop(heap)
        count += 1
        new_price = current_value // 2
        current_prices[i] = new_price
        voucher_counts[i] = count

        # Prepare for the next round
        if new_price > 0:
            next_price = new_price // 2
            saving = new_price - next_price
            heapq.heappush(heap, (-saving, i, new_price, count))

    total_cost = sum(current_prices)
    return total_cost, voucher_counts, current_prices

                                                                                                               
                                                                                                               
