import router_state


if router_state.isBlocked( what='chatgpt3'):
    print("ChatGPT is blocked")
else:
    router_state.block(what='chatgpt3')

router_state.block(what='chatgpt3')
