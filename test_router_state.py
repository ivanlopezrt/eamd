import router_state

#example for Tania

#now two possible exceptions:
#1. InexistingRuleException -> did connect to router, but rule does not exist
#2. Exception -> could not connect to router

try:
    if router_state.isBlocked( what='kjdsfhfsdkj'):
        print("ChatGPT is blocked")
    else:
        router_state.change_state(what='sdmjgfsdkfj',blocked=True)

except router_state.InexistingRuleException as e:
    print("Exception: "+str(e))
except Exception as e:
    print("Error connecting to router: Exception: "+str(e))
