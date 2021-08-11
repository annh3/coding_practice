"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        # like a DFS, where you keep adding
        
        # learning - let's use a hashmap emap = {e.id: e for e in employees}
        
        emap = {e.id: e for e in employees}
        
        # using this for when we get a list of complex, interlinked objects
        visited = set()
        
        def dfs(eid):
            employee = emap[eid]
            
            return (employee.importance + sum(dfs(eid) for eid in employee.subordinates))
                    
            
        
        value = dfs(id)
        return value
