from views import header, middle, textbox, submit, msg_input_form, msg_submit_form

def routes(app):
    app.router.add_get('/', header)
    app.router.add_get('/middle', middle)

    app.router.add_get('/textbox', textbox)
    app.router.add_post('/textbox', submit, name='text')

    app.router.add_get("/msg", msg_input_form)
    app.router.add_post("/msg", msg_submit_form, name='msg_handle')