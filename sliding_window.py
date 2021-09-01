# Find the minimum window containing certain characters

def find_window(S, req_chars):

	counter = len(req_chars)
	req_map = {}
	
	for c in req_chars:
		req_map[c] += 1

	begin = 0
	end = 0
	head = 0
	substr_size = float("inf")

	# slide the end of the window
	while end < len(S):

		if S[end] in req_chars:
			req_map[S[end]] -= 1
			counter -= 1

		# make sure we have all the characters
		while(counter == 0):

			if end - begin + 1 < substr_size:
                substr_size = end - begin + 1
                head = begin
                # current best

			if S[begin] in req_map:
				req_map[S[begin]] += 1
				if req_map[S[begin]] > 0:
					counter += 1
					# make the window invalid

			begin += 1

		# keep searching

		end += 1

	return "" if substr_size == float("inf") else S[begin:begin+substr_size]

print(find_window("abcalgosomedailyr", "ad"))
