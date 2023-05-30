import router_state

#example for Tania

try:
    if router_state.isBlocked( what='chatgpt3'):
        print("ChatGPT is blocked")
    else:
        router_state.change_state(what='chatgpt3',blocked=True)
except Exception as e:
    print("Exception: "+str(e))
