class Solution:
	def reverseString(self, s: List[str]) -> None:
		"""
		Do not return anything, modify s in-place instead.
		"""
		def revStr(st, start, end):
			if start >= end:
				return
			st[start], st[end] = st[end], st[start]
			revStr(st, start+1, end-1)

		revStr(s, 0, len(s)-1)