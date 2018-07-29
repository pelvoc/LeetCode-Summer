from collections import Counter
from itertools import groupby
from heapq import heappush, heappop


def chunks(board):
    return [''.join(g) for _, g in groupby(board)]


class Solution:
    def findMinStep(self, board, hand):
        counts = Counter(hand)
        queue = []

        heappush(queue, (0, board, counts))

        while len(queue) > 0:
            (count, current_board, hand_counts) = heappop(queue)
            board_chunks = chunks(current_board)

            if len(board_chunks) == 0:
                return count

            for i in range(len(board_chunks)):
                chunk_char = board_chunks[i][0]
                chunk_len = len(board_chunks[i])
                hand_count = hand_counts.get(chunk_char, 0)
                need_count = max(0, 3 - chunk_len)
                assert(hand_count >= 0)

                if need_count <= hand_count:
                    next_hand_counts = hand_counts.copy()
                    next_hand_counts[chunk_char] = hand_count - need_count
                    next_board = ''.join(board_chunks[0:i] + board_chunks[i + 1:])

                    heappush(queue, (count + need_count, next_board, next_hand_counts))

        return -1