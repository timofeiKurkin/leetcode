class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # if len(s) == 1 or numRows == 1:
        #     return s

        # diagonal = numRows - 2
        # step = numRows + diagonal

        # def merge_arr(d2_arr: List[List[str]], arr: List[List[str]]) -> None:
        #     if not len(d2_arr):
        #         d2_arr.append(arr)
        #     else:
        #         for i in range(len(d2_arr)):
        #             d2_arr[i] += arr[i]

        # def run(s_arr: List[str], d2_arr: List[List[str]]) -> List[List[str]]:
        #     if not len(s_arr):
        #         return d2_arr

        #     column: List[List[str]] = [[item] for item in s_arr[:numRows]]
        #     z_items: List[str] = s_arr[numRows:step]

        #     if len(column) < numRows:
        #         # merge_arr(d2_arr, column)
        #         d2_arr += column
        #         return d2_arr

        #     for i in range(-1, numRows - 1, -1):
        #         column[i].append(z_items[i - 1])

        #     # merge_arr(d2_arr, column)
        #     d2_arr += column

        #     return run(s_arr[step:], d2_arr)

        # arr_res = run(list(s), [])
        # print(arr_res)

        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        curr_row = 0
        going_down = False

        for char in s:
            rows[curr_row] += char

            if curr_row == 0 or curr_row == numRows - 1:
                going_down = not going_down

            curr_row += 1 if going_down else -1

        return "".join(rows)


solution = Solution()

# print(solution.convert(s="PAYPALISHIRING", numRows=3))
print(solution.convert(s="PAYPALISHIRING", numRows=4))
# print(solution.convert(s="A", numRows=1))
