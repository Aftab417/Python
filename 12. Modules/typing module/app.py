
################----------------------   typing  -------------------#####################

#  It's a python standard library module that provide tools for 'type hint'.
#  Type hint help developers describe what types of values a functions, class, or a variable have.


from typing import Dict, List, Any, Optional, TypedDict, Annotated

##################----------------  Dict  --------------#################
#  A dictionary with a specified key and value types.
# e.g:
def get_users() -> Dict[str, int]:
    return {'id': 1, 'age' : 20}

#  Here Dict has str = key and int = value
 
  




##################----------------  List  --------------#################
#  A List with element of specific type.

def get_ids() -> List[int]:
    return [1, 2, 3]


#  Here List must contain intergers.






##################----------------  Any  --------------#################

# Means any type is allowed

def process(value:Any):
    print(value)   

#  You can pass str, dict, int  etc.






##################----------------  Optional  --------------#################

# Means a value can be of specific type of None.

def find_user(user_id:int) -> Optional[Dict[str, Any]]:
    if user_id == 1:
        return {
            'id' : 1,
            'name': 'Aftab'
        }
    return None







##################----------------  TypedDict  --------------#################

#  A special dictionary where you explicitly define the structure schema of key and values.

class UserDict(TypedDict):
    id: int
    name: str
    email: str


user: UserDict = {
    'id': 1, 
    'name': 'Aftab',
    'email': 'aftabkhan1567ss@gmail.com'
}


#  if you give the wrong keys or types, type checker (like MyPy) will flag it.







##################----------------  Annotated  --------------#################

# This lets you add metadata to type hint.
# Used by frameworks like LangGraph to add extra information.

def add(x:Annotated[int, 'must be positive'], y:int) -> int:
    return x + y


# In our code:
class AgentState(TypedDict):
    messages: Annotated[List, add_messages]


#  messages is a List
#  add_messages is metadata used by LangGraph to handle conversation history.









################----------------  Example Usage  ------------------##################

class AgentState(TypedDict):
    """Enhanced state for the multi-agent system"""
    messages: Annotated[List, add_messages]
    user_query: str
    discussion_result: Optional[Dict]
    sql_query: Optional[str]
    query_results: Optional[List[Dict]]
    response: Optional[str]
    current_agent: str
    reasoning_context: Optional[Dict]
