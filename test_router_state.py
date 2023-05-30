import router_state


if router_state.isBlocked( what='chatgpt3'):
    print("ChatGPT is blocked")
else:
    router_state.change_state(what='chatgpt3',blocked=True)

router_state.change_state(what='chatgpt3',blocked=True)
