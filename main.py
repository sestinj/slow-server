from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
import random
import time
import json

app = FastAPI()

@app.post("/v1/chat/completions")
async def random_numbers(input_object: dict):
    def number_stream():
        for i in range(60 * 60):
            obj = json.dumps({"choices": [
                {"delta": {"content": str(i) + ", "}}
            ]})
            yield f"data: {obj}\n\n"
            time.sleep(1)

    return StreamingResponse(number_stream(), media_type="text/plain")