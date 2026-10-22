from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse
import json
# from django.http.response import StreamingHttpResponse
from openai import OpenAI
from openai.types.responses import ResponseTextDeltaEvent, ResponseOutputItemDoneEvent, ResponseFunctionToolCall

client = OpenAI()

# Create your views here.
def home(request):
    return render(request, "mysite/index.html")

def chat_test(request):
    def _responses_event(prompt):
        stream = client.responses.create(
            model="gpt-5.4-mini",
            instructions="Respond in markdown",
            input=prompt,
            stream=True,
        )
        
        for event in stream:
            if isinstance(event, ResponseTextDeltaEvent):
                payload = json.dumps({"chunk": event.delta, "done": False})
                yield f"data: {payload}\n\n"
        
        done = json.dumps({"chunk": "", "done": True})
        yield f"data: {done}\n\n"
                
    if request.method == "POST":
        prompt = request.POST["prompt"]
           
        response =  StreamingHttpResponse(_responses_event(prompt=prompt), content_type="text/event-stream")
        response["Cache-Control"] = "no-cache"
        response["X-Accel-Buffering"] = "no"
        
        return response
        
    else:
        return HttpResponse("hi")