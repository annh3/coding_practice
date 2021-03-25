def trap(self, height: List[int]) -> int:
        cur_x = 0
        last_seen_tallest = 0
        
        my_stack = []
        # (hleft, hright, x)
        
        reservoir = 0
        
        while cur_x < len(height):
            
            if height[cur_x] < last_seen_tallest:
                # push onto stack
                my_stack.append((last_seen_tallest, height[cur_x], cur_x))
                last_seen_tallest = height[cur_x]
            
            if height[cur_x] > last_seen_tallest:
                last_seen_tallest = height[cur_x]
            
            while len(my_stack) > 0 and height[cur_x] > my_stack[-1][1]:
                # pop and fill reservoir
                hleft, hright, x_left = my_stack.pop()
                h = min(height[cur_x], hleft)
                reservoir += (h-hright)*(cur_x-x_left)
                if hleft > last_seen_tallest:
                    last_seen_tallest = hleft
                if height[cur_x] < last_seen_tallest:
                    my_stack.append((hleft, height[cur_x], x_left))
                    last_seen_tallest = height[cur_x]
                    
                
            cur_x += 1
        
        return reservoir
        
