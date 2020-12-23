from aiohttp import web
import json
import aiohttp_jinja2
from bson import SON



@aiohttp_jinja2.template("header.html")
async def header(request):
    return {}

@aiohttp_jinja2.template("header.html")
async def middle(request):
    lst = {"content" : ["hi", "sayali"]}
    return (lst)



@aiohttp_jinja2.template("textbox.html")
async def textbox(request):
    return request

@aiohttp_jinja2.template("textbox.html")
async def submit(request):
    form = await request.post()
    text = str(form['textname'])
    return {"form":text}




@aiohttp_jinja2.template("msg_textbox.html")
async def msg_input_form(request):
    return {}

#storing the previous output
output_result = []


@aiohttp_jinja2.template("msg_textbox.html")
async def msg_submit_form(request):
    form = await request.post()
    text = form['msg_input']

    output_result.append(text)
    
    db = request.app['db'] 
    try:        
        msg_db = await db.command(SON([ ( "distinct", "collection"), ("key","msg"), ("query", {"msg" :text})]))
        try:
            msg_db = msg_db['values'][0]

        except Exception as e:
            print(e, 1)
            result = "can you say it again"   
            return { "result" : result, "output_result": output_result}       
                
        if msg_db == text:
            try:
                option1 = await db.command(SON([ ( "distinct", "collection"), ("key","option1"), ("query", {"msg" :text})]))
                option2 = await db.command(SON([ ( "distinct", "collection"), ("key","option2"), ("query", {"msg" :text})]))
                option1 = option1['values'][0]
                option2 = option2['values'][0]
                return { "form" : [option1, option2], "output_result": output_result}

            except:
                result = "SON failure"   
                return { "result" : result, "output_result": output_result}

    except Exception as e:
        print(e, 2)
        result = "can you say it again"   
        return { "result" : result, "output_result": output_result}
    
